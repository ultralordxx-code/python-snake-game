def adder(num1,num2):
     answer = num1 + num2
     return (f"the addition of {num1} and{num2} is{answer}")

def substracter(num1, num2):
     answer = num1-num2
     return (f"the substraction between{num1} and{num2} is{answer}")


def multiplier(num1, num2):
     answer = num1*num2
     return (f"the multiplication of{num1} and{num2} is{answer}")


def divider(num1, num2):
     answer = num1/num2
     return (f"the division of{num1} and{num2} is{answer}")


def main():
     print("this is a calculator to perform basic aritmetic between 2 numbers. \n select 1 to add two numbers."
           "\n select 2 to substract two numbers.\n select 3 to multiply two number.\n select 4 to divide two numbers")
     selector=int(input ("what arithmetric do you want to perform ?"))

     if selector==1:
         num1=int(input("what is your first number?"))
         num2=int(input("what is your second number?"))
         final=adder(num1,num2)
         print(final)

     elif selector==2:
         num1=int(input("what is your first number?"))
         num2=int(input("what is your second number?"))
         final=substracter(num1,num2)
         print(final)

     elif selector==3:
         num1=int(input("what is your first number?"))
         num2=int(input("what is your second number?"))
         final=multiplier(num1,num2)
         print(final)
     elif selector==4:
         num1=int(input("what is your first number?"))
         num2=int(input("what is your second number?"))
         final=divider(num1,num2)
         print(final)
    

     else:
         print("the option you selected is not tied to any arithemetric")


main()