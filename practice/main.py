from bs4 import BeautifulSoup
# import lxml

with open("website.html", mode="r") as source:
    html_content = source.read()

soup = BeautifulSoup(html_content, "html.parser")

# print(soup.title)
# print(soup.title.string)

all_anchor = soup.find_all(name="a")
# print(all_anchor)

# for tag in all_anchor:
#     print(tag.get_text())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_headings = soup.find_all(name="h3", class_="heading")
section_heading = soup.find(name="h3", class_="heading")  # first found h3, heading

# print(section_heading.get_text())

name = soup.select("h3")
# print(name)  # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]

name_one = soup.select_one("h3")
print(name_one)  # <h3 class="heading">Books and Teaching</h3>

print(name_one.get_text())  # Books and Teaching
