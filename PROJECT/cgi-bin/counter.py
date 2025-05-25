import cgi
import cgitb

cgitb.enable() 

form = cgi.FieldStorage()
x = form.getfirst("x", "1")

try:
    x = int(x)
except ValueError:
    x = 1

next_x = x + 1

url = f"/cgi-bin/counter.py?x={next_x}"

# Afișăm HTML-ul
print("Content-Type: text/html\n")
print(f"""<!DOCTYPE HTML>
<html>
<head>
  <meta charset="utf-8">
  <title>Contor</title>
</head>
<body>
  <br><br><br><br>
  <font size="7"><b>
    <p align="center"><a href="{url}">{x}</a></p>
  </b></font>
</body>
</html>""")
