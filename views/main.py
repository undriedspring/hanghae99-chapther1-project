from pymongo import MongoClient
from flask import render_template, jsonify, Blueprint, request, redirect, url_for
import jwt

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1
SECRET_KEY = 'SPARTA'

main = Blueprint('main', __name__)

@main.route('/')
def mainpage():
    return render_template('index.html')

@main.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("main.mainpage", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("main.mainpage", msg="로그인 정보가 존재하지 않습니다."))


# main_list
@main.route('/main_list', methods=['GET'])
def main_list():
    main_list = list(db.forTheCulture.find({}, {'_id': False}))
    return jsonify({'main_list': main_list})
