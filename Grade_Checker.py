'''
Write a program that calculates a student's
grade based on their score. The program should prompt the user to enter
a score and then display the corresponding grade (e.g., A, B, C, D, or F).

90-100=A
80-89=B
70-79=C
60-69=D
59 and below = F
'''

# grade =int(input("Enter the score of your paper "))
# if grade>=90 and grade<= 100:
#     print("Congratulations, You have achieved an A")
# elif grade>=80 and grade<=89:
#     print("Good Job you achieved a B")
# elif grade>=70 and grade<=79:
#     print("Good effort you earned a C for trying")
# elif grade>=60 and grade<=69:
#     print("Good motives you have  a D for working hard")
# elif grade>=0 and grade<= 59:
#     print("Try harder, You can do better than an F")
# else:
#     print("Hey buddy that is not a real grade, No grade would be 'that'")
'''
Build a basic calculator program that can perform 
addition, subtraction, multiplication, and division. 
Prompt the user for two numbers and the desired operation, 
and then display the result.

Get Number1 buy input
Get Number2 buy input
Get operation
operate
'''

num1=int(input("What is the first number would you like to operate? "))
operation=(input("What operation would you like to use? (Use a operator)"))
num2=int(input("What is the second number would you like to operate? "))
if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
   if num2 == 0:
        print("Cannot divide 0 by buddy")
   else:
        print (num1 / num2)
