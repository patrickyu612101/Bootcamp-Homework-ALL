from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/misstion_to_mars"
mongo = PyMongo(app)


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


if __name__ == "__main__":
    app.run(debug=True)

