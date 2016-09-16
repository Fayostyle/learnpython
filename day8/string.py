from io import StringIO

f= StringIO()
print(f.write('white'))
print(f.write(''))
print(f.write('blue'))
print(f.getvalue())

f1 = StringIO('Hello\nHi\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f2 = BytesIO()
print(f2.write('中文'.encode('utf-8')))
print(f2.getvalue())
