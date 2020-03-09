#   a115_buggy_image.py
import turtle as trtl
##############
trtl_spider = trtl.Turtle()
#
''' CREATE SPIDER BODY '''
trtl_spider.pensize(40)
trtl_spider.circle(20)
# # #
''' CREATE SPIDER HEAD '''
### isn't part of the code quite yet...? its currently just a bad circle...
# # #
''' CONFIGURE SPIDER LEGS '''
spider_legs = 8 
leg_length = 70
leg_angle = 360 / spider_legs
trtl_spider.pensize(5)
leg_increment = 0
# #
'''DRAW LEGS'''
while (leg_increment < spider_legs):
  trtl_spider.goto(0,20)
  trtl_spider.setheading(leg_angle*leg_increment)
  trtl_spider.forward(leg_length)
  #  trtl_spider.forward(leg_length)
  leg_increment = leg_increment + 1

# # #

trtl_spider.hideturtle()

# # # # 
wn = trtl.Screen()
wn.mainloop()