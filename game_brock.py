#used for random numbers
import random

#used for creating time intervals
import time

#making texts look better
from unicodedata import name 

#The player stats are stored here 
class user:
    def __init__(self, username, location, money, items, loan) :
        self.name = username 
        self.location = location
        self.money = money
        self.items = items
        self.loan = loan


#used to store attributes and descriptions of items
class item:
    def __init__(self, name, value, description) :
        self.name = name 
        self.value = value
        self.description= description   


#dressmaking tool for making dresses in the shed
dressmaker= item("Dressmaker", 1000, "Make dresses in it")

#pickaxe to use in the mine
pickaxe= item("Pickaxe", 50 ,"This tool helps you mine in your mineshaft")

#used to grow crops in the farm
seeds= item("Seeds", 10,"plant the seeds in the farm to earn money!")

#used to make a dress alongside the dressmaker in the shed
cloth= item("Cloth", 40,"To make a dress!")

#looks useless but is useful for secret ending
goatee= item("Goatee",100, "Useless, Mr Brock is just tryna look cool in it")

#used to talk to the king
dress= item("Fancy Dress",1000, "a dress for the king's wife")

#introduction sentence
print("\nBelle: Oh sweet gracious, hi! Welcoome to land of Erehdon")

#PREGAME NEEDS
#username
username= input("HIHIHIHI, Whats your name again sweetheart? ")

player=user(username.title(),"Erehdale",0 ,[], 0 )


#ENDINGS
#SECRET ENNDING USINNG GOATEE
def secretending():
    print("King Bob: KILL HIMMM")
    time.sleep(2)
    print("Mr Brock: I have been exiled for 100 years and finally I have risen. ")
    time.sleep(2)
    print(f"""Mr Brock: With the power of my goatee I give you, {player.name} 
    my powers as a magical fairy """)
    time.sleep(2)


#FINAL CODE TO BEAT THE KING!
    ending= input("""Mr Brock: Quick type the secret code to defeat King Bob!
'UP'""")
    if ending.lower()=="up":
        ending=input("""Mr Brock:
Type 'UP'""")
        if ending.lower()=="up":
            ending=input("""Mr Brock:
Type 'Down'""")
            if ending.lower()=="down":
                ending=input("""Mr Brock:
Type 'Down'""")
                if ending.lower()=="down":
                    ending=input("""Mr Brock:
Type 'Right' """)
                    if ending.lower()=="right":
                        ending=input("""Mr Brock:
Type 'Left'""")
                        if ending.lower()=="left":
                            ending=input("""Mr Brock:
Type 'Right' """)
                            if ending.lower()=="right":
                                ending=input("""Mr Brock:
Type 'Left'""")
                                if ending.lower()=="left":
                                    ending=input("""Mr Brock: 
Type 'B'""")
                                    if ending.lower()=="b":
                                        ending=input("""Mr Brock:
Type 'A'""")
                                    if ending.lower()=="A":
                                        print("*King Bob vanished to the land of the hockey sticks*")
                                        goodending()
    losegame("Summoning Mr Brock")


#good ending/secret ending continuation
def goodending():
    time.sleep(2)
    print(f"""Rise up for the new leader of Erehdale: 
{player.name} 
the greatest fairy ever lived! """)
    time.sleep(2)
    print("Erehdale has never felt sufffering ever since")
    time.sleep(2)
    print(f"and {player.name}, the fairy, the leader, lived happily ever ater")
    time.sleep(2)
    print("""
████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
You finished the game with a happy ending""")
    #final step to win the game
    winenter= input("Press enter to quit the game")
    win= False
    while win== False:
        if winenter=="":
            exit()
        else:
            winenter= input("Press enter to quit the game")


#losing the game brings to this page
def losegame(causeofloss):
    print("King Bob: You disapointed me. I don't want to see you again.")
    print("You got executed!\ncause of execution: "+causeofloss)
    print("Game Over")
    loseenter= input("Press enter to quit the game")
    lose= False
    while lose== False:
        if loseenter=="":
            exit()
        else:
            loseenter= input("Press enter to quit the game")


