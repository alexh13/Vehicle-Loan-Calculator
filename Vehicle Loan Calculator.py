print("Welcome to my vehicle loan calculator")


def vehicleLoanCalc():
        carCost = float(input("What is the cost of the car by itself:"))
        carTax = float(input("What is the sales tax rate? \n"
                             "ex: 7% = 7, 10.5% = 10.5:"))
        carTax2 = carTax / 100
        dealerFee = float(input("Are there any dealership fees? \n"
                                "If none enter a zero:"))
        carFees = float(input("What are the title and license fees:"))
        downPayment = float(input("Do you have a down payment? \n"
                                  "If none enter a zero:"))
        rebates = float(input("Are there any incentives or rebates for this vehicle? \n"
                              "Enter amount:"))
        getSalesTax = carCost * carTax2
        carTotalPrice = carCost + getSalesTax + dealerFee + carFees - downPayment - rebates
        print("The vehicles total price before financing is:", carTotalPrice)
        lengthMonths = int(input("How long is the loan in months:"))
        intRate = float(input("What is the annual interest rate:"))
        carInt = intRate / 100 / 12
        monthlyPayment = carTotalPrice * (1 + carInt) ** lengthMonths * carInt / ((1 + carInt) ** lengthMonths - 1)
        print("Your monthly payment is: $" + ('%0.2f' % monthlyPayment), "for", lengthMonths, "months")
        # outputs vehicle monthly payment formatted 2 decimal and number of months financed

vehicleLoanCalc()

