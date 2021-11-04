from flask import Blueprint
import jwt
from flask import render_template,request
from pymongo import MongoClient

# mongo settings
client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1

# jwt
SECRET_KEY = 'SPARTA'

# blueprint
my_page = Blueprint('mypage', __name__)

# myPage
@my_page.route('/mypage')
def myPage():
    token_reveive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_reveive, SECRET_KEY, algorithms=['HS256'])
        theUser = db.forTheCultureUsers.find_one({'userId': payload['id']}, {'_id': False})
        all_review =db.forTheCultureReviews.find({'userId': payload['id']})
        return render_template('mypage.html', user=theUser, reviews=all_review)
    except jwt.ExpiredSignatureError:
        return render_template('index.html', msg='false')
    except jwt.exceptions.DecodeError:
        return render_template('index.html', msg='false')

    return render_template('mypage.html')