from pymongo import MongoClient
from flask import Flask
# views
from views.main import main
from views.signup import signup
from views.login import log_in
from views.mypage import my_page
from views.detail import detail
app = Flask(__name__)
# import main
app.register_blueprint(main)
# import signup
app.register_blueprint(signup)
# import login
app.register_blueprint(log_in)
# import mypage
app.register_blueprint(my_page)
# import detail
app.register_blueprint(detail)

# modify later
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "../static/profile_pics"

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
