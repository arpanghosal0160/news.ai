from flask import Flask, request, jsonify
from summarizer import summarize_text  # Use your summarization logic
from news_fetcher import fetch_news  # Your news fetching logic

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    try:
        # Fetch news and summarize
        news = fetch_news(query)
        summary = summarize_text(news)
        return jsonify({'summary': summary})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
