# IMPORTING LIABRARIES
# THIS CODE IS MADE BY SHOURYA PANT AND TEJAS DWIVEDI

import math
from tqdm import tqdm
import time
  
#Thsi function is designed for the INTRODUCTION TO OUR CALCULATOR PROGRAM

def Welcome():
    print("\n\n---------------------------------------------------------",end="")
    print("\n|\n|  Welcome to the scientific Calculator app .....  \t|", end="\n")
    print("|\n| MADE BY:  ", " SHOURYA PANT(0105CS191109) \t\t|", end="\n")
    print("|\n| \t       AND  \t\t\t \t\t|")
    print("|\n| \t     TEJAS DWIVEDI(0105CS191123) \t\t|",end="\n\n")
    for i in tqdm (range (100), desc="Loading..."):
        time.sleep(0.02)
        pass
    print("----------------------------------------------------------")

# This function is designed for performing the ADDITION OF n numbers

def Addition():
    print("how many nums to add")
    number=int(input())
    sum=0
    for x in range(number):
        numbers_to_be_added=list(map(int,input("Enter Number "+ str(x+1) + " ").split()))
        for y in numbers_to_be_added:
            sum+=y
    print("\n \n THE SUM OF ALL NUMBERS IS : ", sum, end="\n")  

# This function is designed for performing the SUBTRACTION of n numbers

def Subtraction():
    print("\n For How many variables You want to do subtraction?",end="\n")
    No_of_variable=int(input("\n Enter the Total number of Operands... "))
    if No_of_variable==1:
        print("\n Invalid Operation or please Give atleast two operands to perform Subtraction", end="\n")
    elif No_of_variable==2:
        Num1=int(input("Enter First Number  "))
        Num2=int(input("Enter Second Number  "))
        difference=Num1-Num2
        print("\n\n THE DIFFERENCE BETWEEN TWO NUMBERS ", Num1 , "and", Num2 ,"is :",difference, end="\n")
    elif No_of_variable==3:
        Num1=int(input("Enter First Number  "))
        Num2=int(input("Enter Second Number  "))
        Num3=int(input("Enter Third Number  "))
        difference=Num1-Num2-Num3
        print("\n\n THE DIFFERENCE BETWEEN THREE NUMBERS  ", Num1 , "and", Num2 , "and", Num3, "is :",difference, end="\n")
    elif No_of_variable>=4:
        numbers=[]
        for x  in range(No_of_variable):
            for i in (input("Enter Numbers "+ str(x+1)+ " ").split()):
                numbers.append(i)
            difference=int(numbers[0])
            for number in numbers[1:]:
                difference=difference-int(number)
        print(" \n \n THE DIFFERENCE BETWEEN ALL THE NUMBERS ", difference, end="\n\n")

# This function is designed to perform MULTIPLICATION of two or more numbers

def Multiplication():
    print("\n How many numbers do you want to get MULTIPLY ???", end="\n")
    choice=int(input("\n Enter Total number of Multiplicands :"))
    if choice==1:
        print("\n ERROR MULTIPLICATION of one number is not possible ", end="\n")
        print("\n Do You wish to MULTIPLY  THAT NUMBER with ITSELF :", end="\n")
        option=str(input("Yes or NO , enter (Y,N) "))
        if option=='y' or option=="Y":
            Number=float(input(" \n Enter the number which you want to multiply with ITSELF ", end="\n"))
            result=Number**2
            print("\n \n THE MULTIPLICATION RESULT OF THAT NUMBER ", Number , " WITH ITSELF IS : ", result, end="\n\n")
    elif choice==2:
        Number1=float(input("\n Enter first number "))
        Number2=float(input("\n Enter second number "))
        result=Number1*Number2
        print("\n \n THE MULTIPLICATION OF NUMBER ", Number1, "and ", Number2, "is : ", result, end="\n\n")
    elif choice>=3:
        numbers=[]
        for x  in range(choice):
            for i in (input("Enter Numbers "+ str(x+1)+ " ").split()):
                numbers.append(i)
            result=1
            for x in numbers:
                result=result*float(x)
        print("\n \n THE MULTIPLICATION OF NUMBERS IS : ",result, end="\n\n")

#This function is designed to perform DIVISION of two numbers

def Division():
    print("\n 1. Do the division for the integers numbers ",end="\n")
    print("\n 2. Do the division for the floating point numbers ",end="\n")
    choice=int(input("\n Enter 1 or 2 "))
    if choice==1:
        Num1=int(input("\n Enter the first number (Dividend): "))
        Num2=int(input("\n Enter the Second NUmber (Divisor) "))
        if Num2==0:
            print("\n ERROR!!!",END="\n")
            print("\n\n The Division of a Number by 0 is not possible",end="\n")
        else:
            Division=Num1/Num2
            print("\n\n THE DIVISION OF TWO NUMBERS ",Num1 , " and", Num2, "is : ", Division, end="\n\n")
    elif choice==2:
        Num1=float(input("Enter the first number (Dividend): "))
        Num2=float(input("Enter the Second NUmber (Divisor) "))
        if Num2==0:
            print("\n ERROR!!!",end="\n")
            print("\n\n The Division of a Number by 0 is not possible",end="\n\n")
        else:
            Division=Num1/Num2
            print("\n \n THE DIVISION BETWEEN TWO NUMBERS ",Num1 , " and", Num2, "is : ", Division, end="\n\n")
    else:
        print("\n ERROR!!!! ..... \n",end="\n")
        print("INVALID CHOICE PLEASE CHOOSE BETWEEN 1 OR 2", end="\n\n")

