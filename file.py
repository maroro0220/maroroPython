
class Big( Exception ):
	pass

class Small( Big ):
	pass
def dosomething():
      raise Big( 'big exception')
def dosomething2():
      raise Small( 'small exception' )
for f in (dosomething, dosomething2 ):
      try:f()

#except Big:
#      print( sys.exc_info() )
#
#f=open('C:\maroroWorkspace\\file.txt','w')
#f.close()
#f=open('C:\maroroWorkspace\\file.txt','w')
#for x in range(1,11):
#                 data='{:>2} 번쨰 줄입니다.\n'.format(x)
#                 f.write(data)
#f.close()



#f=open('C:\maroroWorkspace\\file.txt','r')
#while True:
#                 line=f.readline()
#                 if not line:
#                       break
#                 print(line)
#f.close()

f=open('C:\maroroWorkspace\\file.txt','r')
lines=f.readlines()
for line in lines:
                 print(line)
f.close()

                 
f=open('C:\maroroWorkspace\\file.txt','r')
data=f.read()
print(data)
f.close()

                 
f=open('C:\maroroWorkspace\\file.txt','a')
for x in range(11,20):
                 data='{:>2} 번재 줄입니다.\n'.format(x)
                 f.write(data)
f.close()

f=open('C:\maroroWorkspace\\file.txt','r')
print('파일 현재 위치:',f.tell())
print(f.read())
print('파일 현재 위치:',f.tell())
print()
f.seek(0)#처음으로
print('파일 현재 위치:',f.tell())
print(f.readline(),end='')
print('파일 현재 위치:',f.tell())
f.close()


with open('C:\maroroWorkspace\\foo.txt','w') as f:
      f.write("LIfe is too short, you need python")

data=[1,2,3,4,5]
with open('C:\maroroWorkspace\\test.bin','wb') as f:
      f.write(bytes(data))


with open('C:\maroroWorkspace\\test.bin','rb') as f:
      content=f.read()
      print(type(content))
      for b in content:
            print(b)
            
