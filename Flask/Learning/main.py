# Integrate HTML with flask
# HTTP verb GET and POST


from flask import Flask, redirect, url_for, render_template

#WSGI Application
app = Flask(__name__)

@app.route('/')         #decorator with url - the function beneath it will run automatically
def welcome():
    #return 'Welcome to my youtube channel'
    return render_template('index.html')  #we are rendering a message from an HTML file, t do this we have to have a seperate folder structure (look at the folders)

@app.route('/success/<int:score>')         #decorator with url - the function beneath it will run automatically
def success(score):
    return 'The person has passed and the marks are ' + str(score)
    #return'<html><body><h1>The Result is passed</h1></body></html>'

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

# Result checker HTML page
##@app.route('/submit', methods = ['POST', 'GET'])
#def submit():
    



if __name__=='__main__':
    app.run(debug=True)