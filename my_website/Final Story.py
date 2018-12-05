import time
#this is a comment
def collegeBoard():
    print '___________                                    '
    print '\_   _____/  ______  ____  _____  ______   ____   '
    print ' |    __)_  /  ___/ / ___\ \__  \ \____ \_/ __ \  ' 
    print ' |        \ \___ \ \  \___  / __ \|  |_> >  ___/  ' 
    print '/_______  / /____  >\___   >____  /   __/ \___  >  ' 
    print '        \/       \/     \/      \/|__|        \/   '
    #escape the college board
    time.sleep(2)
    print 'You wake up in a dark place with no recollection of how you got there'
    time.sleep(3)
    print 'You hear a voice'
    time.sleep(1)
    print ' "Hello, You must complete a series of College Board Trademarked challenges to escape" '
    time.sleep(5)
    print ' "If you fail any challenge, you will be terminated" '
    time.sleep(3)
    print ' "Choose a door: S.A.T. or A.P." '
    time.sleep(3)
    choice1 = ''
    while choice1 != 'S.A.T.' and choice1 != 'A.P.':
        choice1 = raw_input('Which door do you go through')
        if choice1 != 'S.A.T.' and choice1 != 'A.P.':
            print 'That is not a chooseable door. Please pick S.A.T. or A.P.'
            time.sleep(2)
    if choice1 == 'A.P.':
        print ' "Interesting Choice, wait we never got your name..." '
        time.sleep(3)
        choice2 = ''
        while choice2 != 'Y' and choice2 != 'N': # y is yes and n is no
            choice2 = raw_input(' "Are you the A.P. lord and savior Nicholas Tassinari, Y or N" ')
            if choice2 != 'Y' and choice2 != 'N':
                print 'Please put Y for yes or N for no'
        if choice2 == 'Y':
            choice3 = raw_input(' "Prove it, what are your initials, including your middle names."(Use all caps and no dots')
            if choice3 == 'NBAT':
                print ' "By god, it is you. We are terribly sorry for this Mr. Tassinari, you may leave." '
                time.sleep(3)
                print 'You leave the College Board and return home safely'
                return
            elif choice3 != 'NBAT':
                    print ' "You liar!!!" '
                    time.sleep(1)
                    print 'the tears of those who failed the A.P. tests flood the room and you drown to death'
                    return 
        elif choice2 == 'N':
            print ' "That is okay, we will continue on. Please choose either United States History or Calculus" '
            time.sleep(3)
            choice4 = ''
            while choice4 != 'USH' and choice4 != 'Calc':
                choice4 = raw_input('Put USH for United States History or Calc for Calculus')
                if choice4 != 'USH' and choice4 != 'Calc':
                    print 'Please choose either USH or Calc'
            if choice4 == 'USH':
                print ' "Excellent choice, answer this question to move on" '
                choice5 = ''
                while choice5 != 'Y' and choice5 != 'N':
                    choice5 = raw_input(' "Answer with Y or N, Was Chester A. Arthur the 21st president of the U.S.A.?" ')
                    if choice5 != 'Y' and choice5 != 'N':
                        print ' "please put either Y for yes or N for no" '
                if choice5 == 'N':
                    print ' "I am sorry to see you go" '
                    time.sleep(1)
                    print 'Millions of eraser shavings from people who erase their answers fall on you and kill you'
                    return
                elif choice5 == 'Y':
                    print ' "Good Job, only one more question until freedom" '
                    time.sleep(2)
                    choice6 = raw_input(' "What year did the U.S.A. join World War 2?" ')
                    if choice6 == '1941':
                        print ' "Good job, you may leave" '
                        time.sleep(1)
                        print 'You leave and make it home safe and sound'
                        return
                    elif choice6 != '1941':
                        print ' "You came so close, what a shame..." '
                        time.sleep(2)
                        print 'Every piece of plastic wrap that covered the A.P.U.S.H. exams falls on you and you suffocate to death.'
                        return
            elif choice4 == 'Calc':
                print ' "Interesting choice" '
                choice13 = ''
                while choice13 != 'Y' and choice13 != 'N':
                    choice13 = raw_input(' "Answer with Y or N, Is the derivative of 2x^2 equal to 2x?" ')
                    if choice13 != 'Y' and choice13 != 'N':
                        print ' "please put either Y for yes or N for no" '
                if choice13 == 'Y':
                    print ' "Such a shame" '
                    time.sleep(1)
                    print 'Mr. Jennings comes out of nowhere and casts a spell on you, transporting you e^10 feet in the air. You fall to your death.'
                    return
                elif choice13 == 'N':
                    print ' "Correct, only one more question until freedom" '
                    time.sleep(2)
                    choice14 = raw_input(' "What is the integral of (sin(x))^2*cos(x) from 10 to 10" ')
                    if choice14 == '0':
                        print ' "Good job, you may leave" '
                        time.sleep(1)
                        print 'You leave and you celebrate your victory.'
                        return
                    elif choice14 != '0':
                        print ' "You came so close, what a shame..." '
                        time.sleep(2)
                        print 'Mr Brophy comes out of nowhere and throws an exercise ball at your head, it breaks your neck and you die.'
                        return
    elif choice1 == 'S.A.T.':
        print ' "Ah, the Standardized Aptitude Test. Good choice." '
        time.sleep(2)
        print ' "Choose a door, English or Math" '
        choice7 = ''
        while choice7 !='English' and choice7 !='Math':
            choice7 = raw_input('Which door do you choose?')
            if choice7 !='English' and choice7 !='Math':
                print 'that is not a choice, please pick either English or Math'
        if choice7 == 'English':
            print ' "English, lets see how good you are" '
            time.sleep(2)
            choice8 = ''
            while choice8 !='Y' and choice8 !='N':
                choice8 = raw_input('"I wish i was at there house": is it gramatically correct, Y or N?')
                if choice8 !='Y' and choice8 !='N':
                    print 'Please put either Y for yes or N for no'
            if choice8 == 'Y':
                print ' "You imbecile" '
                time.sleep(1)
                print 'Grammer Nazis come in and tie you to a post, they throw dictionaries at you until you die'
            elif choice8 == 'N':
                print ' "Good job, one more question to go" '
                time.sleep(2)
                choice9 = ''
                while choice9 !='Y' and choice9 !='N':
                    choice9 = raw_input('If all zorgs are borgs and all borgs are zombs, are all zorgs zombs? Y or N')
                    if choice9 !='Y' and choice9 !='N':
                        print 'Please put either Y for yes or N for no'
                if choice9 == 'N':
                    print ' "Your I.Q. must be low" '
                    time.sleep(1)
                    print 'The C.E.O. of the College Board walks up to you and says "perish". You turn into dust and die.'
                elif choice9 == 'Y':
                    print ' "You may leave the College Board" '
                    time.sleep(1)
                    print 'You leave the College Board victorious'
                    return
        else:
            print ' "Math, lets see if you are a math wizz" '
            time.sleep(2)
            choice11 = ''
            while choice11 !='Y' and choice11 !='N':
                choice11 = raw_input('Does x=1 in the following equation: (2x)^2=4? Y or N')
                if choice11 !='Y' and choice11 !='N':
                    print 'Please put either Y for yes or N for no'
            if choice11 == 'N':
                print ' "Then, perish" '
                time.sleep(1)
                print 'A mathemeticion asks you for a pint, another comes in and asks you for 1/2, another comes and asks for 1/4 pint. You must give them whatever percentage of a pint until 0 is reached. You die of old age.'
            elif choice11 == 'Y':
                print ' "Good job, one more question to go" '
                time.sleep(2)
                choice12 = raw_input('If two legs of a right triangle are 3 and 4, what is the hypotenuse?') 
                if choice12 != '5':
                    print ' "Oof, so close yet so far..." '
                    time.sleep(1)
                    print 'You are forced to count to infinity, you die before you can get to .00000001 percent done'
                    return
                elif choice12 == '5':
                    print ' "You have won" '
                    time.sleep(1)
                    print 'You leave and jump in the air as you are triumphent'
                    return