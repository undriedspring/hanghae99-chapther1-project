from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

# views
from views.main import main
from views.signup import signup
from views.login import log_in
from views.mypage import my_page


app = Flask(__name__)
# import main
app.register_blueprint(main)
# import signup
app.register_blueprint(signup)
# import login
app.register_blueprint(log_in)
# import mypage
app.register_blueprint(my_page)


SECRET_KEY = 'SPARTA'

client = MongoClient('localhost', 27017)
db = client.hanghae99_chapter1

# modify later
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "../static/profile_pics"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
