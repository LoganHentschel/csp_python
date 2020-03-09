#   a115_buggy_image.py
import turtle as trtl
##############
trtl_spider = trtl.Turtle()
#
trtl_spider.pensize(40)
trtl_spider.circle(20)
# # #

spider_legs = 6 
leg_length = 38
leg_angle = 380 / spider_legs
trtl_spider.pensize(5)
leg_increment = 0
# #
while (leg_increment < spider_legs):
  trtl_spider.goto(0,0)
  trtl_spider.setheading(leg_angle*leg_increment)
  trtl_spider.forward(70)
  #  trtl_spider.forward(leg_length)
  leg_increment = leg_increment + 1

# # #

trtl_spider.hideturtle()

# # # # 
wn = trtl.Screen()
wn.mainloop()