def age_calc(yob):
    yob = int(input("Enter the year you were born: "))

    if yob <= 0:
        return "No negative values allowed"
    elif yob > 2018:
        return "Not allowed, unless you were born in the future"
    else:
        age = 2018 - yob
        return age

age_calc(yob)


