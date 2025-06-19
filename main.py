### Integrating HTML With FLASK --Called jinja2 tech
### HTTP verb GET And POST
from flask import Flask,redirect,url_for
### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to My Web Application"

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>The resust is passed</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

# Result checker
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)