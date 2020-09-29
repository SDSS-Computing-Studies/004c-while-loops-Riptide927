##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""
i= 0
while i < 3:
    i += 1
    user= input("what is your Username ")
    pas = input("what is your password ")
    if user != "admin" or pas != "12345":
        print("Access denied")
    if user == "admin" and pas == "12345":
        print("Access granted")
        break
