from flask import Flask, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
app.secret_key = 'Hash1234'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'user_registration'
db = MySQL(app)

@app.route('/signup', methods = ['GET','POST'])
def signUpPage():
    logs = ""
    if request.method == 'POST':
        userID = request.form['userID']
        phNo = request.form['regPhNo']
        pwd = request.form['regPwd']
        pwdHashed = generate_password_hash(pwd)

        csr = db.connection.cursor()
        csr.execute("SELECT user_id FROM users WHERE user_id = %s", (userID,))
        usertuple = csr.fetchone()

        if usertuple:
            logs = "This user already exists."
        else:
            csr.execute("INSERT INTO users VALUES (%s,%s,%s)", (userID,phNo, pwdHashed,))
            db.connection.commit()
            logs = "Sign up successful. Please log in."
        csr.close()

    return render_template('Sign-Up.html', log = logs)

@app.route('/login', methods = ['GET','POST'])
def logInPage():
    logs = ""
    if request.method == 'POST':
        userID = request.form['loginID']
        pwd = request.form['loginPwd']
        
        csr = db.connection.cursor()
        csr.execute("SELECT password FROM users WHERE user_id = %s",(userID,))
        usertuple = csr.fetchone()
        

        if usertuple:
            correctPwd = check_password_hash(usertuple[0],pwd)
            if correctPwd:
                logs = "Log in successful"
                session['user'] = userID
                return redirect(url_for('homePage'))
            else:
                logs = "Either User ID or Password entered incorrectly."
        else:
            logs = "This user does not exist. Please sign up."
        csr.close()
    return render_template('Log-In.html', log = logs)

@app.route('/')
def homePage():
    loggedIn = False
    userID = ''
    if 'user' in session:
        loggedIn = True
        userID = session['user'].split('@')[0]   
    return render_template('index.html', loggedIn = loggedIn, userID = userID)

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('homePage'))


if __name__ == '__main__':
    app.run(debug=True)
