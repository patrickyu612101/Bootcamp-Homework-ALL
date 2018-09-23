from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
print(app)
# Use flask_pymongo to set up mongo connection



@app.route("/")
def index():
    
   return render_template("index.html", news_title=news_title, news_paragraph=news_paragraph)


@app.route("/scrape")
def scrape():
   pass


if __name__ == "__main__":
    app.run()
