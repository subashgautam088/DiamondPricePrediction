
```markdown
# 💎 Diamond Price Prediction

This project predicts the price of diamonds based on various features like carat, cut, color, clarity, depth, and table.  
It involves **EDA, Model Training, and Deployment** using Flask.

---

## 📂 Project Structure

```

DiamondPricePrediction/
│── DiamondPricePrediction.egg-info/   # Package info
│── src/DiamondPricePrediction/        # Source code (modules, pipeline, utils)
│── EDA.ipynb                          # Exploratory Data Analysis
│── Model Training.ipynb               # Model training & evaluation
│── application.py                     # Flask app for deployment
│── gemstone.csv                       # Dataset used for training
│── requirements.txt                   # Required Python libraries
│── setup.py                           # For packaging
│── README.md                          # Project documentation

````

---

## 🚀 Features
- Data preprocessing (handling nulls, categorical encoding, scaling).
- Exploratory Data Analysis (EDA) to understand diamond characteristics.
- Machine Learning model training with hyperparameter tuning.
- Model deployment using **Flask** web application.
- Modular code structure for scalability.

---

## 📊 Dataset
The dataset `gemstone.csv` contains features such as:
- **carat** – weight of the diamond  
- **cut** – quality of the diamond cut  
- **color** – diamond color grading  
- **clarity** – diamond clarity grading  
- **depth** – depth percentage  
- **table** – width of diamond top  
- **price** – target variable  

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DiamondPricePrediction.git
   cd DiamondPricePrediction
````

2. Create virtual environment and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python application.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📌 Requirements

See `requirements.txt` for complete details.

---

## 📈 Results

* Best performing model achieved high R² score with optimized hyperparameters.
* Interactive Flask app allows users to input diamond details and get predicted price.

---

## 🙌 Author

**Arun Gautam**

* 📧 Email: [subashgautam088@gmail.com](mailto:subashgautam088@gmail.com)
* 💼 [LinkedIn](https://www.linkedin.com/in/arun-gautam-20921822b)
* 💻 [GitHub](https://github.com/subashgautam088)

---

```
