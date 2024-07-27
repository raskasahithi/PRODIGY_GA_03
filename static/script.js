$(document).ready(function () {
    // Handle prediction request
    $('#predictor-form').submit(function (event) {
        event.preventDefault();

        const seedWord = $('#seed_word').val();
        const numPredictions = $('#num_predictions').val();

        const data = {
            seed_word: seedWord,
            num_predictions: parseInt(numPredictions)
        };

        $.ajax({
            url: '/predict',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                const predictionsList = $('#predictions-list');
                predictionsList.empty();
                response.predictions.forEach(prediction => {
                    const listItem = `<li>Previous word: '${prediction[0]}', Next word: '${prediction[1]}'</li>`;
                    predictionsList.append(listItem);
                });
            },
            error: function (xhr, status, error) {
                console.error('Error predicting next word:', error);
                alert('An error occurred while predicting. Please try again.');
            }
        });
    });
});
