#THE GOAL 
#Build an interactive VIRTUAL PET SIMULATOR where you adopt a digital pet and try to keep it alive and happy by feeding ,playing with
#and resting it on multiple days .
#THE REQUIEMENTS 
#keep the pet happy and its energy over 0 at all time or else the pet will die .
# if you manage to make it to the 100% of the pet energy the pet will evolve , activating  more abilities and having more energy .
# step 1 ask the user to name the pet .
name = str(input("ENTER THE NAME YOU'D LIKE TO GIVE TO YOUR BELOVED PET : "))
print("CONGRATULATIONS YOU'VE GOT YOUR PET ")
energy = 50 # step2  set a fixed energy ,hunger and happiness to begin with .
hunger = 50 
happiness = 50
 # step 3 set a while loop to keep the user asking to feed ,, play or sleep the pet  to keep it alive .
while True: 
    care_action = str(input(" choose (feed , sleep or to play) to keep the pet alive and help it grow or enter exit to let it die :")).lower().strip()
    if care_action == "exit":
         print("you decided to kill your pet sooo\n IT DIED !")
         break
    elif care_action == "feed":
             hunger -= 20
             energy -= 5
             print("you've fed your pet and now its hunger is ",max(0,hunger),"and your pet's energy is ",max(0,energy))   
    elif care_action == "play":
         happiness += 20
         hunger +=15
         energy -= 15 
         print("you are done playing with your pet and now its energy is :", max(0,energy)," its happiness is :",max(0,happiness),"\nits hunger is :", max(0,hunger))
    elif care_action == "sleep":
         energy += 30 
         hunger += 10 
         print("your pet had a good sleep ,and now its energy is :",max(0,energy),"its hunger is :",max(0,hunger))
    else :
         try :
              print("please choose b/w feed ,sleep or play to keep your pet alive" )  
         except:
              ValueError  
    if energy <5 :
         print("your pet died !,\n cause of low energy ")
         break
    elif energy>100 :
         print(" you did a great job and now your pet has evoleved ,\n you get to choose a new name for your pet ")
         name = input("enter the new name for your evolved pet")
    elif hunger >80:
         print("your pet dying cause of hunger hurry up and feed it or else it will die ")
         care_action = str(input("choose to feed sleep or play basd on your pets need :")) 
         if care_action == "feed":
              hunger -= 10
              print("GOOD JOB ,you saved your pet from dying") 
         else:
              energy=0
              print("OOPS ! your pet died .")
              break 
    elif happiness <5:
         print("your pets happiness index is gowing down choose someting to make it happy or else it will DIE.")
         if care_action == "play":
              happiness += 10
              print("perfect decison , \nyou saved your pet from dying")  
         else:
              print("your pet died cause of UNHAPPINESS") 
                                                  
