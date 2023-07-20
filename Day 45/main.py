import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.select(selector=".titleline a[rel]")

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [score.getText().split()[0] for score in soup.select(selector=".subtext .subline .score")]

print(article_texts)
print(article_links)
print(article_upvotes)
