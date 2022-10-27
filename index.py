from flask import Flask, render_bag, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411003829 鄭捷妤 求職相關資訊</h1>"
    homepage += "<a href=/me>我的個人簡介</a><br>"
    homepage += "<a href=/school>求職履歷自傳</a><br>"
    homepage += "<a href=/photo>職涯測驗結果</a><br>"
    homepage += "<a href=/mis>MIS相關工作介紹</a><br>"
    return homepage

@app.route("/me")
def me():
    return render_bag("me.html")

@app.route("/school")
def school():
    return render_bag("school.html")

@app.route("/photo")
def photo():
    return render_bag("photo.html")

@app.route("/mis")
def mis():
    return render_bag("mis.html")

#if __name__ == "__main__":
#    app.run()