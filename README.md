# 🫀 Heart Disease Predictor — Flask + XGBoost Web Application
This is a web-based application developed using Flask and Machine Learning (XGBoost) that allows users to predict the likelihood of heart disease based on key patient medical parameters. The goal is to assist healthcare professionals and individuals in assessing cardiovascular risk quickly and efficiently through a user-friendly interface.

# 🧠 How It Works
The application leverages a trained XGBoost model that analyzes medical input data — such as age, sex, cholesterol levels, blood pressure, fasting blood sugar, chest pain type, and more — to predict whether a person is likely to have heart disease.

## 🧠 Model Info

- Model: XGBoostClassifier
- Accuracy: ~81.5% on test data

---

## Project Structure

```bash

heart_disease_predictor/
│
├── app.py
│   - The main Flask application file that runs the server and handles routing, user input, and model prediction logic.
│
├── model/
│   ├── model.pkl
│   └── xgb_model.pkl
│   - Pre-trained machine learning models used for prediction (e.g., XGBoost).
│
├── dataset/
│   └── Heart_Disease_Prediction.csv
│   - The dataset used for training and evaluating the models.
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── predict.html
│   ├── result.html
│   ├── about.html
│   └── data.html
│   - Jinja2 HTML templates used to render different pages in the web app.
│   - `base.html` is the base layout template extended by others.
│   - `predict.html` contains the form for user inputs.
│   - `result.html` displays prediction results.
│   - `about.html` gives project information.
│   - `data.html` may show raw dataset or statistics.
│
├── static/
│   └── css/
│       └── style.css
│   - Static files (CSS) for styling the web app.
│
├── requirements.txt
│   - Contains the list of Python dependencies required to run the project.
│
└── README.md
    - Project overview, setup instructions, and usage guide.


```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/heart_disease_predictor.git
cd heart_disease_predictor
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
python app.py
```

### 5. Access the Website

- not published yet.

## 📧 Contact

For inquiries or collaboration opportunities, reach out via:

- Email: [sidhusidharth7075@gmail.com](mailto:sidhusidharth7075@gmail.com)
- LinkedIn: [LohithSappa](https://www.linkedin.com/in/lohith-sappa-aab07629a/)

---

# ⭐ Don't forget to **star** this repository if you found it helpful!
