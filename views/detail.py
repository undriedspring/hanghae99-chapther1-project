import jwt
from flask import render_template,request, Blueprint, jsonify
from pymongo import MongoClient

# mongo settings
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.hanghae99_chapter1

# jwt
SECRET_KEY = 'SPARTA'

detail = Blueprint('details', __name__)

initDefault = None
# details
@detail.route('/details')
def details():

    # query string 값 받아온다.
    request.args.get('id')
    try:
        token_reveive = request.cookies.get('mytoken')
        # id 값을 통해 세부 정보 불러 옴
        result = db.forTheCulture.find_one({'id': int(request.args.get('id'))}, {'_id': False})
        # 세부 정보의 리뷰들을 볼러 옴
        review = db.forTheCultureReviews.find({'postId': request.args.get('id')}, {'_id': False})
        # 댓글을 달 유저의 id값을 위해 복호화
        payload = jwt.decode(token_reveive, SECRET_KEY, algorithms=['HS256'])
        return render_template('details.html', detail=result, user=payload['id'], reviews=review)
    except jwt.ExpiredSignatureError:
        return render_template('details.html', detail=result, user=None, reviews=review)
    except jwt.exceptions.DecodeError:
        return render_template('details.html', detail=result, user=None, reviews=review)

# insert the review
@detail.route('/api/review', methods=['POST'])
def api_review():
    post_id = request.form['post_id']
    user_id = request.form['user_id']
    text = request.form['text_give']
    doc = {
        'postId': post_id,
        'userId': user_id,
        'text': text
    }
    db.forTheCultureReviews.insert_one(doc)
    return jsonify({'payload': 'success'})