#create dictionary

stud1 = {101: "harry", 102: "suraj",103: "alpita", 104: "shiva", 105: "khushi"}
marks = {101:67, 102:99,103:89, 104:89, 105:67}

# print(type(marks))
print(stud1[102]) # data taken from both the dictionary at ones
print(marks[102])

#METHODS

#adding the data into dictionary
stud1[106] = "khushboo"
print(stud1)
stud1[106] = 78
print(stud1)
print(stud1.get(104)) #get method dint show the error

#this keys will show the name assign name of the itesm
print(stud1.keys())

#this .items function will show all the items availabel in the dictionary
print(stud1.items())

