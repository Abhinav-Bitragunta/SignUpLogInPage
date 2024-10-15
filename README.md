# SignUpLogInPage
Log in and Sign Up page made using HTML5, CSS, and Python(Flask).

MySQL was used for the Database, with the following definition:
------------------------------------
```sql
CREATE DATABASE user_registration;
USE user_registration;

CREATE TABLE users (
    user_id VARCHAR(255) primary key,
    mobile_number bigint NOT NULL,
    password VARCHAR(255) NOT NULL
);
```
To run this on your own PC:
----------------------------------
1. Replace lines 9 and 10 of app.py with these:
       app.config['MYSQL_USER'] = 'your_mysql_user'
       app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
2. Run this:
       pip install --upgrade Flask Flask-MySQLdb Werkzeug
3. Make sure that the database and table shown above have been created
4. Run app.py and go to http://127.0.0.1:5000 on your browser.



