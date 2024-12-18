import requests

API_KEY = "efdc6ebf45f57603a52a1e30953bcdba"  # Replace with your GNews API key

def fetch_news(query="Technology", max_results=5):
    """
    Fetch the latest news using the GNews API.
    :param query: Search query for news articles
    :param max_results: Maximum number of articles to fetch
    :return: List of articles with title and content
    """
    url = f"https://gnews.io/api/v4/search?q={query}&token={API_KEY}&lang=en&max={max_results}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [{"title": a["title"], "content": a["description"]} for a in articles]
        else:
            print(f"Error fetching news: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print("An error occurred while fetching news:", e)
        return []

# Test fetch_news function
if __name__ == "__main__":
    news = fetch_news("Technology")
    for idx, article in enumerate(news):
        print(f"{idx+1}. {article['title']}\n{article['content']}\n")
