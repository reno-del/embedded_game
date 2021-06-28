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

def clear():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

red = "#FF0000" 
green = "#00FF00"
cyan = "#00FFFF"
pink = "#FF00FF"
white = "#FFFFFF"
blue = "#0000FF"

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)


def draw_card(x_pos, y_pos, card_width, card_height):
    for j in range(0, 4):
        for i in range(0, 6):
            draw.rectangle([(x_pos + 39*i , y_pos + 55*j), (x_pos + card_width + 39*i, y_pos + card_height + 55*j)], outline = white, fill = white)

def player_pos(x_pos, y_pos, player_width, player_height, color):
    draw.rectangle([(x_pos,y_pos), (x_pos+player_width, y_pos+player_height)], outline = color, fill = 0, width = 2)


deck = []

for i in ["spade", "heart", "diamond", "clover"]:
    for j in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:
        deck.append((i,j))

print(deck)
    


# define deck

start_x_pos = 10
start_y_pos = 20 # card's start point

x_pos = start_x_pos
y_pos = start_y_pos # player's position

card_width = 25
card_height = 36

player_width = card_width + 10
player_height = card_height + 10

# data that we need to know 

x_point = 0
y_point = 0

checkpoint = 0

random.shuffle(deck) # randomly shuffle deck

ingame_deck = deck[0:24] # define deck consists of 24 cards which you use in game

print(ingame_deck)

while True:

    num = y_point*6+ x_point
    
    clear()

    player_pos(x_pos-5, y_pos-5, player_width, player_height, green)
   
    draw_card(start_x_pos, start_y_pos, card_width, card_height)
   
    if not button_U.value:  # up pressed 
        y_pos = y_pos - 55
        if y_pos < 20:
           y_pos = 20
    # move up between card
        y_point = y_point - 1
        if y_point < 0:
            y_point = 0

    if not button_D.value:
        y_pos = y_pos + 55 
        if y_pos > 185:
            y_pos = 185
    # move down between card
        y_point =  y_point + 1
        
    
    if not button_R.value:  
       x_pos = x_pos + 39
       if x_pos > 205:
           x_pos = 205
    # move right in card
       x_point = x_point + 1

    
    if not button_L.value:
        x_pos = x_pos - 39
        if x_pos < 10:
            x_pos = 10
    # move left in card
        x_point = x_point - 1
        if x_point < 0:
            x_point = 0

    if not button_C.value:
         draw.rectangle([(x_pos-5,y_pos-5), (x_pos-5 + player_width, y_pos-5 + player_height)], outline = green, fill = green)
         checkpoint = checkpoint + 1
         if checkpoint == 1:
             first_x_pos = x_pos
             first_y_pos = y_pos
         if checkpoint == 2:
             second_x_pos = x_pos
             second_y_pos = y_pos
         if checkpoint > 2:
             checkpoint = 0
         time.sleep(0.1)
         draw.text((20, 150), ingame_deck[num], font=fnt, fill=green)
    
    if checkpoint == 1:
        draw.rectangle([(first_x_pos, first_y_pos), (first_x_pos + card_width, first_y_pos + card_height)], outline = red, fill = red)

    if checkpoint == 2:
        draw.rectangle([(first_x_pos, first_y_pos), (first_x_pos + card_width, first_y_pos + card_height)], outline = red, fill = red)
        draw.rectangle([(second_x_pos, second_y_pos), (second_x_pos + card_width, second_y_pos + card_height)], outline = blue, fill = blue)
        
    

    center_fill = 0

    # center

    A_fill = 0
    # A button

    B_fill = 0
    # B button
    
    # Display the Image
    disp.image(image) 
    time.sleep(0.01)
