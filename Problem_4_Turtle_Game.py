# Turtle Game
#   By Samuel Leonard
#       
#   
#   This program asks if you would like to play a game.
#   If yes, then it loads the turtle game from the Python turtle Module
#   if no, it continues to ask until you say yes.
#       The game then prompts you to select the distance the turtle travels,
#       the number of sides you want for your shape,
#       the color you want the background,  
#       and the color you want the line.    
#   Then the turtle draws your desired shape with sides n.




# defines play as string    
play = ' '
# begins a loop that requires the user to type yes, Yes, or sure.
while play != "yes" or "Yes" or "sure":
    # Woule you like to play a game?
    play = raw_input('would you like to play a game?: ')
    if play == "yes" or play == "Yes" or play == "sure":
        # on an acceptable yes answer the game loads.
        from turtle import *
        # Q1 dictates length of the line
        Q1 = int(raw_input('How far do you want to make your poor turtle walk?: '))
        #Q2  dictates number of sides.
        Q2 = int(raw_input('How many sides should your overworked turtle make?: '))
        #Q  dictates background color.
        Q3 = str(raw_input('What color ground is your exhausted turtle going to walk on: '))
        #Q  dictates pen color.
        Q4 = str(raw_input('What color pen will your wretched turtle drag?: '))
        pen1 = Pen()
        # It wouldn't be a good turtle game without a turtle shaped cursur.
        pen1.shape("turtle")
        # Background color.
        pen1.screen.bgcolor(Q3)
        # Pen color.
        pen1.color(Q4)
        # Begins the drawing function, based on user inputs.
        for i in range(Q2):
            pen1.forward(Q1)
            pen1.left(360/Q2)
    # You just can't say no...        
    elif play == "no" or play == "No":
        print "It has a really cool turtle in it..."
    # Or, anything else for that matter.    
    else:
        print "WTF, just type yes already!"
#
#
#
# Special thanks to the python turtle tutorials @ 
#        http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/Exercises.html
#        https://openhatch.org/wiki/PyCon_intro_tutorial_prep/Windows_set_up_Python   
#        https://docs.python.org
#        and hundredvisionsguy on YouTube