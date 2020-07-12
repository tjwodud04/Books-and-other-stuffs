from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Scrapper")

db = {}

@app.route("/")
def home():
    return render_template("search.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        fromDB = db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)

app.run()