#Main winninng ending
def wingame():
    print("King Bob: HEEE HEE HEE HAA what a nice dress!")
    time.sleep(2)
    print("King Bob: So sad that I have to execute you")
    time.sleep(2)
    print(f"{player.name}: W-why?")
    time.sleep(2)
    print("King Bob: Sorry, nothing personal, but I just like seeing people suffer")
    time.sleep(2)
    print("King Bob: Each room in the castle are filled with caskets of people I have killed")
    time.sleep(2)
    print("""
████████╗██╗░░██╗███████╗  ███████╗███╗░░██╗██████╗░
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝████╗░██║██╔══██╗
░░░██║░░░███████║█████╗░░  █████╗░░██╔██╗██║██║░░██║
░░░██║░░░██╔══██║██╔══╝░░  ██╔══╝░░██║╚████║██║░░██║
░░░██║░░░██║░░██║███████╗  ███████╗██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚══╝╚═════╝░
You finished the game but what a disturbing ending""")
    #final step to win the game
    winenter= input("Press enter to quit the game")
    win= False
    while win== False:
        if winenter=="":
            exit()
        else:
            winenter= input("Press enter to quit the game")


#FUNCTIONS AVAILABLE FOR THE WHOLE GAME 
#how to check the innvenntory
def inventory():
#checking money + loan
    print(f"You have {player.money} dollars\nYou owe {player.loan}\nYou have... ")
    itemdictionary=[]
#checking items in the invnetory
    for i in player.items:
        print(i.name)
        item_dictionary=i.__dict__
        itemdictionary.append(item_dictionary)
    print(" in your inventory")


def whereabouts():
    print(f"HEYYYY IM MAPPY MAPPPP!!! You are currently at {player.location}")


#fast travel to move place to place with a carriage
def fasttravel():
    fasttravelopen= True
    print(f"You are in {player.location}")
#options
    while fasttravelopen:
        wheretogo=input("""Charriot: Where thou want to go?
        A. Home Base\t\t\t B.Store\t\t\t C. Castle 
        D.Toolsmith\t\t\t E. City Hall\t\t\t F. Casino
        """)

        if wheretogo.title()== "A":
            homebase()
            fasttravelopen= False

        elif wheretogo.title()== "B":
            store()
            fasttravelopen= True

        elif wheretogo.title()== "D":
            toolsmith()
            fasttravelopen= True

        elif wheretogo.title()== "E":
            cityhall()
            fasttravelopen= True

        elif wheretogo.title()== "F":
            casino()
            fasttravelopen= True

        elif wheretogo.title()== "C":
            castle()
            fasttravelopen= True

        else:
            print("oopsie wroonng button")


#LOCATIONS
#home base location
def homebase():
    print("Ah... home sweet home")
    player.location= "home base"
    inhomebase=""
    inhomebaseoptions= ["A","B","C","E"]
#4 differennt locations in the homebase
    while inhomebase not in inhomebaseoptions:
        inhomebase=input("""Assistant: Where do you want to go?
        A. Mineshaft         B. Farm         C. Shed         E. Fast Travel""")


        #mineshaft
        if inhomebase.title()== "A":
            print("Miner: Welcome to the mine!")
            #checks if pickkaxe is in the inventory
            if pickaxe in player.items:
                miningmode=True
            #how many times needed to click to earn money 24. I chose 24 as in 24 hours
                miningchance= 24
                while miningmode:
                    mining=input("Miner: Press enter to mine and Z to quit Tip: Keep pressing enter until you get gold!")
                    if mining.title()=="":
                        miningchance= miningchance-1
                        if miningchance==0:
                            player.money=player.money + 50
                            print("Miner: You have gained 50 dollars!")
                            miningchance=24
            #selections for ffunnctions available throughout the game
                    elif mining.title() == "E":
                        fasttravel()
                        break
                    elif mining.title() == "G":
                        inventory()
                    elif mining.title() == "Q":
                        whereabouts()
                    elif mining.title() == "Z":
                        break
                    else:
                        print("Miner: Ooops Try Again!")
            else:
                print("Miner: You need a pickaxe to go in the mineshaft! Tip: Buy in the toolsmith")

        
        #location: farm
        elif inhomebase.title()== "B":
            print("Farmer: Welcome to the farm!")
            #checks if seeds are in the inventory
            if seeds in player.items:
                player.items.remove(seeds)
                growthtime=10
                time.sleep(2)
                print("Farmer: You have planted the seeds")
                #countdown
                while growthtime:
                    print(f"Farmer: Your crops needs {growthtime} seconds to grow!")
                    time.sleep(1)
                    growthtime= growthtime-1
                print("Farmer: Your crop grew and you sold it for 20 dollars!")
                player.money= player.money+ 20
            else:
                print("Farmer: You need seeds to go in the farm! Tip: Buy in the shop")


        #location: shed
        elif inhomebase.title()== "C":
            print("The shed is where you make your dresses!")
            #checks for a dress maker
            if dressmaker in player.items:
                #prevent duplicates
                if dress not in player.items:
                    #checks for cloth
                    if cloth in player.items:
                        player.items.remove(cloth)
                        player.items.append(dress)
                        print("YIPEEE!!! You made a gorgeous dress!")
                        time.sleep(1)
                        print(f"It is {dress.description} and it costs {dress.value} dollars")
                    else:
                        print("You need cloths make dresses! Tip: Buy in the shop")
                else:
                    print("""You already have 1 dress in your inventory, 
now give it to KING BOB in the castle""")
            else:
                print("You need a dress maker to make dresses! Tip: Buy in the toolsmith")


