from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
oneclass = soup.findAll("a")
article_text = oneclass
article_line = oneclass.get("href")
print(article_text)
article_upvote = soup.findAll("span", class_="score")
print(article_upvote.getText())




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.findAll(name="a"))
# all_anchor_tags = soup.findAll(name="a")
# # print(all_anchor_tags)
#
# # for tags in all_anchor_tags:
# #     print(tags.getText())
# #     print(tags.get("href"))
#
# class_is_heading = soup.findAll(class_="heading")
# print(class_is_heading)
#
# h3_heading = soup.findAll("h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# heading = soup.select(".heading")
# print(heading)