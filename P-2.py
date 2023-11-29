c1=input("Enter the 1st primary colour:")

c2=input("Enter the 2nd primary colour:")


if(c1=="red" or c1=="yellow" or c1=="blue"):
    print()
else:
    print("Invalid color 1.")

if(c2=="red" or c2=="yellow" or c2=="blue"):
    print()
else:
    print("Invalid color 2.")

if(c1==c2):
    print("Error: The two colours you entered are the same.")


if(c1=="red" and c2=="blue"):
    print("Result: purple")

elif(c1=="red" and c2=="yellow"):
    print("Result: orange")

elif(c1=="blue" and c2=="red"):
    print("Result: purple")

elif(c1=="blue" and c2=="yellow"):
    print("Result: green")

elif(c1=="yellow" and c2=="red"):
    print("Result: orange")

elif(c1=="yellow" and c2=="blue"):
    print("Result: green")











