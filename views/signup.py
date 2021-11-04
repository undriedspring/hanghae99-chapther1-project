from pymongo import MongoClient
import hashlib
from flask import render_template, jsonify, request, Blueprint

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1

signup = Blueprint('signup', __name__)

# singUp
@signup.route('/singUp')
def signUp():
    return render_template('login.html')

@signup.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

@signup.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})
