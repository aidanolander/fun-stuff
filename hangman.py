import turtle
import sys
import random
turtle.setup(500,600)
turtle.hideturtle()
turtle.penup()

wordList = ('SHARK','BEGIN','LUCKY','PLACE','BURLY','NAMES','ITALY',
            'UNDER','JANUS','PLUTO')

START_AREA_X = -60
START_AREA_Y = 120

TOP_LEFT_X = -60
TOP_LEFT_Y = 140

TOP_RIGHT_X = 40
TOP_RIGHT_Y = 140

BOTTOM_LEFT_X = 0
BOTTOM_LEFT_Y = -20

BOTTOM_MID_X = 40
BOTTOM_MID_Y = -20

BOTTOM_RIGHT_X = 80
BOTTOM_RIGHT_Y = -20

NECK_X = -60
NECK_Y = 80

TORSO_X = -60
TORSO_Y = 60

HIP_X = -60
HIP_Y = 40

LEFT_ARM_X = -80
LEFT_ARM_Y = 60

RIGHT_ARM_X = -40
RIGHT_ARM_Y = 60

LEFT_LEG_X = -80
LEFT_LEG_Y = 20

RIGHT_LEG_X = -40
RIGHT_LEG_Y = 20

WORD_START_X = -100
WORD_START_Y = -60

FIRST_LETTER_X = -88
LETTERS_Y = -60

SECOND_LETTER_X = -38

THIRD_LETTER_X = 12

FOURTH_LETTER_X = 62

FIFTH_LETTER_X = 112

wrongCount = 0
rightCount = 0

turtle.goto(START_AREA_X,START_AREA_Y)
turtle.pendown()
turtle.goto(TOP_LEFT_X,TOP_LEFT_Y)
turtle.goto(TOP_RIGHT_X,TOP_RIGHT_Y)        #creating the stand
turtle.goto(BOTTOM_MID_X,BOTTOM_MID_Y)
turtle.goto(BOTTOM_LEFT_X,BOTTOM_LEFT_Y)
turtle.goto(BOTTOM_RIGHT_X,BOTTOM_RIGHT_Y)
turtle.penup()


turtle.goto(WORD_START_X,WORD_START_Y)
turtle.pendown()
turtle.setheading(0)
turtle.forward(25)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(25)
turtle.penup()
turtle.forward(25)                  # creasting the 5 letter slots
turtle.pendown()
turtle.forward(25)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(25)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(25)
turtle.penup()

#turtle.penup()
#turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
#turtle.pendown()
#turtle.right(180)

#turtle.begin_fill()         #first wrong guess, the head
#turtle.circle(20)
#turtle.end_fill()
#turtle.penup()

#turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
#turtle.pendown()
#turtle.goto(HIP_X,HIP_Y)

#turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg

#turtle.goto(HIP_X,HIP_Y)

#turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
#turtle.penup()

#turtle.goto(TORSO_X,TORSO_Y)
#turtle.pendown()

#turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)        #fifth, right arm

#turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          # and last, left arm
#turtle.penup()

#turtle.goto(FIRST_LETTER_X,LETTERS_Y)
#turtle.dot()

#turtle.goto(SECOND_LETTER_X,LETTERS_Y)
#turtle.dot()

#turtle.goto(THIRD_LETTER_X,LETTERS_Y)
#turtle.dot()

#turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
#turtle.dot()

#turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
#turtle.dot()

#def split(word):
#    return [char for char in word]                      #this block makes it so
word = random.choice(wordList)                #I can split the word
#print(split(word))                                      #Might be useless?
    
let1=word[0]
let2=word[1]
let3=word[2]                            #turns the letters into variables
let4=word[3]
let5=word[4]

#########################guess1###################################

guess1=str(input('Make your first guess: '))
if guess1 in word:                          #sees if the guess was correct
    rightGuess1Data=(word.find(guess1))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess1Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess1,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess1Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess1,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess1Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess1,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess1Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess1,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess1Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess1,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess2###################################

guess2=str(input('Make your second guess: '))
if guess2 in word:                          #sees if the guess was correct
    rightGuess2Data=(word.find(guess2))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess2Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess2,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess2Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess2,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess2Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess2,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess2Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess2,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess2Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess2,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess3###################################
    
guess3=str(input('Make your third guess: '))
if guess3 in word:                          #sees if the guess was correct
    rightGuess3Data=(word.find(guess3))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess3Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess3,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess3Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess3,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess3Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess3,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess3Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess3,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess3Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess3,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess4###################################

