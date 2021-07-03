# NOTICE: THIS LIBRARY IS IN VERY EARLY BETA, IT IS NOT FINISHED AND WILL CHANGE IN THE FUTURE.
# THIS NOTICE IS HERE TO INFORM PEOPLE WHO WRITE SCRIPTS USING THIS LIBRARY THAT THEY WILL MOST
# LIKELY NEED TO UPDATE IN THE FUTURE
# -----------------------
# Made by Mahlarian
# -----------------------
# Credits:
# 
# Bytewave - Miscellaneous help
# Evil - Math formula used in getPixelPos()
# Brittank88 - 
#
# If your name belongs here, but it isn't, please contact me so I can add you

from collections import defaultdict
from PIL import Image as img
from time import sleep
import board
import neopixel
import os

pixels = ""
board_height = ""

# Font is a character that has the possibility of showing in a string. Characters in a string that are not found here
# will display an "X" on the board to indicate a missing character
# Characters by default are always treated as 5 pixels wide. If you need to modify this, see "spacers"
# Sprites of the character should ALWAYS start in the first column. Do not include an empty column at the start or the end
# of your sprite. This will incorrectly mess up spacing. 
# Use switchboard.py to generate sprites and get their LED coords for pasting here with ease.
font = {
    " ": [],
    "A": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,5], [3,1], [3,5], [4,1], [4,5], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]],
    "B": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,4], [2,8], [3,1], [3,4], [3,8], [4,1], [4,4], [4,8], [5,2], [5,3], [5,5], [5,6], [5,7]],
    "C": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,1], [2,8], [3,1], [3,8], [4,1], [4,8], [5,2], [5,7]],
    "D": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,8], [3,1], [3,8], [4,2], [4,7], [5,3], [5,4], [5,5], [5,6]],
    "E": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,4], [2,8], [3,1], [3,4], [3,8], [4,1], [4,4], [4,8], [5,1], [5,8]],
    "F": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,4], [3,1], [3,4], [4,1], [4,4], [5,1]],
    "G": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,1], [2,8], [3,1], [3,5], [3,8], [4,1], [4,5], [4,8], [5,2], [5,6], [5,7], [5,8]],
    "H": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,4], [3,4], [4,4], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]],
    "I": [[1,1], [1,8], [2,1], [2,8], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8], [4,1], [4,8], [5,1], [5,8]],
    "J": [[1,1], [1,7], [2,1], [2,8], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8], [4,1], [5,1]],
    "K": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,4], [2,5], [3,3], [3,6], [4,2], [4,7], [5,1], [5,8]],
    "L": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,8], [3,8], [4,8], [5,8]],
    "M": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,2], [3,3], [3,4], [4,2], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]],
    "N": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,3], [3,4], [4,5], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]],
    "O": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,1], [2,8], [3,1], [3,8], [4,1], [4,8], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7]],
    "P": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,4], [3,1], [3,4], [4,1], [4,4], [5,2], [5,3]],
    "Q": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,1], [2,8], [3,1], [3,6], [3,8], [4,1], [4,7], [5,2], [5,3], [5,4], [5,5], [5,6], [5,8]],
    "R": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,1], [2,4], [2,5], [3,1], [3,4], [3,6], [4,1], [4,4], [4,7], [5,2], [5,3], [5,8]],
    "S": [[1,2], [1,3], [1,8], [2,1], [2,4], [2,8], [3,1], [3,4], [3,8], [4,1], [4,4], [4,8], [5,1], [5,5], [5,6], [5,7]],
    "T": [[1,1], [2,1], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [3,8], [4,1], [5,1]],
    "U": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8], [2,8], [3,8], [4,8], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [5,8]],
    "V": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [2,7], [3,8], [4,7], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6]],
    "W": [[1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,8], [3,6], [3,7], [4,8], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7]],
    "X": [[1,1], [1,2], [1,6], [1,7], [1,8], [2,3], [2,5], [3,4], [4,3], [4,5], [5,1], [5,2], [5,6], [5,7], [5,8]],
    "Y": [[1,1], [1,2], [1,3], [2,4], [3,5], [3,6], [3,7], [3,8], [4,4], [5,1], [5,2], [5,3]],
    "Z": [[1,1], [1,6], [1,7], [1,8], [2,1], [2,5], [2,8], [3,1], [3,4], [3,8], [4,1], [4,3], [4,8], [5,1], [5,2], [5,8]],
    "0": [[1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [2,1], [3,1], [4,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7], [2,8], [3,8], [4,8], [2,6], [3,5], [4,4]],
    "1": [[1,3], [2,2], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7], [2,8], [1,8], [3,8], [4,8], [5,8]],
    "2": [[1,2], [2,1], [3,1], [4,1], [5,2], [1,8], [2,8], [3,8], [4,8], [5,8], [2,7], [3,6], [4,5], [5,4], [5,3]],
    "3": [[1,1], [2,1], [3,1], [4,1], [5,1], [1,7], [2,8], [3,8], [4,8], [5,7], [5,6], [5,2], [4,3], [4,5], [3,4]],
    "4": [[4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7], [4,8], [3,2], [2,3], [1,4], [1,5], [2,5], [3,5], [5,5]],
    "5": [[1,1], [1,2], [1,3], [2,1], [3,1], [4,1], [5,1], [1,7], [2,8], [3,8], [4,8], [5,7], [5,6], [5,5], [4,4], [3,4], [2,4], [1,4]],
    "6": [[5,7], [4,8], [3,8], [2,8], [1,7], [5,6], [1,6], [1,5], [1,4], [1,3], [3,1], [4,1], [5,1], [4,5], [3,5], [2,5], [2,2]],
    "7": [[1,1], [2,1], [3,1], [4,1], [5,1], [3,4], [2,5], [2,6], [2,7], [2,8], [5,2], [4,3]],
    "8": [[2,1], [3,1], [4,1], [1,2], [1,3], [1,4], [4,5], [2,5], [3,5], [5,2], [5,3], [5,4], [5,6], [5,7], [4,8], [3,8], [2,8], [1,7], [1,6]],
    "9": [[2,1], [3,1], [4,1], [1,2], [1,3], [1,4], [4,5], [2,5], [3,5], [5,2], [5,3], [5,4], [5,6], [5,7], [4,8], [3,8], [2,8], [1,8]],
    ":": [[1,2], [1,3], [1,6], [1,7]]
}
# Spacers is a way of modifying characters in "font" if they're smaller or larger than 5 pixels. This makes it so that the board
# will always put a 1x8 column in between the character. Note that you do not need to include anything here if the character is 5
# pixels wide.
spacers = {
    " ": 4,
    ":": 1,
}
# Icons are special sprites that can be displayed using the <name_here> function. They can be positioned anywhere on the board and allow
# multiple colors, whereas font characters do not.
icons = {
    
}