#selections for funnctions available throughout the game
        elif inhomebase.title() == "E":
            fasttravel()
        elif inhomebase.title() == "G":
            inventory()
        elif inhomebase.title() == "Q":
            whereabouts()
        else:
            ("Farmer: OOopsie daisey! Wrong button.")


#location store
def store():
    player.location= "store"
    selllist=[seeds, cloth, goatee]


#prints available stufff
    print("""Vendor: Hi do you want anything this time?
We have...""")
    for items in selllist:
        print(f"""\n{items.name} cost: {items.value} dollars""")
        print(items.description)


    askvendor=""
    while askvendor.lower() not in selllist:
        askvendor=input("Vendor: type your needs here.... press e to cancel")
        #buying seeds
        if askvendor.lower() == "seeds":
            if seeds not in player.items:
                if player.money >= seeds.value:
                    player.items.append(seeds)
                    player.money= player.money-seeds.value
                    print("You bought seeds")
                else:
                    print("Vendor: You don't have enough money peasant")
            else:
                print("Vendor: You already have seeds in your inventory")


#buying cloth
        elif askvendor.lower() == "cloth":
            if cloth not in player.items:
                if player.money >= cloth.value:
                    player.items.append(cloth)
                    player.money= player.money-cloth.value
                    print("You bought a Cloth")
                else:
                    print("Vendor: You don't have enough money peasant")
            else:
                print("Vendor: You already have cloth in your inventory")


#buying goatee
        elif askvendor.lower() == "goatee":
            if goatee not in player.items:
                if player.money >= goatee.value:
                    player.items.append(goatee)
                    player.money= player.money-goatee.value
                    print("You bought a Goatee")
                else:
                    print("Vendor: You don't have enough money peasant")
            else:
                print("Vendor: You already have cloth in your inventory")


#selections for funnctions available throughout the game
        elif askvendor.lower() == "e":
            fasttravel()

        elif askvendor.lower()== "g":
            inventory()

        elif askvendor.lower() == "q":
            whereabouts() 
               
        else:
            print("Vendor: Don't waste my time!")


#cityhall
def cityhall():
    player.location= "City Hall"
    print("Belle: Welcome to City hall sweety!")
    time.sleep(2)

#compensates for 0 money because you cannot do anything without money in the game
    if player.money == 0:
        print("Belle: Oh golly what happened to your money? Here, take a 10")
        player.money= int(player.money) + 10
    asking=True 

#options
    print("""Belle: What are you doing here?
A. Borrow money \t\t\tB. Give back money!\t\t\tE. Call Carriage""")
    while asking:
        askbelle= input("")

#borrow money from belle
        if askbelle.title()=="A":
            print("Can I borrow some money gurlll?")
            askborrow= True
            while askborrow:
                borrowmoney= input("""Belle: How much money do you need sweetheart? 
The state would be happy to lend it to you!(MAX: 300 Dollars)""")

#functions available in every stage of the game
                if borrowmoney.lower() == "e":
                    fasttravel()
                elif borrowmoney.lower() == "g":
                    inventory()
                elif borrowmoney.lower() == "q":
                    whereabouts()  

#spits out noonn numerical values
                while not borrowmoney.isdigit():
                    borrowmoney = input("Belle: How much money do you want to loan? ")

