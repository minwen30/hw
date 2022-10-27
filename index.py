from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
app = Flask(__name__)

@app.route("/")
def index():
    homepage += "<a href=/hw>資管二B 411003829 鄭捷妤 求職相關資訊</a><br>"
    return "hw.html"

#if __name__ == "__main__":
#    app.run()