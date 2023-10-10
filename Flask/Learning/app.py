from flask import Flask, redirect, url_for

#WSGI Application
app = Flask(__name__)

@app.route('/')         #decorator with url - the function beneath it will run automatically
def welcome():
    return '<html><body><h1>The Result is passed</h1></body></html>'

@app.route('/success/<int:score>')         #decorator with url - the function beneath it will run automatically
def success(score):
    return 'The person has passed and the marks are ' + str(score)

@app.route('/fail/<int:score>')         #decorator with url - the function beneath it will run automatically
def fail(score):
    return 'The person has failed and the marks are ' + str(score)

#result checker
@app.route('/results/<int:marks>')         
def results(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
        
    return redirect(url_for(result, score = marks))   #used to redirect to a different url



if __name__=='__main__':
    app.run(debug=True)