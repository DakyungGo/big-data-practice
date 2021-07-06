from bs4 import BeautifulSoup

html = """
<html><body>
<div id="project">
    <h1 id='title'>BIG DATA PROGRAMMING</h1>
    <p id='body'>DATA ANLYSIS AND SCIENCE</p>
    <p>DATA ACQUISITION PART1</p>
    <ul class="items">
        <li>CRAWLING</li>
        <li>SCRAPPING</li>
        <li>HYBIRD WAY</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p2.string)

title = soup.find(id="title")
body = soup.find(id="body")

print("#title=" + title.string)
print("#body=" + body.string)

h1 = soup.select_one("div#project > h1").string
print("h1 =", h1)

li_list = soup.select("div#project > ul.items > li")
for li in li_list:
    print("li =", li.string)