#functions available in every stage of the game
                    if borrowmoney.lower() == "e":
                        fasttravel()
                        break
                    elif borrowmoney.lower() == "g":
                        inventory()
                        borrowmoney= "Not a number"
                    elif borrowmoney.lower() == "q":
                        whereabouts()
                        borrowmoney= "Not a number"

#checks if money is given over the limit
                if int(borrowmoney) <= 300:
#checks previous moneny given+ money given now
                    pseudomoney= int(player.loan) + int(borrowmoney)
                    if pseudomoney > 300:
                        print("Belle: The state does not let you borrow that much money!")
                        break
                    player.money= int(player.money) + int(borrowmoney)
                    player.loan= int(borrowmoney)
                    print(f"You borrowed {borrowmoney} Now, you have {player.money} dollars in your pocket\n")
                    print("""Belle: Remember, PAY YOUR LOANS
You can only talk to the king after paying all your loans!""")
                    break
#rejects the usage of loans
                elif int(borrowmoney) >= 300:
                    print("Belle: The state does not let you borrow that much money!")
                    break


#return loan monney
        elif askbelle.title()=="B":
            print("I have your money back sistur.")
            time.sleep(2)

#checks if money is enough to return (money is enough)
            if int(player.money)>=int(player.loan):
                player.money= int(player.money) - int(player.loan)
                print(f"""Belle: Wow! You have paid all your loans!
You paid {player.loan} dollars...
Now you have {player.money} dollars!""")
                int(player.money) - int(player.loan)
                player.loan= 0

#money is not enough to return
            elif int(player.money)<=int(player.loan):
                loanmargin= int(player.loan)- int(player.money) 
                print(f"""Belle: You do not have the money to pay your loans
You need {loanmargin} dollars more to pay your loans
Come back later!""") 

#basic functions throughout the game
        elif askbelle.lower() == "e":
            fasttravel()

        elif askbelle.lower() == "g":
            inventory()

        elif askbelle.lower() == "q":
            whereabouts()  
        print("""Anything else I can do for you sweety?
A. Borrow money \t\t\tB. Give back money!""")

#toolsmith
def toolsmith():
    player.location= "Toolsmith"
    toollist=[pickaxe, dressmaker]

#selling options
    print("""ToolSmith: Oh Hello darling what can I doo fot you today? 
    We have...""")
    for items in toollist:
        print(f"""\n{items.name} cost: {items.value} dollars""")
        print(items.description)

    asktoolsmith=""
    while asktoolsmith.lower() not in toollist:
        asktoolsmith=input("ToolSmith: Order here please.... press e to cancel")


#Selling pickaxe
        if asktoolsmith.lower() == "pickaxe":
            if pickaxe not in player.items:
                if player.money >= pickaxe.value:
                    player.items.append(pickaxe)
                    player.money= player.money-pickaxe.value
                    print("You bought pickaxe")
                else:
                    print("ToolSmith: You don't have enough money boo")
            else:
                print("ToolSmith: You already have a pickaxe sweety!")


#selling dress maker
        elif asktoolsmith.lower() == "dressmaker":
            if dressmaker not in player.items:
                if player.money >= dressmaker.value:
                    player.items.append(dressmaker)
                    player.money= player.money-dressmaker.value
                    print("You bought dressmaker, visit youor shed to make one!")
                else:
                    print("ToolSmith: You don't have enough money boo")
            else:
                print("ToolSmith: You already have a dressmaker sweety!")


#basic functions throughout the game
        elif asktoolsmith.lower() == "e":
            fasttravel()

        elif asktoolsmith.lower() == "g":
            inventory()

        elif asktoolsmith.lower() == "q":
            whereabouts()   

        else:
            print("Toolsmith: UM what do you mean sweetheart?")

#castle
def castle():
    player.location= "castle"

#does not let people with a loan through
    if player.loan > 0:  
        print("""Securty guard: Im sorry, you still have loans to pay before meeting the king!
Call your cart and go elsewhere!""")
        fasttravel()

#introduction of the castle
    print(f"""Welcome to King's Bob's Castle!
King Bob: HI {player.name}, nice place huh?
I built this place with my bare hands and these rooms is for each kid I have
Nevertheless, do you have my wife's dress?""")

#ask user has a dress
    askdress= True
    while askdress:
        havedress= input("")

#user claims to have a dress
        if havedress.title() == "Yes":
            print("King Bob: Great give me the dress")
