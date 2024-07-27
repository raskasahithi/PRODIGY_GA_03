import random
import re
from collections import defaultdict


class MarkovWordPredictor:
    def __init__(self):
        self.model = defaultdict(lambda: defaultdict(int))

    def train(self, text):
        words = re.findall(r'\b\w+\b', text.lower())
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.model[current_word][next_word] += 1

        # Debug: Print a sample of the model
        print(f"Model trained with {len(words)} words. Model structure:")
        for word, next_words in list(self.model.items())[:10]:
            print(f"{word}: {dict(next_words)}")

    def generate_predictions(self, seed_word, num_predictions=5):
        predictions = []
        current_word = seed_word
        for _ in range(num_predictions):
            next_word = self.predict(current_word)
            if next_word:
                predictions.append((current_word, next_word))
                current_word = next_word
            else:
                break
        return predictions

    def predict(self, current_word):
        next_words = self.model.get(current_word.lower(), {})
        print(f"Predicting for '{current_word}'. Next words: {next_words}")  # Debug statement
        if not next_words:
            return None
        next_word = random.choices(
            population=list(next_words.keys()),
            weights=next_words.values()
        )[0]
        return next_word


def load_training_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
