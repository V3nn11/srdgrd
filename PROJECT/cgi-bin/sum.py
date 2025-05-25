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

forms = cgi.FieldStorage()
num1 = forms.getfirst('num1', '1')
num2 = forms.getfirst('num2', '2')

print('<h1>')
print('First number is: ' + num1)
print('</h1>')

print('<h1>')
print('second number is: ' +  num2)
print('</h1>')

print('<h1>')
print('The sum of the numbers is: ', int(num1) + int(num2))
print('</h1>')

print('''
        </body>
        </html>
        ''')