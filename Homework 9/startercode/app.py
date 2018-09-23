from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection



@app.route("/")
def index():
    datas = scrape_mars.scrape_all()
    alldata={
        "title":datas["news_title"],
        "paragraph":datas["news_paragraph"],
        "imgurl":datas["imgurl"],
        "weather":datas["weather"],
        "fact":datas["fact"],
        "hemispheresInfo":datas["hemispheresInfo"]
    }
    return render_template("index.html", alldata=alldata)


@app.route("/scrape")
def scrape():
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

