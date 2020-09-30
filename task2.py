#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
i= 1
while i == 1:
    user= input("what is your Username ").strip()
    pas = input("what is your password ").strip()
    if user != "admin" or pas != "12345":
        print("Access denied")
    if user == "admin" and pas == "12345":
        print("Access granted")
        i = 2
