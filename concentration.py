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
draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
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

fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)


def player_i(num):
    return num - 10 # start position of player
def player_f(num):
   return  num + 10 # final position of player
 
def up_card(y):
    if not button_U.value:  # up pressed
        y = y - 5
    # move up card

def down_card(y):
    if not button_D.value:
        y = y + 5
    # move down in card

def right_card(x):
    if not button_R.value:
        x = x + 5
    # move right in

def left_card(x):
    if not button_L.value:
        x = x - 5
    # move left

def total_card(x):
    for i in range(0,52-x): # make deck [total(52) - x =] card number you defined
        deck.pop()    

def draw_card(x_pos, y_pos):
    for j in range(0, 3):
        for i in range(0, 12):
            draw.rectangle((x_pos + i*15 , y_pos + j*18, 9, 12), outline=white, fill=white)

def draw_player(x_pos, y_pos):
    draw.rectangle((x_pos))

spade = ['spadeace', 'spade2', 'spade3', 'spade4', 'spade5', 'spade6', 'spade7', 'spade8', 'spade9', 'spade10', 'spadejack', 'spadequeen', 'spadeking']

heart = ['heartace', 'heart2', 'heart3', 'heart4', 'heart5', 'heart6', 'heart7', 'heart8', 'heart9', 'heart10', 'heartjack', 'heartqueen', 'heartking']

diamond = ['diamondace', 'diamond2', 'diamond3', 'diamond4', 'diamond5', 'diamond6', 'diamond7', 'diamond8', 'diamond9', 'diamond10', 'diamondjack', 'diamondqueen', 'diamondking']

clover = ['cloverace', 'clover2', 'clover3', 'clover4', 'clover5', 'clover6', 'clover7', 'clover8', 'clover9', 'clover9', 'cloverjack', 'cloverqueen', 'cloverking']

deck = spade + heart + diamond + clover  # define deck

card_x_pos = 20
card_y_pos = 106 # card's start point



while True:

    random.shuffle(deck) # randomly shuffle deck
        
    total card(40)

    clear()

    up_card()
    
    down_card()
    
    right_card()
    
    left_card()

    center_fill = 0
    # center

    A_fill = 0
    if not button_A.value:  # button 5 pressed
        checkpoint_a =  checkpoint_a + 1
    if not checkpoint_a == 0:
        draw_bullet((player_f(x)+x)/2, shoot_b_i(player_f(shoot_b_y)), (player_f(x)+x)/2, shoot_b_f(player_f(shoot_b_y)))
         # draw front line
    
    # A deckbutton

    B_fill = 0
    if not button_B.value: # button 6 pressed
        checkpoint_b  = checkpoint_b + 1
    if not checkpoint_b == 0:     
        draw.line(((player_f(x)+x)/2, shoot_b_i(player_f(shoot_b_y)), (player_f(x)+x)/2, shoot_b_f(player_f(shoot_b_y))), fill = button_outline, width = 2, joint = None) #draw back line
    
    # B button
    
    
    # Display the Image
    disp.image(image)    
