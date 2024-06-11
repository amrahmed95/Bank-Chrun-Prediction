import os


import pandas as pd
import numpy as np

from flask import Flask, request, render_template
from src.BankChurn.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homePage():
    return render_template("index.html")

@app.route("/train", methods=['GET'])
def train():
    os.system("python main.py")
    return "Training Successful !"

@app.route("/predict", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            CreditScore = np.int64(request.form['CreditScore'])
            Geography = np.int32(request.form['Geography'])
            Gender = np.int32(request.form['Gender'])
            Age = np.int64(request.form['Age'])
            Tenure = np.int64(request.form['Tenure'])
            Balance = np.int32(request.form['Balance'])
            NumOfProducts = np.int64(request.form['NumOfProducts'])
            IsActiveMember = np.int64(request.form['IsActiveMember'])
            EstimatedSalary = np.int32(request.form['EstimatedSalary'])


            pred_args = [CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, IsActiveMember, EstimatedSalary]
            pred_args = np.array(pred_args).reshape(1, 9)

            pred_pipeline = PredictionPipeline()
            predict = pred_pipeline.predict(pred_args)
            
            if predict == 0:
                msg = "The customer most probably will not leave the bank."
            elif predict == 1:
                msg = "The customer most probably will leave the bank soon."
            else:
                msg = "The prediction is neither 0 nor 1."            
                            
            
            return render_template('results.html', prediction = str(predict), message=msg)
        
        except Exception as e:
            print("The Exception message is: ", e)
            return 'Something is wrong !'
        
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)