'''
Write a program that stores a password that the user has to guess
'''
passward="password"
val=input("Guess da passward: ")

while val!="password":
    val=(input("Try again: "))

print("you got the password!")