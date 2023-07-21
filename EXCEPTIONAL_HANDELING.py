#TRY EXCEPTIIONAL HANDELING

#Try and except function
#Basically this fun is used to show error what we want to show then not anything that comes with the code

try:
    a = int(input("Enter the number: "))
    print(a + 3)
#We use Exception hear to show that what error is comming
#Without exception this works fine show what we wanted to show
except Exception as e:
    print("some error occures\n ", e)
