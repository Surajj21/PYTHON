#function started  with logic

# def function(name, end): #we have taken name as input variables
#     print("Hello Good morning " + name)
#     print("Hello Suraj")
#     print("Hello Harry")
#     print("Hello Khushboo")
#     print("Hello Khushi")
#     print("Hello Aachal")
#     print("Hello " + name) #concating the input call variable
#     print("Hello "+ end)
#     print(name)
#     print(end)
#
# print("Function printiung started")
#
# function("AASTHA","AJINKYA") #hear set the variables
# function("parmar","somiya") #we can call the same function again and again
#
# print("function is end...")


#Letter formate to send the latter with multiple input values


#def lettergenerator(name, date):
#     str = f"Hello ma'am, \n This is {name} and i am not abele to coma on {date}"
#     print(str)
# name = input(" Enter the name: ") # we can take the input for the prnt
# date = input(" Enter the date and month: ") # we can take the input for the print
# lettergenerator("Suraj", "10th may,2023.")
# lettergenerator(name, date + " 2023.")



#Calculate the average number with the function
def average(a, b):
    return (a+b)/2

a = int(input("ENTER THE FIRST NUMBER: "))
b = int(input("ENTER THE SECOND NUMBER: "))
avg = average(a,b)
print("The avargae of a and b is: " , avg)
print("program ends hear....")