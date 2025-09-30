file=open("data.txt","w")
file.write("hello world")
file.close()

file=open("data.txt","r")
print("file content:",file.read())
file.close()
          
