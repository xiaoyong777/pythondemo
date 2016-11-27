from flask import redirect,url_for,abort,render_template,Flask,make_response,session

from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import  FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
manager = Manager(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:123456@localhost:3306/test'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db=SQLAlchemy(app)

bootstrap=Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

@app.route('/index',methods=['GET','POST'])
def index1():
    username=None
    form=NaneForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

@app.route('/index2')
def index2():
    response=make_response("<h1>hello wordl</h1>")
    return response

@app.route('/index3')
def index3():
  return redirect(url_for('index1'))

@app.route("/index4")
def index4():
    return abort(404)

# @app.errorhandler(404)
# def page_not_fount(e):
#     return render_template('404.html'),404

class NaneForm(FlaskForm):
    name=StringField('What is your name?',validators=[Required('输入正确的内容')])
    submit=SubmitField('提交')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' %self.name

    users=db.relationship('User',backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' %self.username

if __name__=='__main__':
   # manager.run()
    app.run()