import pygame

pygame.init()  #initializes pygame module

# #We're going to create a small python list of 6 numbers,
# #  and imagine it represents some fantastic graphics we could see on the screen.
# #  It might actually be surprising how closely this represents exactly what we'll later be doing with real graphics.

# screen=[1,1,2,2,2,1]
# print(screen)

# #lets create a hero that looks like number 8.
# screen[3]=8
# print(screen)

# #lets pick a arbitary postion for hero more officially
# playerprops=3
# screen[playerprops]=8
# print(screen)

#Now lets change the position of hero.
# Its quite simple lets change the position of player props.

# playerprops=playerprops-1
# screen[playerprops]=8
# print(screen)

#OOps we got two heroes now.This is theexact reason why 
#we need to erase the hero in old position before we move into new ome.

# To deo this we need to usually keep a seperate copy of the scrreen background.
#We will create the background so it looks like our original screen did.

background=[1,1,2,2,2,1]
screen=[0]*6 #creating a new blank screen
for i in range(6):
    screen[i]=background[i]  #creating a screen same as backgound
print(screen)
playerprops=3
screen[playerprops]=8
print(screen)

#Now we will erase the previous postion of hero and add new position
#we can use the previous value using background

screen[playerprops]=background[playerprops] #screen has its original value now
playerprops=playerprops-1 #the value of palyerprops is decreased
screen[playerprops]=8
print(screen)

# The loop below moves the hero 2 steps left using loop
# for i in range(2):
#     screen[playerprops]=background[playerprops] #screen has its original value now
#     playerprops=playerprops-1 #the value of palyerprops is decreased
#     screen[playerprops]=8
#     print(screen)
