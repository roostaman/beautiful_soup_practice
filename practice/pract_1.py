import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# only 1 article
# article_text = soup.find(name="span", class_="titleline")
# print(article_text.get_text())
# article_link = article_text.a["href"]
# print(article_link)
# article_upvote = soup.find(name="span", class_="score", id="score_39850318")
# print(article_upvote.get_text())

articles_list = []
articles_links = []

# all articles
articles = soup.find_all(name="span", class_="titleline")

for article_tag in articles:
    article_text = article_tag.get_text()
    articles_list.append(article_text)

    article_link = article_tag.a["href"]
    articles_links.append(article_link)

print(articles_list, "\n", articles_links)

upvotes = [int(score.get_text().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]
print(upvotes)

highest_score = max(upvotes)
highest_i = upvotes.index(highest_score)
print(highest_score, "\n", highest_i)
print(articles_list[highest_i])
print(articles_links[highest_i])
