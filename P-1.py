
m=int(input("Enter the month:"))

if(m>12):
         print("Error: Invalid Input Month")
else:
        print("Success: Congratulations! You entered a correct date.")


d=int(input("Enter the day:"))

if(d>31):
        print("Error: Invalid Input Day.")


y=int(input("Enter the year:"))

if(y>99):
         print("Error: Invalid Input Year.")
else:
        print("Success: Congratulations! You entered a correct date.")        



if(m==2):
        if(y%4==0 and d>29):
                print("Error: There is no such date in the calendar.")
        elif(y%4!=0 and d>28):
                print("Error: There is no such date in the calendar.")

        else:
                print("Success: Congratulations! You entered a correct date.")


        


    





