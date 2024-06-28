Score = int(input("what score did you get on the test?"))

if Score >= 90:
    print("Good job you did everything correctly!, You get 2000 GEL")
elif Score >= 70:
    print("You will get 1500 GEL")
elif Score >= 40:
    print("You will get 500 GEL")
elif Score < 40:
    print("You Failed")