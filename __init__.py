import joblib
import requests
import time
import re
import json
import streamlit as st
from streamlit_lottie import st_lottie
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('vader_lexicon')
import pandas as pd

stop_words = stopwords.words('english')
new_stopwords = ['class', 'take', 'teacher', 'professor', 'students', 'student', 'like', 'test', 'tests']
stop_words.extend(new_stopwords)

w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize(text):
    result = ''
    for w in w_tokenizer.tokenize(text):
        result = result + lemmatizer.lemmatize(w) + ' '
    return result

def predict(comment):
  comment = re.sub(r'[^a-zA-Z\s]', '', comment).lower().split()
  comment = [' '.join([word for word in comment if word not in (stop_words)])]
  comment = list(map(lemmatize, comment))
  comment = loaded_tfidfv.transform(comment)
  result = loaded_model.predict(comment)
  predict_proba = loaded_model.predict_proba(comment)

  if predict_proba[0][0] > predict_proba[0][1]:
    return f'According to this comment, we do not recommend you to take this course with {round(predict_proba[0][0]*100)}% chance.'
  elif predict_proba[0][0] < predict_proba[0][1]:
    return f'According to this comment, we recommend you to take this course with {round(predict_proba[0][1]*100)}% chance.'

def get_features(comment):
  comment = re.sub(r'[^a-zA-Z\s]', '', comment).lower().split()
  comment = [' '.join([word for word in comment if word not in (stop_words)])]
  comment = list(map(lemmatize, comment))
  comment = loaded_tfidfv.transform(comment)

  features = loaded_tfidfv.get_feature_names()

  def sort_matrix(matrix):
    importances = zip(matrix.col, matrix.data)
    return sorted(importances, key=lambda x: (x[1], x[0]), reverse=True)
  
  sorted_features = sort_matrix(comment.tocoo())

  def top_features(features, sorted_features, n):
    sorted_features = sorted_features[:n]

    scores = []
    feature = []

    for idx, score in sorted_features:
      scores.append(round(score, 2))
      feature.append(features[idx])
    
    return pd.Series(feature)
  
  important_words = top_features(features, sorted_features, 10)

  return important_words

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_class = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_bjyiojos.json')

loaded_model = joblib.load('best_model.pkl')
loaded_tfidfv = joblib.load('tfidfv.pkl')

st.set_page_config(page_title="Add or drop!?",
    page_icon="👀",
    layout="centered")

st.title('Add or drop this course?! 💻📚')

st_lottie(lottie_class,
          speed=1,
          loop=False,
          quality='high')

if st.button('Guide'):
    st.success('''
    Please enter the course reviews you want to analyze among the course you wish to take!  \n

    Based on the text entered, we will analyze whether the course review recommends taking it or not.  \n

    We'll also let you know the important words that influenced the analysis result.    \n

    Compare these words to see if there are your course-related interests!
    ''')
with st.form('form'):
    comment = st.text_area('Please enter the course review here.')

    submitted = st.form_submit_button('Submit')

    if submitted:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        result = predict(comment)
        st.write(result)

if submitted:
    st.write('Here are the crucial words that influenced the analysis result!')
    importances = get_features(comment)
    if 'we recommend' in result:
      for word in importances:
        st.success(word)
    elif 'we do not recommend' in result:
      for word in importances:
        st.warning(word)