guess4=str(input('Make your fourth guess: '))
if guess4 in word:                          #sees if the guess was correct
    rightGuess4Data=(word.find(guess4))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess4Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess4,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess4Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess4,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess4Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess4,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess4Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess4,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess4Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess4,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess5###################################

guess5=str(input('Make your fifth guess: '))
if guess5 in word:                          #sees if the guess was correct
    rightGuess5Data=(word.find(guess5))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess5Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess5,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess5Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess5,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess5Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess5,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess5Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess5,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess5Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess5,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess6###################################

guess6=str(input('Make your sixth guess: '))
if guess6 in word:                          #sees if the guess was correct
    rightGuess6Data=(word.find(guess6))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess6Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess6,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess6Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess6,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess6Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess6,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess6Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess6,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess6Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess6,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess7###################################

guess7=str(input('Make your seventh guess: '))
if guess7 in word:                          #sees if the guess was correct
    rightGuess7Data=(word.find(guess7))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess7Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess7,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess7Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess7,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess7Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess7,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess7Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess7,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess7Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess7,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess8###################################

guess8=str(input('Make your eighth guess: '))
if guess8 in word:                          #sees if the guess was correct
    rightGuess8Data=(word.find(guess8))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess8Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess8,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess8Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess8,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess8Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess8,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess8Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess8,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess8Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess8,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess9###################################

guess9=str(input('Make your ninth guess: '))
if guess9 in word:                          #sees if the guess was correct
    rightGuess9Data=(word.find(guess9))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess9Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess9,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess9Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess9,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess9Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess9,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess9Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess9,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess9Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess9,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

#########################guess10###################################

guess10=str(input('Make your tenth guess: '))
if guess10 in word:                          #sees if the guess was correct
    rightGuess10Data=(word.find(guess10))     #gets the data in guess1 
    #print(word[rightGuess1Data])
    if rightGuess10Data == 0:
        turtle.goto(FIRST_LETTER_X,LETTERS_Y)
        turtle.write(guess10,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess10Data == 1:
        turtle.goto(SECOND_LETTER_X,LETTERS_Y)
        turtle.write(guess10,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess10Data == 2:
        turtle.goto(THIRD_LETTER_X,LETTERS_Y)
        turtle.write(guess10,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess10Data == 3:
        turtle.goto(FOURTH_LETTER_X,LETTERS_Y)
        turtle.write(guess10,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    if rightGuess10Data == 4:
        turtle.goto(FIFTH_LETTER_X,LETTERS_Y)
        turtle.write(guess10,font=16)
        rightCount = rightCount+1
        if rightCount==5:
            sys.exit('Congrats! You won!')
        else:
            pass
    else:
        pass
    

else:
    print('Wrong.')
    wrongCount = wrongCount+1
    if wrongCount == 1:
        print('Try again!')
        turtle.penup()
        turtle.goto(START_AREA_X,START_AREA_Y)      #orienting it for the head
        turtle.pendown()
        turtle.right(180)

        turtle.begin_fill()         #first wrong guess, the head
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
    else:
        pass

    if wrongCount==2:
        print('Try again!')
        turtle.goto(NECK_X,NECK_Y)          #second wrong guess, the body
        turtle.pendown()
        turtle.goto(HIP_X,HIP_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==3:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(RIGHT_LEG_X,RIGHT_LEG_Y)    #third, right leg
        turtle.penup()
    else:
        pass

    if wrongCount==4:
        print('Try again!')
        turtle.goto(HIP_X,HIP_Y)
        turtle.pendown()
        turtle.goto(LEFT_LEG_X,LEFT_LEG_Y)      #fourth, left leg
        turtle.penup()
    else:
        pass

    if wrongCount==5:
        print('Try again!')
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()                        #fifth, the right arm
        turtle.goto(RIGHT_ARM_X,RIGHT_ARM_Y)
        turtle.penup()
    else:
        pass

    if wrongCount==6:
        turtle.goto(TORSO_X,TORSO_Y)
        turtle.pendown()
        turtle.goto(LEFT_ARM_X,LEFT_ARM_Y)          #finally sixth, the left arm, and you're done
        turtle.penup()
        print('Oops, out of tries. The word was ',word,', play again!',sep='')
        sys.exit()
    else:
        pass

