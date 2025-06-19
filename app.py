#Building Url Dynamically
### Variable Rules and URL Building
# if pass goto another page if fail goto another page , needs library-"redirect"
##### To creat that url Dynamically use library-"url_for"
from flask import Flask,redirect,url_for
### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to My Web Application"

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

# Result checker
@app.route('/result/<int:score>')
def result(score):
    result=""
    if score<50:
        result='fail'
    else:
        result='pass'
    return 


if __name__=='__main__':
    app.run(debug=True)