text = input()
happy = text.count(":-)")
sad =  text.count(":-(")
if happy>0 or sad>0:
    if happy == sad:
        print("unsure")
    elif happy < sad:
        print("sad")
    else:
        print("happy")
else:
    print("none")