#if user has a dress
            if dress in player.items:

#pivotal question to do 
                while askdress:
                    attackornoot= input("""What do you do?
A. Attack King Bob\t\t\tB. Give the dress """)

#goatee is needed to get the secret endinng
                    if attackornoot.title()== "A":
                        if goatee in player.items:
                            secretending()
                        else:
                            losegame("Attacked the King!")

#gives the dress (win game traditionnaally)
                    elif attackornoot.title()== "B":
                        wingame()

#basic functions available throughout the game
                    elif attackornoot.title()== "E":
                        print("Carriage is not available right now")
                    elif attackornoot.title()== "Q":
                        whereabouts()
                    elif attackornoot.title()== "G":
                        inventory()

#if user lies about having the dress
            else:
                print("Kinng Bob: LIEEESS: Search him!")
                losegame("Lied to the King!")

#if user does not claim to have a dress
        elif havedress.title() == "No":
            print("King Bob: Stop wasting my time peasant")
            fasttravel()

#basic functions available throughout the game
        elif havedress.title()== "E":
            print("Carriage is not available right now")
        elif havedress.title()== "Q":
            whereabouts()
        elif havedress.title()== "G":
            inventory()
        else:
            print("Do you have it?")


#casino
def casino():
#introductionn to jimmy the gambler and the dealer
    player.location= "casino"
    print("Dealer: Welcome to the Casino!")
    time.sleep(2)
    print("Jimmy: Hey girl, are you ready to lose? \nLet's play dice, who has the lower roll loses")

#Asks if ready to gamble
    askgambling= True
    while askgambling:
        askgamble= input("Are you on for it?")
        if askgamble.title()== "Yes":
            insufficientfunds=True
#asks how much is gambled
            while insufficientfunds:
                amountgamble=input("Dealer: How much money do you want to put at stake?")

#basic functions available throughout the game
                if amountgamble.lower() == "e":
                    fasttravel()
                elif amountgamble.lower() == "g":
                    inventory()
                elif amountgamble.lower() == "q":
                    whereabouts()  

#checks if the amount is a digit
                while not amountgamble.isdigit():
                    amountgamble = input("Dealer: How much money do you want to put at stake? ")

#basic functions available throughout the game
                    if amountgamble.lower() == "e":
                        fasttravel()
                        break
                    elif amountgamble.lower() == "g":
                        inventory()
                        amountgamble= "Not a number"
                    elif amountgamble.lower() == "q":
                        whereabouts()
                        amountgamble= "Not a number"

#checks if balance is enough for the gamble
                if int(amountgamble)<=int(player.money):
                    print(f"You have bet {amountgamble} dollars")
                    insufficientfunds= False
                    input("Press any button and enter to roll")

#picks a random number as a die for jimmy
                    jimmynumber= random.randint(1,6)
                    print(f"Jimmy rolled a {jimmynumber}")
                    time.sleep(3)

#picks a random number as a die for the user              
                    mynumber= random.randint(1,6)
                    print(f"You rolled a {mynumber}")
                    time.sleep(2)

#the money calculated after the loss
                    if jimmynumber > mynumber:
                        print(f"You lost {amountgamble} dollars!")
                        player.money= int(player.money) - int(amountgamble)
                        print(f"You have {player.money} dollars in your wallet")

#the money calculated after the win
                    if jimmynumber < mynumber:
                        print(f"You won {amountgamble} dollars!")
                        player.money= int(player.money) + int(amountgamble)
                        print(f"You have {player.money} dollars in your wallet")

#the money calculated after the tie
                    if jimmynumber == mynumber:
                        print("Its a tie, house takes 1 dollar")
                        player.money= int(player.money) - 1
                        print(f"You have {player.money} dollars in your wallet")
                    print("lets play again!")

                else:
                    print("You have insufficient funds dumbhead!")
        elif askgamble.title()== "No":
            print("Why are you here then? SHOO")
            break
        else:
            print("Huh??")

