try:
    ball_color = 'green'

    ball_color = input("Enter a color: ")

    if ball_color == 'green':
        print ('You earned 5 points!')
    elif ball_color == 'yellow':
        print ("You earned 10 points!")
    else :
        print ("You earned 15 points!")
        
except:
    print("Error! Enter a valid color")