user_age = int(input("Enter your age : "))
user_sex = input("Enter your sex (Male,Female OR Nonbinary) : ")


if user_age >= 65 and user_sex == ("Male"):
    print("გილოცავთ!! თქვენ გეკუთვნით პენსია.")
else:
    if user_age >= 60 and user_sex == ("Female"):
        print("გილოცავთ!! თქვენ გეკუთვნით პენსია.")

    if user_sex == ("Nonbinary"):
        print("გამასწარი აქედან სანამ გაგცხე ყურისძირში.")