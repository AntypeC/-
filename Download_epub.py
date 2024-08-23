import pypub, requests
from bs4 import BeautifulSoup

book_index = 110034 #http://www.kdxx.net/txt/91818.html
r = requests.get(f'http://www.kdxx.net/read/{book_index}/')
soup = BeautifulSoup(r.text, features="html.parser")
find_N = str(soup.find_all(id="indexselect")).split(f'</option><option value="/read/{book_index}/')
N = int(find_N[-1].split('/">')[0])
chapter_index = []

for i in range(N):
    s = BeautifulSoup(requests.get(f'http://www.kdxx.net/read/{book_index}/{i+1}').text, features="html.parser")
    dict = str(s.find(id="content_1")).split(f'<a href="/read/{book_index}/')

    print(f"Generating chapter(s) index... {i+1}/{N}")

    for j in range(len(dict)):
        n = dict[j].split(".")[0]
        if j ==0:
            continue
        elif n not in chapter_index:
            chapter_index.append(n)

print("Done! Creating a new epub...")

info1 = str(soup.find_all(id="info1")).split(f'<a href="/txt/{book_index}.html">')[1].split("</a></h1>")
title = info1[0]
author = info1[1].split("author/")[1].split('/"')[0]

book = pypub.Epub(title, creator=author)

for chapter in chapter_index:
    while True:
        try:
            part_1 = pypub.create_chapter_from_url(f"http://www.kdxx.net/read/{book_index}/{chapter}.html")
            part_2 = pypub.create_chapter_from_url(f"http://www.kdxx.net/read/{book_index}/{chapter}_2.html")
            book.add_chapter(part_1)
            book.add_chapter(part_2)
            print(f"Copied chapter {chapter_index.index(chapter)+1}: {chapter}.html")
        except Exception as e:
            print(f"Experienced error timed out, rerequesting chapter {chapter_index.index(chapter)+1}: {chapter}.html")
            continue
        break

pwd = r"C:\Users\AntypeC\dev\吞噬星空\untitled.epub"
book.create(pwd)

print(f"Done! New book saved at {pwd}.")
