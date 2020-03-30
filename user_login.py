print ("""***
User Login
***""")

my_username= "oguzbozkurt"
my_password= "09041993"

username=input("Username:")
password=input("Password:")

if (username == my_username and password != my_password):
    print("Wrong password")
elif (username != my_username and password == my_password):
    print("Wrong username")
elif (username != my_username and password != my_password):
    print("Wrong username or password")
else:
    print("Welcome to website")