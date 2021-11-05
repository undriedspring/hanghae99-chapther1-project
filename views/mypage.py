from flask import Blueprint
import jwt
from flask import render_template,request
from pymongo import MongoClient

# mongo settings
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.hanghae99_chapter1

# jwt
SECRET_KEY = 'SPARTA'

# blueprint
my_page = Blueprint('mypage', __name__)

# myPage
@my_page.route('/mypage')
def myPage():
    # 토근 get
    token_reveive = request.cookies.get('mytoken')
    try:
        # 복호화
        payload = jwt.decode(token_reveive, SECRET_KEY, algorithms=['HS256'])
        # user id로 review 가져오기
        all_review =list(db.forTheCultureReviews.find({'userId': payload['id']}, {'_id': False}))
        # 유저가 달았던 리뷰를 토대로 게시물의 제목을 가져오기 위해 list 셋팅
        arr = list()
        for review in all_review:
            content = db.forTheCulture.find_one({'id': int(review['postId'])})
            arr.append(content['title'])

        return render_template('mypage.html', user=payload['id'], reviews=all_review, result=arr)
    except jwt.ExpiredSignatureError:
        return render_template('index.html', msg='false')
    except jwt.exceptions.DecodeError:
        return render_template('index.html', msg='false')

    return render_template('mypage.html')