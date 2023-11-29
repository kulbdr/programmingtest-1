def countrymigrate():
ger=int(input("Please enter your salary in Germany in euros:"))
mig=input("Enter the country you want to migrate to:")
if (mig=="canada" or "usa" or "cambodia" or "uk"):
    print()
else:
    print("Invalid Country.")

countrymigrate()

def convertSalary():
    
canada= 37535.40
usa= 41007.60
cambodia= 1691.78
uk= 52542.37

if ger>canada:
    print("You will be poor in Canada with this salary.")

if ger>usa:
    print("You will be poor in USA with this salary.")

if ger>cambodia:
    print("You will be poor in Cambodia with this salary.")

if ger>uk:
    print("You will be poor in UK with this salary.")


convertSalary()

















    