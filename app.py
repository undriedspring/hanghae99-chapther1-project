from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1


# index .main
@app.route('/')
def index():
    return render_template('index.html')


# main_list
@app.route('/main_list',methods=['GET'])
def main_list():
    main_list = list(db.forTheCulture.find({}, {'_id': False}))
    return jsonify({'main_list': main_list})


# login
@app.route('/login')
def login():
    return render_template('login.html')


# singUp
@app.route('/singUp')
def singUp():
    return render_template('singUp.html')


# myPage
@app.route('/mypage')
def myPage():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
