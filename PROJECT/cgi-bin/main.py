import cgi
import cgitb
import sqlite3
import hashlib

# Enable error reporting
cgitb.enable()

# Set headers
print("Content-Type: text/html; charset=utf-8")
print("X-Content-Type-Options: nosniff")
print("X-Frame-Options: DENY")
print()

def register_user():
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    
    # Ensure table exists
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
    
    form = cgi.FieldStorage()

    if "username" in form and "password" in form and "email" in form:
        username = form.getvalue("username").strip()
        password = form.getvalue("password")
        email = form.getvalue("email").strip()

        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cur.fetchone():
            print("<p style='color:red;'>Error: Username already exists. Please choose a different one.</p>")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            try:
                cur.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                            (username, hashed_password, email))
                con.commit()
                print("<p style='color:green;'>User registered successfully!</p>")
            except sqlite3.IntegrityError:
                print("<p style='color:red;'>Error: Email already exists.</p>")

    con.close()

def show_form():
    print('''
    <html>
    <head>
      <meta charset="utf-8">
      <title>Register</title>
    </head>
    <body>
    <h2>Registration Form</h2>
    <form action="/cgi-bin/main.py" method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" required><br><br>

      <label for="password">Password:</label>
      <input type="password" id="password" name="password" required><br><br>

      <label for="email">Email:</label>
      <input type="email" id="email" name="email" required><br><br>

      <input type="submit" value="Register">
      <br><br>
      <a href="/cgi-bin/login.py">Login</a>
    </form>
    </body>
    </html>
    ''')

# Run
register_user()
show_form()