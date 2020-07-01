import indeed as ind
import stackoverflow as stf
import save
from flask import Flask, render_template, request, redirect
from exporter import save

# ind_jobs = ind.startScrap("python")
# stf_jobs = stf.startScrap("python")
# save.save_to_file(ind_jobs, 'ind_jobs')
# save.save_to_file(stf_jobs, 'stf_jobs')

app = Flask("myScrapper")
db = {}

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    searchedJob = request.args.get("job")
    if searchedJob:
        fromDb = db.get(searchedJob)
        if fromDb:
            searchResult = fromDb
        else:
            searchResult = stf.startScrap(searchedJob)
            db[searchedJob]=searchResult
        return render_template(
            "result.html", searched=searchedJob, searchResult=searchResult, num=len(searchResult)
        )  # 인자를 넘겨서 템플릿을 구성 => soSexxxy
    else:
        return redirect("/")

@app.route("/export")
def export():
    try:
        job = request.args.get('job')
        if not job:
            raise Exception()
        jobs = db.get(job)
        if not jobs:
            raise Exception()
        save(jobs, job)
        return redirect("/")
    except:
        return redirect("/")

print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
