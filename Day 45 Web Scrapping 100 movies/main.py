from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

article_texts = []
article_tags = []

all_spans = soup.find_all('span', class_='titleline')

for span in all_spans:
    article_text = span.find("a").getText()
    article_texts.append(article_text)

    article_tag = span.find("a").get("href")
    article_tags.append(article_tag)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_tags)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_number, largest_index)


# article_upvote = soup.find(name="span", class_="score").getText()
# print(target_link)
# print(article_upvote)

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# #
# # print(soup)
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find_all(name="h1", id="name")
# print(heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one("#name")
# print(name)
