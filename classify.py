import os
import csv
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
#pip3 install pdfminer.six
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
nltk.download('punkt')
nltk.download('stopwords')
import string
import pandas as pd
import io
from io import StringIO
#import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import pickle


'''
Data extraction and Pre-processing using nltk
'''
def get_processed_text(file_path):
    raw_data = extract_text(file_path)
    raw_data = raw_data.replace("\n", " ")
    data = []
    for i in sent_tokenize(raw_data):
        temp = []
        for j in word_tokenize(i):
            temp.append(j.lower())
        data.append(temp)

    flat_data = [word for sublist in data for word in sublist]

    stopwords_english = stopwords.words('english')
    clean_data = []

    for word in flat_data:
        if (word not in stopwords_english and
            word not in string.punctuation):
            clean_data.append(word)

    stemmer = PorterStemmer()
    stemmed_data = []

    for word in clean_data:
        stem_word = stemmer.stem(word)
        stemmed_data.append(stem_word)

    return " ".join(stemmed_data)

def create_dataset():
    dataset = "dataset.csv"
    fields = ["Label", "Content"]

    with io.open(dataset, "w", encoding = "utf-8") as dataset:
        csv_writer = csv.writer(dataset)
        csv_writer.writerow(fields)
        for root, dirs, files in os.walk("Resumes"):
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    processed_text = get_processed_text(file_path)
                    label = root.split("/")[1]
                    csv_writer.writerow([label, processed_text])

try:
    create_dataset()
except:
    print("Dataset exists.")
else:
    print("Created dataset.")


df = pd.read_csv("dataset.csv")
df['category_id'] = df['Label'].factorize()[0]
category_id_df = df[['Label', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Label']].values)

#Feature Extraction using Term Frequency, Inverse Document Frequency

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.Content).toarray()
labels = df.category_id
X_train, X_test, y_train, y_test = train_test_split(df['Content'], df['Label'], random_state = 0)
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
Model = MultinomialNB().fit(X_train_tfidf, y_train)
#serializing the model
with open("model.pkl", "wb") as file:
    pickle.dump(Model, file)

def predict(file_path_to_test):
    prediction = Model.predict(count_vect.transform([get_processed_text(file_path_to_test)]))
    return prediction

