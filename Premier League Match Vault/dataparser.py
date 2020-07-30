import pandas as pd
import numpy as np
import csv
from flask import Flask, render_template, request
import sys

app = Flask(__name__)

data = pd.read_csv('results.csv')

@app.route("/", methods = ['POST', 'GET'])
def teamTable():
    if request.method == 'POST':
        team = request.form["Team"]
        year = request.form["Year"]
        newtable = data[((data['home_team'] == team) | (data['away_team'] == team)) & (data['season'] == year)]
        return f"<p>{newtable.to_html()}</p>"
              
    else:
        return render_template('index.html')   

if __name__ == '__main__':
    app.run(debug=True)
     
