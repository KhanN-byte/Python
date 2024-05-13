'''

Fetch the top 5 trending business articles around the world!
Developer - Haris Khan

Request Params:
- category = technology, business, sports, entertainment, general, health, science

'''
import requests


def get_top_news(api_key, country_code):
    url = 'https://newsapi.org/v2/top-headlines'

    final_url = f'{url}?country={country_code}&category=technology&apiKey={api_key}'
    response = requests.get(final_url)
    if response.status_code == 200:
        data = response.json()
        articles = data['articles']
        return articles[:5]  # Get the top 5 articles
    else:
        print("Failed to fetch news:", response.text)
        return []

def print_news(articles):
    for i, article in enumerate(articles, start=1):
        print(f"{i}. {article['title']}")
        print(article['description'])
        print(article['url'])
        print()

def main():

    api_key = '<your_api_key>'
    # Get your API key from newsapi.org

    for i in ['in', 'us', 'cn', 'fr', 'uk', 'sg', 'de']:
        print(f'Countries: {i} \n')
    cc = str(input("From the list of countries, enter a code: "))
        
    top_news = get_top_news(api_key, cc)
    if top_news:
        print("Top 5 Latest News Headlines:")
        print_news(top_news)
    else:
        print("No news articles found.")

if __name__ == "__main__":
    main()
