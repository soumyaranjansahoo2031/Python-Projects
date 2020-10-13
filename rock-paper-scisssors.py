import random

NUM=int(input("no. of times you want to play: "))
win,lose,draw=0,0,0

for i in range(NUM):
    your_weapon=input("Choose from r,p,s: ").casefold()
    master=random.choice(["r","p","s"])
    print("master's weapon: {}".format(master))

    if your_weapon == master:
        print("match draw,dono ki takat ek samaan hai")
        draw+=1
    elif your_weapon not in ["r","p","s"]:
        print(" -----------------xxxxxx INVALID INPUT xxxxx-----------------")
    elif (your_weapon == "r" and master == "s") or (your_weapon == "s" and master == "p") or (your_weapon == "p" and master == "r"):
        print("HURREYYY !, your weapon is more powerful than master.\tyou won")
        win+=1
    else:
        print("Sorry! master ne bazi marli.           \tyou lost")
        lose+=1
    print("win: {}, lose: {}, draw: {}".format(win,lose,draw))

print("\nTotal win is {} and total lose is {} and total draw {} is".format(win,lose,draw))

# elif your_weapon == "s" and master == "p":
    #     print("HURREYYY !, your weapon is more powerful than master.\nyou won")
    # elif your_weapon == "p" and master == "r":
    #     print("HURREYYY !, your weapon is more powerful than master.\nyou won")
