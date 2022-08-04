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
		bio = request.form['bio']
		username = request.form['username']
		full_name = request.form['full_name']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			user = {'bio': bio, 'email': email, 'password': password, 'username': username, 'full_name': full_name}
			db.child("user").child(login_session['user']['localId']).set(user)			

			return redirect(url_for('homepage'))
			
		except:
			error = "Authentication failed"
		
	return render_template("signup.html")

@app.route('/home')
def homepage():
	user = db.child("user").child(login_session['user']['localId']).get().val()
	full_name = user["full_name"]

	return render_template("home.html", full_name=full_name)


@app.route('/')
def home2():
	return render_template("index.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		login_session["user"]= auth.sign_in_with_email_and_password(email, password)
		try:
			return redirect(url_for('homepage'))
		except:
			error = "Authentication failed"
			return render_template("signin.html")
	return render_template("signin.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/css')
def css():
	return render_template("Css.html")

@app.route('/idea')
def idea():
	return render_template("idea.html")


@app.route('/why')
def why():
	return render_template("why.html")


#Code goes above here

if __name__ == '__main__':
	app.run(debug=True)