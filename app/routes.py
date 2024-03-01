from flask import render_template, redirect, url_for, flash, request
from app import app
from app.forms import AnalysisForm
from nltk.sentiment.vader import SentimentIntensityAnalyzer

@app.route('/')
def index():
    form = AnalysisForm()
    return render_template('index.html', form=form)

@app.route('/analyze', methods=['POST'])
def analyze():
    form = AnalysisForm()
    if form.validate_on_submit():
        text = form.text.data  # Get the text input from the form
        sentiment = analyze_sentiment(text)  # Perform sentiment analysis
        return render_template('result.html', text=text, sentiment=sentiment)
    return render_template('index.html', form=form)

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'Positive'
    elif scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'