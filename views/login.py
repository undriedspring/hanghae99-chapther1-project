from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import render_template, jsonify, request, Blueprint
from datetime import datetime, timedelta

SECRET_KEY = 'SPARTA'

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1

log_in = Blueprint('login', __name__)

@log_in.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@log_in.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.forTheCultureUsers.find_one({'userId': username_receive, 'userPw': pw_hash})
    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})