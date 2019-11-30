from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "Web Scrapper"

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.scrapedProducts  # Select the database
products = db.products  # Select the collection name


@app.route("/")
@app.route("/list")
def list_products():
    products_l = products.find()
    return render_template('index.html', products=products_l, title=title)


if __name__ == "__main__":
    app.run()
