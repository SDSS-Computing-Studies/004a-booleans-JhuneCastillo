#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

x = input("Enter a username: ")
y = "admin"
a = "12345password"

if (x == y):
    z = input("Enter your password: ")
    if (z == a):
        print("Access granted")
else:
    print("invalid user")

    
