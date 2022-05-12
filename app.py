from flask import Flask, render_template
#import pandas as pd

app = Flask(__name__)

#hangman functions

# def create_dataframe():
#     base_words = ['chien','chat','voiture']
#     base_counts = [0] * len(base_words)
#     df = pd.DataFrame(list(zip(base_words, base_counts)), columns = ['words','counts'])
#     return df

# df = create_dataframe()

def create_db():
    base_words = ['chien','chat','voiture']
    base_counts = [0] * len(base_words)
    db = []
    for word, count in zip(base_words, base_counts):
        db.append({'words':word, 'counts':count})
    return db

db = create_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/db')
def display_db():
    return render_template('db.html', db=db)