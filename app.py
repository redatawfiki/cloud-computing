from flask import Flask, render_template

app = Flask(__name__)

#db functions

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