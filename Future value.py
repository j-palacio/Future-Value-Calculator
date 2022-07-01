#Function that takes the accounts present value, monthly interest rate
#and number of months as parameters and returns the future value of the amount
def getFutureValue(p, i , t):
#compute and return the future value
    futureValue = p * ((1 + i))** t
    return futureValue

#prompt and read current account balance
balance = float(input("Enter current bank balance: "))

#prompt and read monthly interest rate
interestRate = float(input("Enter interest rate: "))

#prompt and read number of months
time = int(input("Enter the amount of time that passes: "))

#print the future value by the function getFutureValue
print("The future value is: ${:.2f}".format(getFutureValue(balance,interestRate,time)))
