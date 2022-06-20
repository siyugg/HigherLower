import random
from art import *
from game_data import data
import os

score=0
guess = True
print(logo)
while guess:
    a=random.randint(0,len(data))
    b=random.randint(0,len(data))
    print("Compare A: "+data[a]['name']+', a '+data[a]['description']+" from "+data[a]['country'])
    print(vs)
    print("Against B: "+data[b]['name']+', a '+data[b]['description']+" from "+data[b]['country'])
    answer=input("Who has more followers? A or B:")

    followerA=data[a]['follower_count']
    followerB=data[b]['follower_count']
    if followerA>followerB:
        if answer == 'A':
            os.system('cls')
            score+=1
            print("You're right! Score: "+str(score))
        elif answer=='B':
            os.system('cls')
            print("Sorry, your answer is wrong. Final score = "+ str(score))
            guess = False
    elif followerB>followerA:
        if answer=='B':
            os.system('cls')
            score+=1
            print("You're right! Score: "+str(score))
        elif answer=='A':
            os.system('cls')
            print("Sorry, your answer is wrong. Final score: "+ str(score))
            guess = False

