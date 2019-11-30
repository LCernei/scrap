# For flask implementation
from flask import Flask, render_template, request, redirect, url_for
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os

app = Flask(__name__)
title = "Web Scrapper"

client = MongoClient("mongodb://127.0.0.1:27017")  # host uri
db = client.scrapedProducts  # Select the database
products = db.products  # Select the collection name


def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


@app.route("/")
@app.route("/list")
def lists():
    products_l = products.find()
    a1 = "active"
    return render_template('index.html', a1=a1, products=products_l, t=title)


if __name__ == "__main__":

    app.run()
