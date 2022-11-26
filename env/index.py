from flask import Flask,render_template, request
import csv
import io 
import joblib

#importing naive.joblib
#importing Tree.joblib

naive_bayes = joblib.load('modelPersistence\naive.joblib')
tree = joblib.load('modelPersistence\Tree.joblib')


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def index(name=None):   
    return render_template('index.html')

@app.post('/result')
def result():
    data = request.form
    job = request.form.get('job')
    maritalStatus = request.form.get('marital_status')
    education = request.form.get('education')
    housing = request.form.get('housing')
    loan = request.form.get('loan')
    contact = request.form.get('contact')
    month = request.form.get('month')
    outcome = request.form.get('outcome')
    target = request.form.get('target')

    return f'{data}{job}{maritalStatus}{education}{housing}{loan}{contact}{month}{contact}{target} '



