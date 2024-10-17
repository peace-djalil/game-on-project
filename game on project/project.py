name=input("type your name:")
print("welcome", name, " to this adventurel")
answer=input("you are on an empty island, and you can north or south?")
if answer == "north":
   answer = input("I come to a lake, in the middle of an island and a land,and I either crossed it by swimming (and risking my life droning),or I built a fishing boat as a means of transportation to cross( making the boat requires a lot of time and effort,so I would run out of food and thus lose)")
   if answer == swim:
       print("Crossing the lake swimming risked drowning my life")
   elif answer=="walk":
       print("I build a fishing boat as a means of transportation to cross the lake. This requires a lot of time and effort, so I run out of food and thus lose !")
   else: 
        print ("wrong choise,I definiely lose")
elif answer == "south":
    answer =input("Reaching the old and worn-out bridge. Should I retreat and walk back for a long time and thus lose, or should I follow it and the resulting risks(to retreat/move forward)?:")
    if answer =="to retreat":
        print("you go to retreat and lose")
    elif answer== "move forward":
         answer= input("crossing an old bridge on foot It takes me to the location of the treasure, but,I could fall to the bottom of the bridge and die before reaching it(yes/no)")
    if answer== "yes":  
        print("takes me to the location of the treasure,!")
    elif answer == "no":
        print("Fall from the top of the bridge") 
    else:
        print("not valid option,you lose.")
else:
        print("not valid option")   