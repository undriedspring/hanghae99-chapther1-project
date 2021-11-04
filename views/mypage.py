from flask import render_template, Blueprint

my_page = Blueprint('mypage', __name__)

# myPage
@my_page.route('/mypage')
def myPage():
    return render_template('mypage.html')