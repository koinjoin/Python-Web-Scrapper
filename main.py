import indeed as ind
import stackoverflow as stf
import save
from flask import Flask

# ind_jobs = ind.startScrap()
# stf_jobs = stf.startScrap()
# save.save_to_file(ind_jobs, 'ind_jobs')
# save.save_to_file(stf_jobs, 'stf_jobs')

app = Flask("myScrapper")

@app.route("/")
def home():
    return "Hello People"

app.run()