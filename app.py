import json
import random
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
from pprint import pprint


app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

# 1. はてブのホットエントリーページ
@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    # **** ここを実装します（基礎課題） ****
    # 1. はてブのホットエントリーページのHTMLを取得する
    with urlopen("https://b.hatena.ne.jp/hotentry/all") as res:
        html = res.read().decode("utf-8")
    # 2. BeautifulSoupでHTMLを読み込む
    soup = BeautifulSoup(html, "html.parser")
    # pprint(soup)
    # 3. 記事一覧を取得する
    items = soup.select(".js-keyboard-openable")
    # print(items[1])
    # 4. ランダムに1件取得する
    shuffle(items)
    # print(items)
    item = items[0]["title"]
    url = items[0]["href"]
    # pprint(items)
    # 5. 以下の形式で返却する.
    return json.dumps({
        "content": item,
        # "link" : item.find("link").string
        "link": url
    })
    
# 2. JDN （デザイン）
@app.route("/api/recommend_design")
def api_recommend_design():
    
        # **** ここを実装します（発展課題） ****
    with urlopen("https://www.japandesign.ne.jp/news/") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(" .c-box ")
    shuffle(items)
    item = items[0]
    url = item.find("a")
    print(item)
    return json.dumps({
        "content": item.find(class_="c-box_title").text,
        # "link" : item.find("link").string
        "link": url.get("href")
    })

# 3. アーキテクチャフォト （建築）
@app.route("/api/recommend_architecture")
def api_recommend_architecture():

    with urlopen("https://architecturephoto.net/feature/") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".VisualList__title")
    shuffle(items)
    
    item = items[0].text
    pprint(item)
    url = items[0]["href"]
    return json.dumps({
        "content": item,
        "link": url
    })

# 2. JDN （デザイン）


@app.route("/api/recommend_art")
def api_recommend_art():

    # **** ここを実装します（発展課題） ****
    with urlopen("https://bijutsutecho.com/") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select(".home_item")
    shuffle(items)
    item = items[0]
    news = item.find("span")
    url = item.find("a")
    pprint(item)
    return json.dumps({
        "content": news.text,
        # "link" : item.find("link").string
        "link": url.get("href")
    })


    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
