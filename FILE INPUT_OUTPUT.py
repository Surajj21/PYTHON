#We are taking the variable whatever we want to show in the written file
#using this function we can give a msg to the user just generation one file

msg = "This is the test message which is generated by the python fule(FILE INPUT_OUTPUT)"
msg2 = "This is the second method to write the message with the help of python open fundtion"

#Using with function we can insert our msg into the given name file
# "W" this is mentioned hear for write we have 2 more modes read and apend

# with open("name.txt", "w") as f:
#     f.write(msg)

#second method to do the same thing
# fp = open("name.txt", "w")
# fp.write(msg2)
# fp.close()


#Above code was to writeing a file
#Now we will write a code to read only file

# # method 1
# with open("name.txt", "r") as f:
#     a = f.read()
#     print(a)


#method 2
# fp = open("name.txt", "r")
# a = fp.read()
# print(a)

#Above code was to reading a file
#Now we will write a code to apend the data into file
#
# with open("name.txt", "a") as f:
#     a = f.write("HELLO I AM ERITEING THIS")
#     print(a)
#