#TITLE SCREEN
readystart= ("")
print("Welcome to...")
time.sleep(2)
print("""
██████╗░███████╗██╗░░░░░██╗░░░░░███████╗██╗░██████╗
██╔══██╗██╔════╝██║░░░░░██║░░░░░██╔════╝╚█║██╔════╝
██████╦╝█████╗░░██║░░░░░██║░░░░░█████╗░░░╚╝╚█████╗░
██╔══██╗██╔══╝░░██║░░░░░██║░░░░░██╔══╝░░░░░░╚═══██╗
██████╦╝███████╗███████╗███████╗███████╗░░░██████╔╝
╚═════╝░╚══════╝╚══════╝╚══════╝╚══════╝░░░╚═════╝░
██████╗░██████╗░███████╗░██████╗░██████╗███╗░░░███╗░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝████╗░████║██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
██║░░██║██████╔╝█████╗░░╚█████╗░╚█████╗░██╔████╔██║███████║█████═╝░██║██╔██╗██║██║░░██╗░
██║░░██║██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗██║╚██╔╝██║██╔══██║██╔═██╗░██║██║╚████║██║░░╚██╗
██████╔╝██║░░██║███████╗██████╔╝██████╔╝██║░╚═╝░██║██║░░██║██║░╚██╗██║██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
░██████╗████████╗██╗░░░██╗██████╗░██╗░█████╗░
██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║██╔══██╗
╚█████╗░░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██║██║░░██║
██████╔╝░░░██║░░░╚██████╔╝██████╔╝██║╚█████╔╝
╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░​​​​​""")
option=("Yes","No")
#asks user if ready?
while readystart not in option:
    askreadystart=input("Belle: Oh hi little " +username.title()+", are you ready for a jolly ride?")
    readystart= askreadystart.title()
    if readystart.title()=="Yes":
        print("Belle: Let's start our wonderful journey, love!")
        time.sleep(2)
    #exits if not ready
    elif readystart.title()=="No":
        print("Belle: OK then, see you next time little one!")
        exit()
    else:
        print("Belle: Thats's not quite right. You didn't hear me right.")


#Introduction
print("Belle: Once upon a time, in the land of Erehdon...")
time.sleep(3)
print("There was a mighty king, KING BOB!\nHe was so strong and rich that he has many wives.")
time.sleep(2)
print("Yesterday, he just lynched his dressmaker because she failed at her job.")
time.sleep(2)
print("Now it is up to you little one to step up to that role!")
time.sleep(2)
print("All you have to do is make King Bob happy, and you can earn more money!")
time.sleep(2)
print("The next day...")
time.sleep(5)


#START OF THE STORY
#only one right optioon to waking up
multiplechoice= ["A","B","C","D"]
sleepornot = ""
while sleepornot.title() not in multiplechoice:
    sleepornot = input("""Belle: Wake up, sweetheart! Its your first day on the job! 
    What do you do?
    A.*Wake up*\t\t\t\tB.*Sleep the whole day*
    C.Wake me up in 5 minutes\t\tD.*swear at Belle for waking me up*
    type in the letter...""")
    if sleepornot.title() == "A" :
        print("Belle: Alright, wake up!")
    elif sleepornot.title() == "B":
        losegame("Woke up late")
    elif sleepornot.title() == "C":
        losegame("Woke up late")
    elif sleepornot.title() == "D":
        losegame("Woke up late")
    else:
        print("Belle: Huuhhh?")
print("Belle: Let me give you a tour of the place!")


#Tutorial (functions used throughout the code)
time.sleep(2)
player.location="City Hall"
tutorial= True
while tutorial:
    answercollumn=input("Belle: This is the city hall, press Q and enter to check your whereabouts!")
    if answercollumn.title() == "Q":
        whereabouts()
        break
    else: 
        print("Belle: That ain't right innit?")


time.sleep(2)
print("""Belle: Now, you have to make the best dress for Kings Bob's wife 
Make sure make the best quality""")
time.sleep(2)
print("""Belle: You have 0 money right now, 
utilize the mine and the farm in your homebase to gather resources
and trade with other people ato earn money to build that dress using a dressmaker
don't worry sweetheart I will guide you in everystep of the way!
""")


time.sleep(2)
buydressmaker=False


while tutorial:
    answercollumn=input("""Belle: Now you can access your inventory.
All you have to do is press G""")
    if answercollumn.title() == "G":
        inventory()
        break
    else: 
        print("Belle: That ain't right innit?")



time.sleep(2)
while tutorial:
    answercollumn=input("""Belle: Great! Now you can fast travel using our carriage system.
All you have to do is press E
You can use these 3 functions throughout the game""")
    if answercollumn.title() == "E":
        fasttravel()
        break
    else: 
        print("Belle: That ain't right innit?")
