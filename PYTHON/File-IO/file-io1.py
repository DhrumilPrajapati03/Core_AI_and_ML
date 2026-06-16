'''The random-access memory is volatile, and all its contents are lost once a program 
terminates. In order to persist the data forever, we use files. 

A file is data stored in a storage device. A python program can talk to the file by reading 
content from it and writing content to it. '''

#Steps for File Handling in Python: 
# • Opening a file  
# • Reading from a file - r 
# • Writing to a file - w (write mode) and a (append mode)
# • Closing the file 

# Syntax for opening a file:
# open("filename", "mode of opening(read mode by default)") 
# f = open("File-IO\\hello.txt", "r") 
# text = f.readline() 
# print(text)

# text = f.readline()
# print(text)

# text = f.readline()
# print(text)
# f.close()

# f = open("new.txt", "w")
# f.write("Hello, Good evening\n")
# f.close()

# f = open("new.txt", "a")
# f.write("Hello, Good evening\n")
# f.close()

with open('File-IO\\hello.txt', 'r') as f:
    a = f.read()
with open('File-IO\\hello.txt', 'w') as f:
    a = f.write("me")
with open('File-IO\\hello.txt','a') as f:
    a = f.write("Hello !")
print(a)


# 1 Write a program to read the text from a given file ‘poems.txt’ 
# 2 Write a program to write the text “Hello, Good evening” to a file named ‘greeting.txt’
# 3 Write a program to append the text “Have a nice day” to the file ‘greeting.txt’
# 4 use with statement to read the text from a given file ‘poems.txt’ and write it to another file named ‘copy_poems.txt’