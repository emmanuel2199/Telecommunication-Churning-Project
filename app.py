from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
import matplotlib
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        
        account_length=int(request.form['account_length'])
        voice_mail_plan=int(request.form['voice_mail_plan'])
        voice_mail_messages=int(request.form['voice_mail_messages'])
        day_mins=float(request.form['day_mins'])
        evening_mins=float(request.form['evening_mins'])
        night_mins=float(request.form['night_mins'])
        international_mins=float(request.form['international_mins'])
        customer_service_calls=int(request.form['customer_service_calls'])
        international_plan=int(request.form['international_plan'])
        day_calls=int(request.form['day_calls'])
        evening_calls=int(request.form['evening_calls'])
        night_calls=int(request.form['night_calls'])
        international_calls=int(request.form['international_calls'])
        total_charge=float(request.form['total_charge'])
        
        

 
        prediction = model.predict([[account_length,voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins,customer_service_calls,international_plan,day_calls,evening_calls,night_calls,international_calls,total_charge]])
        if prediction==1:
             return render_template('index.html',prediction_text="The Customer will churn")
        else:
             return render_template('index.html',prediction_text="The Customer will not churn")
                
if __name__=="__main__":
    app.run(debug=True)
    
    