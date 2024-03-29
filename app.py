import datetime
import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URL"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            post_entry(request)
            entries_with_date = retrieve_entries()

        if request.method == "GET":
            entries_with_date = retrieve_entries()

        return render_template("home.html", entries=entries_with_date)

    def retrieve_entries():
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"),
            )
            for entry in app.db.entries.find()
        ]
        return entries_with_date

    def post_entry(request):
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

    return app
