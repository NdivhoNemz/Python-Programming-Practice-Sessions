weight = float(input("What is your weight: "))
unit = input("Weight in (K)g or (L)bs? ")

grams = weight / 0.45
pounds = weight *  0.45

if unit == 'K' or unit == 'k':
    print("Weight in Lbs: " + str(grams))
elif unit == 'L' or unit == 'l':
    print("Weight in Kgs: ", pounds)
else:
    print("Please enter valid unit of measurement option")
