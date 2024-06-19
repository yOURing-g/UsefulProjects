
'''plement your formula
4, Print output
'''
answer=(input("Enter the first letter of whatever you want to convert (F or C) "))
upperan=answer.upper()
temp=input("Enter a temperature to convert")
if upperan=="F":
    # TMP = input("Enter Fahrenheit temp to convert ")
    floated1=float(temp)

    celsiusFC1 = (floated1-32)*5/9
    print(celsiusFC1)

elif upperan == "C":
    # celsiusCF2 = input("Enter Celsuis temp to convert ")
    floated2=float(temp)

    fahrenCF2 = (floated2*9/5)+32
    print(fahrenCF2)
else:
    print("Rerun the program and try again {error34}")


1,Take input from user
2,Convert input to floating point
3, Im
