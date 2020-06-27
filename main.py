import indeed as ind
import stackoverflow as stf
import save
from flask import Flask, render_template, request

# ind_jobs = ind.startScrap()
# stf_jobs = stf.startScrap()
# save.save_to_file(ind_jobs, 'ind_jobs')
# save.save_to_file(stf_jobs, 'stf_jobs')

app = Flask("myScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result")
def result():
    searchedJob = request.args.get("job")

    return render_template(
        "result.html", searched=searchedJob
    )  # 인자를 넘겨서 템플릿을 구성 => soSexxxy


print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
