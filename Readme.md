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
- **Classical ML models**: Logistic Regression, Random Forest, XGBoost.  
- **Deep Learning models**: LSTM, GRU, Siamese Network.  
- **Transformers**: Fine-tuned BERT for best performance.  

### 🔹 Evaluation  
- Metrics used: Accuracy, Precision, Recall, F1-score, ROC-AUC.  

---

## 🎯 Outcome  
- A trained model that can detect duplicate questions with **high accuracy**.  
- Comparison between **classical NLP approaches** and **modern deep learning methods**.  
- Hands-on experience with **text preprocessing, embeddings, and sequence models**.  

---

## 🚀 Future Work  
- Deploy model as a **web app** (Flask / Django / Streamlit).  
- Improve results with **ensemble techniques**.  
- Use **cross-lingual embeddings** to handle multilingual questions.  

---

## 📌 Tech Stack  
- Python  
- NLTK, SpaCy  
- Scikit-learn  
- Gensim (Word2Vec)  
- TensorFlow / PyTorch  
- HuggingFace Transformers  

---

## 🙌 Acknowledgements  
- [Quora Question Pairs Dataset - Kaggle](https://www.kaggle.com/c/quora-question-pairs)  
- Research papers and tutorials on NLP and duplicate question detection.  

## 🔗 Connect with Me
- 💼 [LinkedIn](https://www.linkedin.com/in/onkarshinde77)  
- ✍️ [Medium Blog](https://medium.com/@onkarshinde77)  
