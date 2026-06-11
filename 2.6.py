#Program to Accept Two number and print the following

num1 = int(input("enter first number: "))
num2 = int(input("enter the second number: "))

sum=num1 + num2
print("Addition of the number is: ", sum)

sub=num1 - num2
print("Subtraction of the number is: ",sub)

product=num1 * num2
print("Product of the given number is: ",product)

division=num1 / num2
if(num2==0):
    print("Division not possible")
else:
    print("Quotient is: ",division)

remainder= num1 % num2    
if(num2==0):
    print("Division not possible")
else:
    print("Remainder is: ", division)    



