
from flask import Flask, request,  render_template, Response
from werkzeug.utils import secure_filename
from flask_restful import Api 
from flask_sqlalchemy import SQLAlchemy

#################################################################################################

app = Flask(__name__) 
db = SQLAlchemy()

#################################################################################################

class Image(db.Model):
    user_id  = db.Column(db.Integer, primary_key=True)
    image    = db.Column(db.Text, unique=True, nullable=False)
    name     = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

#################################################################################################

# def db_init(app):
#     db.init_app(app)

#     with app.app_context():
#         db.create_all()

#################################################################################################

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db_init(app)

#################################################################################################

@app.route('/')
def home():
    return render_template('home.html')

#################################################################################################


@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')

#################################################################################################


@app.route('/find_work')
def find_work():
    return render_template('find_work.html')

#################################################################################################

@app.route('/learn_design')
def learn_design():
    return render_template('learn_design.html')

#################################################################################################

@app.route('/go_pro')
def go_pro():
    return render_template('go_pro.html')

#################################################################################################

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

#################################################################################################


'''
@app.route('/upload', methods=['POST'])
def upload():
    picture = request.files['pic']
    if not picture:
        return 'No picture detected!', 400

    filename = secure_filename(picture.filename)
    mimetype = picture.mimetype

    # if not filename or not mimetype:
    #     return 'Bad upload!', 400

    image = Image(image=picture.read(), name=filename, mimetype=mimetype)
    db.session.add(image)
    db.session.commit()

    return 'Image upload successful !!!!', 200

#################################################################################################

'''

if __name__ == '__main__':
    app.run(debug=True)