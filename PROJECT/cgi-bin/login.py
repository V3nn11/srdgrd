import cgi
import cgitb
import sqlite3
import hashlib

# Enable error reporting for debugging
cgitb.enable()

# Set HTTP headers
print("Content-Type: text/html; charset=utf-8")
print("X-Content-Type-Options: nosniff")
print("X-Frame-Options: DENY")
print()

# Function to authenticate user
def authenticate_user():
    form = cgi.FieldStorage()

    if "username" in form and "password" in form:
        username = form.getvalue("username").strip()
        password = form.getvalue("password")

        # Hash the entered password with SHA-256
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

        # Connect to the database
        con = sqlite3.connect('main.db')
        cur = con.cursor()

        # Query for user info
        cur.execute("SELECT password, email FROM users WHERE username = ?", (username,))
        result = cur.fetchone()
        con.close()

        # If user found
        if result:
            stored_password, email = result
            if hashed_input_password == stored_password:
                print(f"<p style='color:green;'>Login successful! Welcome, <strong>{username}</strong>.</p>")
                print(f"<p>Your email is: {email}</p>")
            else:
                print("<p style='color:red;'>Incorrect password. Please try again.</p>")
        else:
            print("<p style='color:red;'>Username not found. Please <a href='/cgi-bin/main.py'>register</a>.</p>")

# Function to show login form
def show_login_form():
    print('''
    <html>
    <head>
      <meta charset="utf-8">
      <title>Login</title>
    </head>
    <body>
    <h2>Login</h2>
    <form action="/cgi-bin/login.py" method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required><br><br>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required><br><br>

      <input type="submit" value="Login">
      <br><br>
      <a href="/cgi-bin/main.py">Register</a>
    </form>
    </body>
    </html>
    ''')

# Run the authentication and form display
authenticate_user()
show_login_form()