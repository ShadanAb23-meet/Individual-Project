from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

Config = {

  "apiKey": "AIzaSyCBrXxv0Ue5Be95LTYxMDCkcIbUZ-TLIDU",

  "authDomain": "workingonit-b95cf.firebaseapp.com",

  "projectId": "workingonit-b95cf",

  "storageBucket": "workingonit-b95cf.appspot.com",

  "messagingSenderId": "357714558121",

  "appId": "1:357714558121:web:cc434de957738451523db8",

  "measurementI": "G-PT1ZX2VJFS",

  "databaseURL": "https://workingonit-b95cf-default-rtdb.europe-west1.firebasedatabase.app/",

}

firebase=pyrebase.initialize_app(Config)
auth=firebase.auth()
db=firebase.database()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			return redirect(url_for('index.html'))
		except:
			error = "Authentication failed"
	return render_template("signup.html")

@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session["user"]= auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('signin'))
		except:
			error = "Authentication failed"
			return render_template("signin.html")
	return render_template("signin.html")

@app.route('/about_us')
def about_us():
	return render_template("about_us.html")




#Code goes above here

if __name__ == '__main__':
	app.run(debug=True)