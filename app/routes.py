from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import AnalysisForm
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import gpt_2_simple as gpt2

# Download the GPT-2 model (only need to run this once)
gpt2.download_gpt2(model_name="124M")

@app.route('/')
def index():
    form = AnalysisForm()
    return render_template('index.html', form=form)

@app.route('/analyze', methods=['POST'])
def analyze():
    form = AnalysisForm()
    if form.validate_on_submit():
        text = form.text.data  # Get the text input from the form
        sentiment, sentiment_scores, major_words, generated_text = analyze_text(text)
        return render_template('result.html', text=text, sentiment=sentiment, sentiment_scores=sentiment_scores, major_words=major_words, generated_text=generated_text)
    return render_template('index.html', form=form)

def analyze_text(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    
    # Tokenize the text
    words = word_tokenize(text)
    
    positive_words = []
    negative_words = []
    neutral_words = []

    for word in words:
        word_score = sid.polarity_scores(word)
        if word_score['compound'] >= 0.5:
            positive_words.append(word)
        elif word_score['compound'] <= -0.5:
            negative_words.append(word)
        else:
            neutral_words.append(word)

    major_words = {
        'Positive': positive_words,
        'Negative': negative_words,
        'Neutral': neutral_words
    }
    
    # Text generation using GPT-2
    generated_text = gpt2.generate(sess=None, model_name='124M', prefix=text, length=100, return_as_list=True)[0]
    
    # Overall sentiment
    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, scores, major_words, generated_text
