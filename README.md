# AI-Powered Text Generation and Sentiment Analysis Dashboard

This Flask web application performs text sentiment analysis and text generation based on user input. Users can input text, and the application will analyze its sentiment using NLTK's Vader sentiment analysis tool and generate additional text using the GPT-2 model.

## Features

- Input text for sentiment analysis.
- Perform sentiment analysis using NLTK's Vader sentiment analysis tool.
- Generate additional text based on the input text using the GPT-2 model.
- View sentiment analysis results along with the input text and generated text.
- Navigation back to the input page from the result page.

## Technologies Used

- **Python**: Backend development and text analysis.
- **Flask**: Web framework for building the application.
- **NLTK (Natural Language Toolkit)**: Library for natural language processing tasks such as sentiment analysis.
- **Hugging Face Transformers**: Library for accessing pre-trained natural language processing models for text generation, including GPT-2.
- **HTML/CSS**: Frontend development for web interface and styling.
- **Bootstrap**: Frontend framework for responsive design and layout.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vinit714/AI-Powered-Text-Generation-and-Sentiment-Analysis-Dashboard.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    
3. run the NLTK download command to download the vader_lexicon resource:
    ```bash
    python -m nltk.downloader vader_lexicon
    ```
    and
   ```bash
   python -m nltk.downloader reuters
   ```

5. Run the application:

    ```bash
    python run.py
    ```

6. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Navigate to the home page.
2. Enter text into the provided form.
3. Submit the form for sentiment analysis and text generation.
4. View the sentiment analysis results and additional generated text on the result page.
5. Use the provided button to navigate back to the input page.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or create a pull request.