def init(output_pin, board_res, **kwargs):
    try:
        pixel_count = board_res[0] * board_res[1]
    except TypeError:
        raise TypeError(f"board_res must be a list with values [width, height]")
    global pixels
    pixels = neopixel.NeoPixel(output_pin, pixel_count, **kwargs)
    global board_height
    board_height = board_res[1]

# This function will not help you for any practical use, it's mainly used for other functions
def getPixelPos(coordinates):
    # Offset by 1 so you don't have to start at 0
    pixels_skipped = (coordinates[0] - 1) * board_height
    # All even numbers go up and odd numbers go down
    if (coordinates[0] % 2) == 1:
        pixel_pos = pixels_skipped + (coordinates[1] - 1)
    else:
        pixel_pos = pixels_skipped + (-coordinates[1] + board_height)
    # Return result   
    return pixel_pos

# Function for displaying scrolling text. Text will scroll starting from the right and move left.
# pausetime is how long the board will wait until displaying the next frame
# cutoff is the column on the board that will stop rendering that column
def scroll(string, color, bground_color=[0,0,0], pausetime=0.2, cutoff=0):
    # Get pixel position of every value in the coordinate list
    base_list = retrieveLetterString(string)
    scroll_list = []
    for coordinate in base_list:
        coord_pair = []
        coord_pair.append(coordinate[0] + 32)
        coord_pair.append(coordinate[1])
        scroll_list.append(coord_pair)
    while True:
        active_list = []
        for pair in range(len(scroll_list)):
            x = scroll_list[pair][0] - 1
            y = scroll_list[pair][1]
            updated_pair = [x,y]
            scroll_list[pair] = updated_pair
            if cutoff < scroll_list[pair][0] < 33:
                active_list.append(scroll_list[pair])
        pixelid_list = convertToID(active_list)
        enableLED(pixelid_list, color, bground_color)
        if not active_list:
            break
        sleep(pausetime)

