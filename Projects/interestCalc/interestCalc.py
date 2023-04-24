print("Welcome to Interest Calculator!")
print("Note: You must have all values of P, R, T (amount is not necessary!)")
choice = input("What do you want to calculate? (SI/CI): ")
if choice == "SI" or choice == "si":
    print("Welcome to SI calculator")
    print("Enter the asked values, type 0 if value is not given!")
    siPrinciple = int(input("What is the principle amount? "))
    siRate = int(input("What is the Rate of Interest? "))
    siTime = int(input("What is the Time Period? "))
    si = (siPrinciple * siRate * siTime) / 100
    siAmount = ((siPrinciple * siRate * siTime) / 100) + siPrinciple
    print("SI = ₹", si)
    print("Amount = ₹", siAmount)
elif choice == "CI" or choice == "ci":
    print ("Welcome to CI calculator!")
    print("Enter the asked values, type 0 if value is not given!")
    ciPrinciple = int(input("What is the principle amount? "))
    ciRate = int(input("What is the Rate of Interest? "))
    ciTime = int(input("What is the Time Period? "))
    ciAmount = int(input("Enter the Amount (if you know): "))
    ciAmountForCI = (ciPrinciple * (1 + ciRate/100) ** (2 * ciTime))
    ci = ciAmountForCI - ciPrinciple
else: 
    print("Sorry an ERROR occured, please enter something valid!")