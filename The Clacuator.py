from AssignmentOperators import add,subtract,divide,mutipy

A=int(input("Enter the first number"))
operationMalfunctionErrorWhatIsGoingON=input("Enter the operation symbol")
B=int(input("Enter the second number"))


if operationMalfunctionErrorWhatIsGoingON == "+":
    print(add(A,B))
elif operationMalfunctionErrorWhatIsGoingON == "-":
    print(subtract(A,B))
elif operationMalfunctionErrorWhatIsGoingON == "/":
    if B == 0:
        print("Dont Divide Dah Deros   (D.D.D.D)")
    else:
        print(divide(A,B))
elif operationMalfunctionErrorWhatIsGoingON == "*":
    print(mutipy(A,B))
else:
    print("Sorry buddy you did not enter a valid operation symbol"
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          ""
          "Please try again later!!")













