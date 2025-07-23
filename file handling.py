'''
open

read/write

close


'''
# s=open('demo.txt',mode='r')
# print(s.read())
# s.close()

# s=open('demo.txt',mode='w')
# s.write("bye")
# s.close()

# s=open('demo.txt',mode='a')
# s.write(" hello welcome to pythonlife")
# s.close()

# "first read next write"
# s=open('demo.txt',mode='r+')
# print(s.read())
# s.write("r+ mode")
# s.close()
#first write next read
s=open('demo.txt',mode='w+')
s.write("w+ mode")
s.seek(0)
print(s.read())
s.close()