# This funciton is designed for CALCULATING THE MODULUS OF the numbers

def Modulus():
    x=float(input("\n Enter  First number : "))
    y=float(input("\n Enter divisor : "))
    modulus=x%y
    print("\n\n THE MODULUS BETWEEN TWO NUMBERS ",x ,"and", y , "is :{:.2f}".format(modulus))

# This function is designed for CALCULATING THE POWERS taking BASE AND  EXPONENTIAL  values from the user

def Powers_Exponents():
    Base=float(input("\n Enter the Base NUmber whose powers you have to calculate : "))
    exponent=float(input("\n Enter the exponent Number which will be given as power to base  : "))
    power=Base**exponent
    print("\n\n THE VALUE OF THE NUMBER ", Base, "TO THE POWER OF ",exponent,"is : ", power ,end="\n\n")

# This function is designed to CALCULATE THE ROOTS OF A NUMBER OR 1/NTH POWER OF A NUMBER

def Calculating_Roots():
    Number=float(input("\n Enter the number whose root you want to find : "))
    exponent=float(input("\n Which Root You want ? "))
    result=pow(Number,1/exponent)
    if exponent==2:
        print("\n THE SQUARE ROOT OF ", Number, "is : ", result, end="\n")
    elif exponent==3:
        print("\n THE CUBE ROOT OF ", Number, "is : ", result, end="\n")
    else:
        print("\n THE NTH ROOT OF ", Number, "is : ", result, end="\n")

# This function is designed to calculate the FACTORIAL OF A NUMBER

def Factorial():
    factorial=1
    Number=float(input("\n Enter a Number whose factorial You want to be Calculated : "))
    if (Number>=1) and Number.is_integer()==True:
        for fact in range(1, int(Number+1)):
            factorial=factorial*fact
        print("\n\n THE FACTORIAL OF THE GIVEN NUMBER  ", Number,"is : ", factorial, end="\n\n")
    else:
        print("\n")
        for i in tqdm (range (100), desc=" ERROR !!!!..."):
            time.sleep(0.01)
            pass
        print("\n The FACTORIAL cannot be calculated for NEGATIVE NUMBERS and DECIMAL NUMBERS !!!!!!!!!", end="\n\n")

# This function is designed to calculate the TRIGNOMETRY

def Trignometry():
    print("\n WHICH TRIGNOMETRIC FUNCTION DO YOU WANT TO USE \n\n 1. SIN \n 2. COS \n 3. TAN \n 4. SEC \n 5. COSEC \n 6. COT ", end="\n")
    choice=float(input("\n Enter Choice (1-6)"))
    x=float(input("\n Enter the values in degrees "))
    x=(x/180)*3.14159265359
    if (choice==1):
        print(math.sin(x), end="\n")
    elif(choice==2):
        print(math.cos(x), end="\n")
    elif(choice==3):
        print(math.tan(x), end="\n")
    elif(choice==4):
        print(1/math.cos(x), end="\n")
    elif(choice==5):
        print(1/math.sin(x), end="\n")
    elif(choice==6):
        print(1/math.tan(x), end="\n")
    else:
        print("\n\n INVALID CHOICE !!!! \n \n Please Enter a VALID CHOICE(1-6)",end="\n ")
    return(0)

# This function  is designed for calculating the LOGARITHMIC VALUES

def logarithms():
    print("\n Which type of logarithms do you want to calculate ?", end="\n")
    print("\n 1.  NATURAL LOGS , (Base=e or ln)", end="\n")
    print("\n 2. LOGS WITH A BASE AND VALUE", end="\n")
    choice=int(input("\n Enter 1 or 2 "))
    if choice==1:
        Base=float(input("\n Enter a Base Number whose log you want to calculate "))
        print("\n\n THE NATURAL LOG OF THE NUMBER ", Base ," is : ", math.log(Base))
    elif choice==2:
        Base=float(input("\n Enter a Base Number whose log you want to calculate "))
        Exponent=float(input("\n Enter a exponent number which will the log base "))
        print("\n \n THE LOG OF ", Base ," WITH LOG BASE ", Exponent ,"is : ", math.log(Base, Exponent), end="\n\n")
    else:
        print("\n Print INVALID CHOICE!!!! \n\n")
        print("Enter a choice between 1 or 2 ")

# This function  is designed for calculating the EUCLEDIAN DISTANCE BETWEEN TWO POINTS

