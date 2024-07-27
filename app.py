from flask import Flask, request, jsonify, render_template
from markov_word import MarkovWordPredictor, load_training_text

app = Flask(__name__)

# Initialize the word predictor
predictor = MarkovWordPredictor()


# Load and train the model with the dataset
def load_and_train_dataset(file_path):
    with open(file_path, 'r') as file:
        dataset_text = file.read()
        predictor.train(dataset_text)


# Path to your dataset file
dataset_file_path = 'dataset.txt'
load_and_train_dataset(dataset_file_path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    seed_word = data.get('seed_word', '')
    num_predictions = data.get('num_predictions', 5)
    print(f"Received seed_word: {seed_word}, num_predictions: {num_predictions}")  # Debug statement
    predictions = predictor.generate_predictions(seed_word, num_predictions)
    print(f"Predictions: {predictions}")  # Debug statement
    return jsonify({'predictions': predictions})


if __name__ == '__main__':
    app.run(debug=True)
