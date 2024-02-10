# Importing necessary libraries and modules for the program to have functions related to system operations, turtle graphics, and time manipulation.

import sys
from turtle import *
import time

# The function - read_and_print_file reads content from a file and display it using turtle graphics.

def read_and_print_file(file_name):
    # Open the specified file for reading.
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        # Lift the pen to move without drawing. With this, the turtle will not draw lines when moving to the write position.
        penup()
        # Set a specified color
        color("black")
        # Write the file's content on the screen with the mentioned specification.
        write(content, font=("Arial", 10, "normal"))
        # Move the turtle to the next position to continue writing so that the subsequent text will not overlap.
        move_next(110)

# The function move_next moves the turtle to the next position so the text will be properly spaced on the screen.
        
def move_next(length):
    penup() # Lift the pen to move without drawing.
    right(90)  # Turn the turtle right. With this the turtle will move in the correct direction the way we intend to.
    forward(length) # Move forward for given length.
    left(90) # Turn the turtle left to realign otherwise subsequent text will be misaligned.
    pendown() # Put the pen down to resume drawing.

# The function flash_game_status flashes game status.
    
def flash_game_status(status, color_val):
    current_pos = position() # Get current turtle position. 
    screen = Screen() # Create a screen to display the status.
    t = Turtle()  # Create a new turtle for status display.
    t.hideturtle() # Hide the turtle icon for a more cleaner display.
    t.penup() # Lift the pen to move without drawing.
    t.goto(current_pos) # Go to the current position.
    t.forward(600) # Move forward to a position for status display.
    t.pendown() # Put the pen down to start drawing.
    for _ in range(6): # Flashes the status 6 times.
        t.color(color_val)  # Set the color for the text.
        t.write(status, font=("Arial", 40, "bold")) # Writes the status on turtle.
        time.sleep(0.3) # Wait for 0.3 seconds so that the flashing will be slow enough to be observed.
        t.clear()  # Clear the text so the flashing is visible.
        time.sleep(0.3) # Wait for 0.3 seconds before the next flash.
    # Write the final status, so the status will remain on the screen after flashing
    t.color(color_val) 
    t.write(status, font=("Arial", 40, "bold"))

# The function user_input handles user input and enforce valid choices.
    
def user_input(prompt, valid_choices):
    while True:  # Keep asking until a valid choice is made by the user.
        user_choice = textinput("Choose your own story", prompt) 
        if user_choice.lower() == "quit": # Allows user to exit during mid-game.
            sys.exit() 
        # Check if input is valid so that the invalid inputs won't crash the game or cause any unexpected behavior.
        if user_choice.isdigit() and int(user_choice) in valid_choices:
            return int(user_choice) # Return the valid choice.
        else:
            # Inform the user of invalid input.
            print("Invalid input. Please enter a valid choice.")

# Sets up the turtle screen with the desired appearance and dimensions.
            
bgcolor("lightblue")
screensize(2000, 1500, "lightblue") #Scroll the turtle canvas up or down to view the final result
hideturtle()

# Initial turtle position and settings for the game title.

penup() # Lift the pen to move without drawing.
setposition(-750, 320) # sets the position according to the requirement, so the title won't overlap any other text
color("red") # Set a red color for the title
write("ADVENTURE STORY: THE MYSTICAL ODYSSEY", font=("Arial", 20, "normal")) # Write the game title with given specifications
move_next(250) # call move_next to move the turtle to the next position.

# Read and display the intended introduction of the story.

read_and_print_file("story/intro.txt") 

# Get the user's first choice.

user_choice = user_input("Please enter your choice (1, 2, 3) or type quit to exit: ", [1, 2, 3])

# With this loop, the game will have its interactive story structure.
game_over = False
game_status = False
while not game_over:

    # Handle the user's choice and display the corresponding story path. With these if-elif blocks, the game will have different story paths.
    # Each block corresponds to a different path in the story, with nested choices leading to different outcomes.
    # With these nested if-elif statements, the game will respond correctly to user choices and won't reach an end directly.
    
    if user_choice == 1:
        bgpic("images/snow.png")
        read_and_print_file("story/snow_scene.txt")
        read_and_print_file("story/snow_choice.txt")
        user_choice = user_input("Please enter your choice (1, 2) or type quit to exit: ", [1, 2])
        if user_choice == 1:
            read_and_print_file("story/snow_choice_1.txt")
            read_and_print_file("story/snow_choice_1_1.txt")
            user_choice = user_input("Please enter your choice (1, 2) or type quit to exit: ", [1, 2])
            if user_choice == 1:
                read_and_print_file("story/snow_choice_1_1_1.txt")
                read_and_print_file("story/ending_2.txt")
                game_over = True
                game_status = True
            elif user_choice == 2:
                read_and_print_file("story/snow_choice_1_1_2.txt")
                read_and_print_file("story/ending_1.txt")
                game_over = True
        elif user_choice == 2:
            read_and_print_file("story/snow_choice_2.txt")
            read_and_print_file("story/ending_2.txt")
            game_over = True
            game_status = True
    elif user_choice == 2:
        bgpic("images/island.png")
        read_and_print_file("story/island_scene.txt")
        read_and_print_file("story/island_choice.txt")
        user_choice = user_input("Please enter your choice (1, 2) or type quit to exit: ", [1, 2])
        if user_choice == 1:
            read_and_print_file("story/island_choice_1.txt")
            read_and_print_file("story/island_choice_1_1.txt")
            user_choice = user_input("Please enter your choice (1, 2) or type quit to exit: ", [1, 2])
            if user_choice == 1:
                read_and_print_file("story/island_choice_1_1_1.txt")
                read_and_print_file("story/ending_2.txt")
                game_over = True
                game_status = True
            elif user_choice == 2:
                read_and_print_file("story/island_choice_1_1_2.txt")
                read_and_print_file("story/ending_1.txt")
                game_over = True
        elif user_choice == 2:
            read_and_print_file("story/island_choice_2.txt")
            read_and_print_file("story/ending_2.txt")
            game_over = True
            game_status = True
    elif user_choice == 3:
        bgpic("images/desert.png")
        read_and_print_file("story/desert_scene.txt")
        read_and_print_file("story/desert_choice.txt")
        user_choice = user_input("Please enter your choice (1, 2): or type quit to exit ", [1, 2])
        if user_choice == 1:
            read_and_print_file("story/desert_choice_1.txt")
            read_and_print_file("story/desert_choice_1_1.txt")
            user_choice = user_input("Please enter your choice (1, 2): or type quit to exit", [1, 2])
            if user_choice == 1:
                read_and_print_file("story/desert_choice_1_1_1.txt")
                read_and_print_file("story/ending_2.txt")
                game_over = True
                game_status = True
            elif user_choice == 2:
                read_and_print_file("story/desert_choice_1_1_2.txt")
                read_and_print_file("story/ending_1.txt")
                game_over = True
        elif user_choice == 2:
            read_and_print_file("story/desert_choice_2.txt")
            read_and_print_file("story/ending_2.txt")
            game_over = True
            game_status = True
    else:
        print("Invalid choice. Please try again.")
        user_choice = user_input("Please enter your choice (1, 2, 3): or type quit to exit", [1, 2, 3])

# Display the final game status so that the game will provide a clear end message to the player.
        
flash_game_status("You Won" if game_status else "Game Over", "Green" if game_status else "Red") # Scroll down the canvas to view GAME OVER

# Finish the turtle graphics so that the turtle window will close properly after the game ends.

done()
