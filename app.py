from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze-sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')

    if not text.strip():
        return jsonify({'sentiment': 'Neutral', 'score': {}})  # If text is empty, return Neutral

    sentiment_score = analyzer.polarity_scores(text)
    compound_score = sentiment_score['compound']  # Extract compound score

    # Adjust classification thresholds
    if compound_score >= 0.3:  # More lenient for short texts
        sentiment = "Positive"
    elif compound_score <= -0.3:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return jsonify({'sentiment': sentiment, 'score': sentiment_score})

if __name__ == '__main__':
    app.run(debug=True)
