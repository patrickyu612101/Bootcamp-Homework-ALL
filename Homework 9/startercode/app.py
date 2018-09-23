from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
# Use flask_pymongo to set up mongo connection



@app.route("/")
def index():
    alldata = scrape_mars.scrape_all()
    title=alldata["news_title"]
    paragraph=alldata["news_paragraph"]
    imgurl=alldata["imgurl"]
    fact=alldata["fact"]
    hemispheresInfo=alldata["hemispheresInfo"]
    weather=alldata["weather"]
    return render_template("index.html", title=title,paragraph=paragraph,imgurl=imgurl,fact=fact,weather=weather)


# @app.route("/scrape")
# def scrape():
#    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

