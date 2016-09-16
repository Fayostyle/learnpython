with open('./hello.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('./s.png', 'rb') as f1:
    print(f1.read())

with open('./gbk.txt', 'r', encoding='gbk') as f2:
    print(f2.read())

with open('./hello.txt', 'w') as f3:
    f3.write('hello,again')