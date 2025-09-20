# 🔍 Quora Duplicate Question Pairs Detection  

## 📝 Problem Statement  
Quora is a popular platform where people ask and answer questions.  
However, many users often ask the **same question in different ways**.  

For example:  
- *“How can I learn Python programming?”*  
- *“What is the best way to learn Python?”*  

Both mean the same thing, but Quora needs to detect them as **duplicates** to avoid redundancy and improve the user experience.  

👉 The goal of this project is to **build a Machine Learning / Deep Learning model** that can automatically determine whether two questions are duplicates or not.  

---

## 📂 Dataset  
- **Source:** [Kaggle – Quora Question Pairs](https://www.kaggle.com/c/quora-question-pairs)  
- **Details:**  
  - Contains **pairs of questions**.  
  - Each pair is labeled as:  
    - `1 = duplicate`  
    - `0 = not duplicate`.  
---

## ⚙️ Approach  

### 🔹 Data Preprocessing  
- Lowercasing, removing stopwords, punctuation.  
- Tokenization and lemmatization.  

### 🔹 Feature Engineering  
- Word overlap features.  
- Length difference features.  
- TF-IDF, Word2Vec, and GloVe embeddings.  

### 🔹 Modeling  
- **Classical ML models**: Random Forest, XGBoost.  
- **Deep Learning models**: LSTM
- **Transformers**: Fine-tuned BERT for best performance.

### 🔹 Evaluation  
- Metrics used: Accuracy, Precision, Recall, F1-score, ROC-AUC.  

---

## 🎯 Outcome  
- A trained model that can detect duplicate questions with **83% Accuracy**.  
- Comparison between **classical NLP approaches** and **modern deep learning methods**.  
- Hands-on experience with **text preprocessing, embeddings, and sequence models**.  
---

## 🚀 Future Work  
- Deploy model as a **web app** (Flask / Django / ).  
- Improve results with **ensemble techniques**.  
- Use **cross-lingual embeddings** to handle multilingual questions.  

---

## 📌 Tech Stack  
- Python  
- NLTK, SpaCy  
- Scikit-learn  
- bs4
- 	Bag of Words (BoW)
- fuzzywuzzy
- RandomForestClassifier
---

## ⚠️ **Challenges Faced**  

- **Dataset Size**: The Quora dataset contains over **500,000 rows**, which is difficult to train on a normal laptop.  
- **Data Cleaning**
- **To increase accuracy i create more feature from old features (which is 22 features)**
- **Hardware Limitation**: My laptop has only **8GB RAM**, so training large data caused memory issues.  
- **Training Time**: Model training took a long time on limited hardware, reducing the scope for experimentation.  
- **Accuracy Limitation**: Due to hardware constraints, the model could not achieve very high accuracy.  
- **Using Google Colab**:  
  - Colab initially helped, but while adding more features and improving accuracy, memory usage went above **100+ GB**.  
  - Sessions frequently **disconnected**, causing loss of progress.  
  - After disconnections, Colab required a **paid subscription** to access **TPU support** for retraining.  
- **Final Decision**: Due to these issues, I decided to keep and use my **first trained model** in this project.


## 🙌 Acknowledgements  
- [Quora Question Pairs Dataset - Kaggle](https://www.kaggle.com/c/quora-question-pairs)  
- Research papers and tutorials on NLP and duplicate question detection.  

## 🔗 Connect with Me
- 💼 [LinkedIn](https://www.linkedin.com/in/onkarshinde77)  
- ✍️ [Medium Blog](https://medium.com/@onkarshinde77)  


## ⚠️ **Note**  

Training this model requires a **high-performance laptop or computer**, which I currently do not have.  
Because of this limitation, the model may not provide very high accuracy.  

I trained the model on **Google Colab**, but while trying to improve accuracy and create more features, Colab consumed over **100+ GB RAM** and often disconnected.  
When I attempted to reconnect and train again, Colab required a **paid subscription** to access TPU support.  

Therefore, I have included my **initial trained model (82% accuracy)** in this project.

