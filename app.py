from flask import Flask, render_template, request, redirect, url_for
import jsonify
import requests
import pickle
import numpy as np
import sklearn

#creating instance of the class
app=Flask(__name__)

model = pickle.load(open('random.pkl', 'rb'))

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/failure')
def failure():
    return render_template('failure.html')

@app.route('/result',methods = ['GET','POST'])
def result():
    if request.method == 'POST':
        hsc_com = 0
        hsc_sci = 0
        sscp = (float)(request.form['ssc'])
        hscp = (float)(request.form['hsc'])
        hscs = (int)(request.form['hsc_stream'])
        if hscs=='2':
            hsc_com = 1
            hsc_sci = 0
        if hscs=='3' :
            hsc_sci = 1
            hsc_com = 0
        degp = (float)(request.form['deg'])
        mbap = (float)(request.form['mba'])
        spec = (int)(request.form['specialization'])
        empp = (float)(request.form['emp'])
        wrke = (int)(request.form['work'])
        prediction = model.predict([[sscp, hscp, degp, empp, mbap, hsc_com, hsc_sci, wrke, spec]])
        output=prediction[0]
        if int(output)==1:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))

if __name__ == "__main__":
	app.run(debug=True)

