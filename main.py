### Integrating HTML With FLASK --Called jinja2 tech
### HTTP verb GET And POST
### use library-"request" to make submit working like give result
##### jinja2 template engine
'''
{%...%} condictions,for loop
{{    }} expressions to print output
{#....#} thi is for comments
'''
from flask import Flask,redirect,url_for,render_template,request
### WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
   return render_template('result.html',result=score) 

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
### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        history=float(request.form['history'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+history+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))






if __name__=='__main__':
    app.run(debug=True)