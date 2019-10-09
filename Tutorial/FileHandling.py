#There are 6 type of modes in which we can open
# "r" read mode ; "w" write mode ; "a" append mode ; "rb" ; "wb" ; "ab" read mode for byte
filename = "hello.txt"
file = open(filename, "r")
for line in file:  # To access the lines of the file
   print (line)
   
#The read functions contains different methods, read(),readline() and readlines()
read()		#return one big string
readline()	#return one line at a time
readlines()	#returns a list of lines

#This method writes a sequence of strings to the file.
write ()	#Used to write a fixed sequence of characters to a file
writelines()	#writelines can write a list of strings.

#When you’re done with a file, use close() to close it and free up any system and it automatically calls the flush()
filename.close()