def Eucledian_distance():
    x1=float(input("\n Enter the x coordinate of the first point (x1) "))
    x2=float(input("\n Enter the x coordinate of the second point (x2) "))
    y1=float(input("\n Enter the y coordinate of the first point (y1) "))
    y2=float(input("\n Enter the y coordinate of the second point (y2) "))
    Eucledian_distance=((x2-x1)**2 + (y2-y1)**2)**0.5
    print("\n \n THE EUCLEDIAN DISTANCE BETWEEN TWO POINTS ","(",x1,",",y1,")","and","(",x2,",",y2,")","is : ", Eucledian_distance, end="\n\n")

# This function is designed to CALCULATE AREA OF DIFFERENT POLYGONS 

def Area():
    print("\n Which Figure Area do you want to calculate ? \n\n 1. RECTANGLE \n 2. SQUARE \n 3. TRIANGLE \n 4. CIRCLE \n 5. REGULAR POLYGON  ", end="\n")
    choice=int(input("\n Enter a Choice (1-5)"))
    if choice ==1:
        length=float(input("\n Enter The Length of Rectangle : "))
        breadth=float(input("\n Enter The Breadth of Rectangle : "))
        print("\n\n THE AREA OF RECTANGLE IS : ", length*breadth, end="\n")
    elif choice==2:
        side=float(input("\n Enter The Side of Square : "))
        print("\n\n THE AREA OF SQUARE IS : ", side*side, end="\n")
    elif choice==3:
        height=float(input("\n Enter The height of Triangle : "))
        breadth=float(input("\n Enter The Breadth of Triangle : "))
        print("\n\n THE AREA OF TRIANGLE IS : ", 0.5*breadth*height, end="\n")
    elif choice==4:
        Radius=float(input("\n Enter The Radius of Circle : "))
        print("\n\n THE AREA OF CIRCLE IS : {:.4f}".format( math.pi*Radius*Radius), end="\n")
    elif choice==5:
        no_of_sides=int(input("\n Enter no. of sides  of the REGULAR POLYGON : "))
        length=float(input("\n Enter Length of side :"))
        ans=length*length*no_of_sides/4*math.tan(3.14159265359/no_of_sides)
        print("{:.4f}".format(ans))
    else:
        print("\n \n  INVALID CHOICE !!! PLEASE ENTER A VALID CHOICE(1-5) ",end="\n")

#  THE MAIN MENU 

def Calculator():

    Welcome()
    print("\n What do you want to do with our calculator ?", end="\n")
    print("\n MAIN MENU : ", end="\n\n")
    print("\n 1. ADDING NUMBERS TWO OR MORE ", end="\n")
    print("\n 2. SUBTRACTING NUMBERS TWO OR MORE ", end="\n")
    print("\n 3. MULTIPLYING NUMBERS TWO OR MORE ", end="\n")
    print("\n 4. DIVIDING NUMBERS  ", end="\n")
    print("\n 5. TAKING MODULUS(REMAINDER ) OF NUMBERS ", end="\n")
    print("\n 6. CALCULATING THE POWERS OR EXPONENTS  ", end="\n")
    print("\n 7. CALCULATING THE ROOTS OR 1/nth POWERS OF A NUMBER ", end="\n")
    print("\n 8. CALCULATING THE FACTORIAL ", end="\n")
    print("\n 9. TRIGNOMETRY ", end="\n")
    print("\n 10. CALCULATING THE LOGARITHMICS AND NATURAL LOGS ", end="\n")
    print("\n 11. CALCULATING THE EUCLEDIAN DISTANCE BETWEEN TWO POINTS  ", end="\n")
    print("\n 12. CALCULATING THE AREA OF VARIOUS SHAPES AND POLYGONS ", end="\n")
    print("\n\n PLEASE ENTER A VALID CHOICE (1-12) ", end="\n\n")
    choice=int(input("Please Enter a Choice(1-12) what you want to do ??"))

    if choice==1:
        Addition()
    elif choice==2:
        Subtraction()
    elif choice==3:
        Multiplication()
    elif choice==4:
        Division()
    elif choice==5:
        Modulus()
    elif choice==6:
        Powers_Exponents()
    elif choice==7:
        Calculating_Roots()
    elif choice==8:
        Factorial()
    elif choice==9:
        Trignometry()
    elif choice==10:
        logarithms()
    elif choice==11:
        Eucledian_distance()
    elif choice==12:
        Area()
    else:
        print("\n\n INVALID CHOICE !!!!!! ", end="\n")
        print("\n \n PLEASE ENTER A VALID CHOICE (1-12) ", end="\n\n")

# THE MAIN FUNCITON

if __name__=="__main__":

    print("\n\n HELLO EVERYONE WELCOME TO OUR CALCULATOR PROGRAM .........", end="\n")
    print("\n")
    for i in tqdm (range (100), desc=" INITIALIZING..."):
        time.sleep(0.01)
        pass
    Calculator()

    while True:
        Yes_no=input("\n Do You want to continue (Yes or No) ?")
        if Yes_no=="Y" or Yes_no=='y' or Yes_no=='Yes' or  Yes_no=='yes':
            Calculator()
        else:
            break