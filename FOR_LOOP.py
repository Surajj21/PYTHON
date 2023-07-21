#for loop and conditions

#simple for loop to print numbers till 5
print("Printing the simple numbers")
for i in range(10):
    print(i+1)


a = [23,4,5,67,87,98]
b = {4,67,43,56,98}
print("Printing the sets items")

for items in a:
    print(items)

print("Printing the dictionary items")
for items in b:
    print(items)


# write a programe to stop the value to 0 and take the starting point from user

print("Printing the user input")
a = int(input("Enter the number: "))
# a = 10
for i in range(a):

    print(i-(a))





