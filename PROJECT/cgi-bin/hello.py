import cgi

print('''
      <!DOCTYPE html>
      <html>
      <head>
      <title>HEello</title>
        </head>
        <body>
        <h1>exercitiu</h1>
      ''')

form = cgi.FieldStorage()
number1 = form.getfirst('number1', '23')
number2 = form.getfirst('number2', '2010')
number3 = form.getfirst('number3', '14')

print('<h4>')
print("ziua de :" + number1)
print('</h4>')

print('<h4>')
print("anul :" + number2)
print('</h4>')

print('<h4>')
print("varsta de :" + number3)
print('</h4>')


print('''
        </body>
        </html>
        ''')
