from flask import redirect,url_for,abort,render_template,Flask,make_response
from flask_bootstrap import Bootstrap
from flask_wtf import  Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

app=Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='xxx'

@app.route('/index1',methods=['GET','POST'])
def index1():
    username=None
    form=NaneForm()
    if form.validate_on_submit():
        username=form.name.data
        form.name.data=''
    return render_template('index.html',username=username,form=form)

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

class NaneForm(Form):
    name=StringField('What is your name?',validators=[Required('输入正确的内容')])
    submit=SubmitField('提交')

if __name__=='__main__':
    app.run(host='0.0.0.0')