import indeed as ind
import stackoverflow as stf
import save
from flask import Flask, render_template, request, redirect

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
            searchResult = ind.startScrap(searchedJob)
            db[searchedJob]=searchResult
        return render_template(
            "result.html", searched=searchedJob, searchResult=searchResult
        )  # 인자를 넘겨서 템플릿을 구성 => soSexxxy
    else:
        return redirect("/")


print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
