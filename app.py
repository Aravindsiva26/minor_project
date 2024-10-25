import numpy as np
import pickle
from flask import Flask, redirect, url_for, request, render_template

# Define a flask app
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

print('Model loaded. Start serving...')
print('Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print("Inside POST")

        # Convert inputs to the appropriate data types
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        Polyuria = int(request.form['Polyuria'])
        Polydipsia = int(request.form['Polydipsia'])
        Weight = int(request.form['Weight'])
        Weakness = int(request.form['Weakness'])
        Polyphagia = int(request.form['Polyphagia'])
        Thrush = int(request.form['Thrush'])
        Blurring = int(request.form['Blurring'])
        Itching = int(request.form['Itching'])
        Irritability = int(request.form['Irritability'])
        Healing = int(request.form['Healing'])
        Paresis = int(request.form['Paresis'])
        Stiffness = int(request.form['Stiffness'])
        Alopecia = int(request.form['Alopecia'])
        Obesity = int(request.form['Obesity'])

        newpat = [[age, gender, Polyuria, Polydipsia, Weight, Weakness,
                   Polyphagia, Thrush, Blurring, Itching, Irritability,
                   Healing, Paresis, Stiffness, Alopecia, Obesity]]
        print(f"Input data: {newpat}")

        result = model.predict(newpat)[0]
        print(f"Prediction result: {result}")

        if result == 1:
            val = "You have Diabetes. Please consult doctor asap!!"
        else:
            val = "Yayyy!! You Don't have Diabetes"

        return render_template('index.html', value=val)
    else:
        return render_template('index.html', value=None)

if __name__ == '__main__':
    app.run(debug=True)