# This function takes in a string and will return a list of coordinates to enable.
# Used for displaying stationary text
# Use the result of this function and pass it to convertToID()
def retrieveLetterString(string, extraspace=0):
    pixelsToEnable = []
    # the amount of spacing to start at
    spacing = 0 + extraspace
    for letter in range(len(string)):
        if letter > 0:
            spacing += spacers.get(string[letter - 1], 5) + 1
        letter_coords = font.get(string[letter], font["X"])
        for coord in letter_coords:
            formatted_coord = []
            x = int(coord[0]) + spacing
            y = coord[1]
            formatted_coord.append(x)
            formatted_coord.append(y)
            pixelsToEnable.append(formatted_coord)
    return pixelsToEnable

# Used mainly as an internal function, may or may not use serve much use on it's own.
# Takes in a list of ID's generated by convertToID() and enables all pixels in the list,
# then updates the board. Does NOT clear the board when activated, so this can be used
# to render multiple layers on top of each other
def enableLED(pixelid_list, color=[0,0,0], bground_color=[0,0,0]):
    pixels.fill(bground_color)
    for id in pixelid_list:
        if len(id) >= 2:
            pixels[id[0]] = (id[1][0], id[1][1], id[1][2])
        else:
            pixels[id[0]] = (color[0], color[1], color[2])
    pixels.show()

# Used for converting grid coordinates to pixel ID's that Neopixel's library can understand
# Will return a list of ID's that the coordniate list contained locations of
def convertToID(coordinate_list):
    pixelid_list = []
    for coord in coordinate_list:
        coord_id = getPixelPos(coord)
        converted_coord = []
        converted_coord.append(coord_id)
        if len(coord) >= 3:
            color_list = []
            for color in coord[2]:
                color_list.append(color)
            converted_coord.append(color_list)
        pixelid_list.append(converted_coord)
    return pixelid_list

def playAnimation(sprite_folder, speed, loop=False):
    if not os.path.isdir(sprite_folder):
        raise TypeError(f"{sprite_folder} is not a valid directory")
    filelist = sorted(os.listdir(sprite_folder))
    if loop == False:
        for img in filelist:
            led_list = imageToCoord(f"{sprite_folder}/{img}")
            enableLED(led_list)
            sleep(speed)
    else:
        while True:
            for img in filelist:
                led_list = imageToCoord(f"{sprite_folder}/{img}")
                id_list = convertToID(led_list)
                enableLED(id_list)
                sleep(speed)


def imageToCoord(imageName):
    try:
        userSprite = img.open(f"{imageName}")
        print("success")
    except FileNotFoundError as err:
        print(f"\nUnable to open file \"{imageName}\": Image does not exist\n")
        return
    except Exception as err:
        print(f"\nUnable to open file \"{imageName}\": {err}\n")
        return
    # Parameter to force a different board resolution maybe? Also would like to maybe
    # add option for changing behavior of rescale
    userSprite.thumbnail((32, 8))
    spriteWidth, spriteHeight = userSprite.size
    userSprite = userSprite.load()
    pixel_list = []
    for x in range(spriteWidth):
        for y in range(spriteHeight):
            pixel = [x + 1, y + 1]
            color = userSprite[x,y]
            if color[0] == 0 and color[1] == 0 and color[2] == 0:
                continue
            pixel.append(color[0:3])
            pixel_list.append(pixel)
    return(pixel_list)