#!/usr/bin/python
import time
import math
total_height = 42;
total_width  = 42;
backlight = '\033[44;2m'
backlight2 = '\033[40;37;1;2m'
regionlight = '\033[47;30;1;2m'

print "Reference Color\n"
for i in range(0,10):
  print "\033[%dm \\033[%dm       " % (i+30, i+30),
print "\033[0m"
for i in range(0,10):
  print "\033[%dm \\033[%dm       " % (i+40, i+40),
print "\033[0m"

for i in range(0,10):
  print "\033[1;%dm \\033[%d;1m     " % (i+30, i+30),
print "\033[0m"
for i in range(0,10):
  print "\033[1;%dm \\033[%d;1m     " % (i+40, i+40),
print "\033[0m"

for i in range(0,10):
  print "\033[%d;%dm \\033[%d;%dm    " % (i+30, 9-i+40, i+30, 9-i+40),
print "\033[0m"
for i in range(0,10):
  print "\033[%d;%dm \\033[%d;%d;m   " % (i+40, 9-i+30, i+40, 9-i+30),
print "\033[0m"

for i in range(0,10):
  print "\033[%d;%d;1m \\033[%d;%d;1m  " % (i+30, 9-i+40, i+30, 9-i+40),
print "\033[0m"
for i in range(0,10):
  print "\033[%d;%d;1m \\033[%d;%d;1m  " % (i+40, 9-i+30, i+40, 9-i+30),
print "\033[0m\n"

#functions
def draw_string(vs, hs, height, width, color, string, center):
  print "\033[u\r",
  if(vs>0):
    print "\033[%dB\r" % (vs),
  if(math.floor((height-1)/2)*center > 0):
    print "\033[%dB\r" % (math.floor((height-1)/2)*center),
  print "%s\r" % (color),
  if(hs*2+round((width*2-len(string))/2)>0):
    print "\033[%dC" % (hs*2+round((width*2-len(string))/2)),
  print "%s%s" % (string, "\033[0m")
  time.sleep(0.03)

def draw_region(vs, hs, height, width, color, string, char_center=1):
  print "\033[u\033[%dB\r" % (total_height),
  print "Painting region %s ..%d" % (string, len(string)),
  print "\033[u\r",
  if(vs>0): print "\033[%dB\r" % (vs),
  for v in range(height):
    print "%s\r" % (color),
    if(hs>0):
      print "\033[%dC" % (hs*2),
    if(width*2>0):
      print "%s%s" % ("\033[1D", ' '*(width*2));#, "\033[0m\033[1D")
    time.sleep(0.03)
  draw_string(vs, hs, height, width, color, string, char_center);





for i in range(total_height):
   print "\r"
print "\033[%0dA\r\033[s" % (total_height)

draw_region(                 0,                 0, total_height*  1, total_width*  1, backlight,        "Top TestBench", 0)

draw_region(                 2,                 2,               3,              38, backlight2,       "Test Cases", 1)

draw_region(                 6,                 2,               21,              38, backlight2,       "DSI_HOST Environment", 0)
draw_region(                25,                 2,               15,              10, backlight2,       "", 0)
draw_region(                25,                30,               15,              10, backlight2,       "", 0)
draw_region(                28,                14,               11,              14, regionlight,      "DUT(DSI_HOST)", 1)


draw_region(                8,                  4,               5,              10, regionlight,      "Sequences", 1)
draw_region(                15,                 4,               5,              10, regionlight,      "Agent 1", 1)
draw_region(                15,                16,               5,              10, regionlight,      "Agent 2", 1)
draw_region(                15,                28,               5,              10, regionlight,      "Agent 3", 1)

draw_region(                22,                 4,               3,              34, regionlight,      "Binded Interface", 1)

print "\033[u\033[%dB\r" % (total_height),
print "Painting Finish\033[K",
