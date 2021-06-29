# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Copyright (c) 2017 Adafruit Industries
# Author: James DeVito
# Ported to RGB Display by Melissa LeBlanc-Williams
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
"""
This example is for use on (Linux) computers that are using CPython with
Adafruit Blinka to support CircuitPython libraries. CircuitPython does
not support PIL/pillow (python imaging library)!
"""

import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789

# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Turn on the Backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for color.
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Clear display.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

def clear(color):
    draw.rectangle((0, 0, width, height), outline=color, fill=color)


red = "#FF0000"
orange = "#F39800"
yellow = "#FFFF00"
green = "#00FF00"
blue = "#0000FF"
navy = "#000080"
pink = "#FF00FF"
purple = "#800080"
white = "#FFFFFF"

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
fnt_content = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)

def time_meas():
    return time.time()

def check_time():
    return int(end-start)

def draw_card(x_pos, y_pos, card_width, card_height):
    for j in range(0, 4):
        for i in range(0, 4):
            draw.rectangle([(x_pos + 60*i , y_pos + 55*j), (x_pos + card_width + 60*i, y_pos + card_height + 55*j)], outline = white, fill = white)

def open_card(x_pos, y_pos, card_width, card_height, i, j):
    draw.rectangle([(x_pos + 60*i , y_pos + 55*j), (x_pos + card_width + 60*i, y_pos + card_height + 55*j)], outline = 0, fill = 0)

def select_color(num):
    if ingame_deck[num] == "red":
        return red
    if ingame_deck[num] == "orange":
        return orange
    if ingame_deck[num] == "yellow":
        return yellow
    if ingame_deck[num] == "green":
        return green
    if ingame_deck[num] == "blue":
        return blue
    if ingame_deck[num] == "navy":
        return navy
    if ingame_deck[num] == "pink":
        return pink
    if ingame_deck[num] == "purple":
        return purple
    


def player_pos(x_pos, y_pos, player_width, player_height, color):
    draw.rectangle([(x_pos,y_pos), (x_pos+player_width, y_pos+player_height)], outline = color, fill = 0, width = 2)

deck = ["red", "orange", "yellow", "green", "blue", "navy", "pink", "purple"]

# define deck

def card_num(x_point, y_point):
    return y_point*4 + x_point

phase = 0
px = 50
py = 110

pw = 130
ph = 40

card_width = 40
card_height = 36

player_width = card_width + 10
player_height = card_height + 10

checkpoint = 0

start_x_pos = 10
start_y_pos = 20

x_pos = start_x_pos
y_pos = start_y_pos
# player's position

x_point = 0
y_point = 0

x_list = []
y_list = []
# card's location & card's location list

ingame_deck = deck + deck

record = []
record.sort()
new_record = record[0:5]

random.shuffle(ingame_deck) # randomly shuffle deck

while True:
    while True:

        clear(0)

        if not button_U.value:
            py = py - 40
            if py < 110:
                py = 110

        if not button_D.value:
            py = py + 40
            if py > 151:
                py = 150
    
        if not button_A.value:
        
            if py == 110:
                phase = phase + 1
                break

            if py == 150:
                phase = phase + 2
                break

        player_pos(px, py, pw, ph, white)

        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((20, 45), "GAME START", font = fnt, fill =rcolor)
    
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((60, 120), "Play Game", font = fnt_content, fill = rcolor)
    
        disp.image(image) 
        time.sleep(0.1)

    start = time_meas()  # check the time - start
    
    while True:
    

        clear(0)

        player_pos(x_pos-5, y_pos-5, player_width, player_height, green)
   
        draw_card(start_x_pos, start_y_pos, card_width, card_height)
    
        for n in range(len(x_list)):
            open_card(start_x_pos, start_y_pos, card_width, card_height, x_list[n], y_list[n])

        if not button_U.value:  # up pressed 
            y_pos = y_pos - 55
            if y_pos < 20:
                y_pos = 20
    # move up between card
            
            y_point = y_point - 1
            if y_point < 0:
                y_point = 0
            time.sleep(0.01)

        if not button_D.value:
            y_pos = y_pos + 55 
            if y_pos > 185:
                y_pos = 185
    # move down between card
            y_point =  y_point + 1
            if y_point > 3:
                y_point = 3
            time.sleep(0.01)
         
        if not button_R.value:  
            x_pos = x_pos + 60
            if x_pos > 190:
                x_pos = 190
    # move right in card
            x_point = x_point + 1
            if x_point > 3:
                x_point = 3
            time.sleep(0.01)

    
        if not button_L.value:
            x_pos = x_pos - 60
            if x_pos < 10:
                x_pos = 10
    # move left in card
            x_point = x_point - 1
            if x_point < 0:
                x_point = 0
            time.sleep(0.01)

        if not button_C.value:
            time.sleep(0.2)
            checkpoint = checkpoint + 1
     
            if checkpoint == 1:
                first_x_pos = x_pos
                first_y_pos = y_pos
                first = card_num(x_point, y_point)
                x_list.append(x_point)
                y_list.append(y_point)
                rcolor1 = select_color(first)

            if checkpoint == 2:
                second_x_pos = x_pos
                second_y_pos = y_pos
                second = card_num(x_point, y_point)
                rcolor2= select_color(second)
            
                if first == second:
                    checkpoint = 1
                    x_list.pop()
                    y_list.pop()


                if ingame_deck[first] == ingame_deck[second]:
                    x_list.append(x_point)
                    y_list.append(y_point)
            
                else:
                    x_list.pop()
                    y_list.pop()
            
            if checkpoint > 2:
                checkpoint = 0
    # If you check the 2 cards and they didn't match, reverse the card

    # A button

        if checkpoint == 1:
            draw.rectangle([(first_x_pos, first_y_pos), (first_x_pos + card_width, first_y_pos + card_height)], outline = rcolor1, fill = rcolor1)

        if checkpoint == 2:
            draw.rectangle([(first_x_pos, first_y_pos), (first_x_pos + card_width, first_y_pos + card_height)], outline = rcolor1, fill = rcolor1)
            draw.rectangle([(second_x_pos, second_y_pos), (second_x_pos + card_width, second_y_pos + card_height)], outline = rcolor2, fill = rcolor2)
    
            if ingame_deck[first] == ingame_deck[second]:
                draw.rectangle([(first_x_pos, first_y_pos), (first_x_pos + card_width, first_y_pos + card_height)], outline = 0, fill = 0)
                draw.rectangle([(second_x_pos, second_y_pos), (second_x_pos + card_width, second_y_pos + card_height)], outline = 0, fill = 0)
                checkpoint = 0

        if len(x_list)+len(y_list) == 32:
            break
    
        # Display the Image
        disp.image(image) 
        time.sleep(0.01)

    end = time_meas() # check the time -  end
    while True:
 

        clear(white)

        time = str(check_time())
    
        rcolor = tuple(int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1))
        draw.text((30, 60), "GAME OVER", font = fnt, fill =rcolor)
        draw.text((30, 120), "Time:"+ time+ "sec", font=fnt, fill=rcolor)
 
        record.append(time)

        if not button_A.value:
            break
        
        if not button_B.value:
            break


        disp.image(image) 


