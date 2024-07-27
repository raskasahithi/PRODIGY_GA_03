# Character-Level Markov Chain Predictor

This project implements a character-level Markov chain model for predicting the next character based on a given seed character. It consists of a backend using Flask and a frontend with HTML, CSS, and JavaScript.

## Project Structure

- **Backend**:
  - `app.py`: The Flask application that serves the web interface and handles prediction requests.
  - `markov_char.py`: Contains the Markov chain model for character-level prediction.

- **Frontend**:
  - `templates/index.html`: The main HTML file for the web interface.
  - `static/styles.css`: The CSS file for styling the web interface.
  - `static/script.js`: The JavaScript file for handling AJAX requests and updating the UI.

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

   Ensure `requirements.txt` includes:
    ```plaintext
    Flask
    ```

## Usage

1. **Prepare your dataset**: Create a file named `dataset.txt` and add the text data you want to use for training the model.

2. **Run the Flask application**:
    ```bash
    python app.py
    ```

   The application will start and be accessible at `http://127.0.0.1:5000/`.

3. **Open your browser** and navigate to `http://127.0.0.1:5000/`.

4. **Interact with the web interface**:
    - Enter a seed character in the "Seed Character" input field.
    - Specify the number of predictions in the "Number of Predictions" field.
    - Click "Get Predictions" to see the results.

## Screenshots

### Web Interface

**Form View**:

![Form View](https://via.placeholder.com/600x400?text=Form+View)

**Predictions View**:

![Predictions View](https://via.placeholder.com/600x400?text=Predictions+View)

## Example Output

**Example Prediction List**:

In the web interface, after submitting the seed word `example` with `5` predictions, the results might appear as:

- Previous word: `example`, Next word: `word1`
- Previous word: `word1`, Next word: `word2`
- Previous word: `word2`, Next word: `word3`
- Previous word: `word3`, Next word: `word4`
- Previous word: `word4`, Next word: `word5`


## File Descriptions

- **`app.py`**: Defines the Flask app, handles requests, and serves the web interface.
- **`markov_char.py`**: Implements the Markov chain model for character prediction.
- **`templates/index.html`**: Provides the HTML structure and form for user input.
- **`static/styles.css`**: Contains CSS styles for the web interface.
- **`static/script.js`**: Manages form submission and AJAX requests.

## Troubleshooting

- **No predictions**: Ensure that `dataset.txt` has enough data and is properly formatted. Check the training output in the console to confirm that the model is being trained correctly.
- **AJAX errors**: Check the browser console for JavaScript errors and inspect network requests for issues with API calls.
- **Model not trained**: Verify that the `dataset.txt` path is correct and the file is accessible. Make sure the data is being read and processed correctly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on the project's GitHub repository or contact [your-email@example.com](mailto:your-email@example.com).

