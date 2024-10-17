#practice code:

tvShow = input("What is your favorite TV show? ")
if tvShow == "peppa pig":
    print("Ugh, why?")
    faveCharacter = input("Who is your favorite character? ")
    if faveCharacter == "daddy pig":
        print("Right answer, lol!")
    else:
        print("Nah, Daddy Pig's the greatest :)")
elif tvShow == "paw patrol":
    print ("Aww, sad times :( ")
else:
    print("Yea, that's cool and all... ")


#-----------------challenge-------------------
tvShow = input("Did you say you're a fan of Vox Machina?  Who's your favorite character? ")
if tvShow == "Vex" or "Pike" or "Grog":
    print("Nice they're my fav too!")
    faveCharacter = input("Do you remember who Grog was throwing in the intro to the first season?")
    if faveCharacter != "daddy pig":
        print("Hmmm, wanna try that again? ")
    else:
        print("Ok, now I know you're real :)")
elif tvShow != "Vex" or "Pike" or "Grog":
    print ("Aww, you're gonna have to give me some good reasons for not choosing Pike or Vex or Grog! ")
else:
    print("Yea, that's cool and all... ")
