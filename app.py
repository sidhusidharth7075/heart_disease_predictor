from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# ✅ Updated model path to use XGBoost model
MODEL_PATH = os.path.join('model', 'xgb_model.pkl')

# Load the trained model
try:
    model = pickle.load(open(MODEL_PATH, 'rb'))
except FileNotFoundError:
    model = None
    print(f"❌ Error: Model file not found at {MODEL_PATH}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if model is None:
            return "Model not loaded. Please check your model file."

        try:
            fields = [
                'age', 'sex', 'cp', 'bp', 'cholesterol',
                'fbs', 'ekg', 'maxhr', 'exangina',
                'st_depression', 'slope', 'vessels', 'thallium'
            ]
            features = [float(request.form[field]) for field in fields]

            input_array = np.array([features])
            prediction = model.predict(input_array)[0]

            if prediction == 1:
                result = "✅ Presence of Heart Disease"
                suggestion = (
                    "⚠️ Please consult a cardiologist immediately. "
                    "Maintain a heart-healthy lifestyle: eat low-fat food, avoid smoking, "
                    "engage in moderate physical activity, and monitor blood pressure regularly."
                )
            else:
                result = "🟢 No Heart Disease Detected"
                suggestion = (
                    "🎉 Great job! Keep following a healthy lifestyle. "
                    "Continue regular exercise, eat a balanced diet, and go for periodic checkups."
                )

            return render_template('result.html', result=result, suggestion=suggestion)

        except Exception as e:
            return render_template('result.html', result=f"⚠️ Error: {str(e)}", suggestion="")

    return render_template('predict.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)

