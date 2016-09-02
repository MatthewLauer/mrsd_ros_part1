#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import *
import math

# Function to set command velocity
# Note that setting turtle is commanded velocity for 1 second
def moveTurtle(pub, twist):
  pub.publish(twist)
  rospy.sleep(1.1)

# Function moves a turtle in a square
def drawSquare(pub):
  
  twist = Twist()
  moveTurtle(pub,twist)

  for i in range(4):

    twist.linear.x = 0.75
    twist.angular.z = 0

    moveTurtle(pub, twist)

    ###################################
    ### INSERT CODE HERE            ###
    ### Make turtle complete square ###
    ###################################

  return

def run():
  
  # Initialize node
  rospy.init_node('DrawSmiley')

  # Handle for calling Spawn service
  spawnService = rospy.ServiceProxy('spawn', Spawn)
  
  # Spawn a second turtle
  r = spawnService(2, 8,0,"turtle2")
  rospy.sleep(2)
  pub = rospy.Publisher('turtle2/cmd_vel', Twist, queue_size=1)
  drawSquare(pub)

  ###############################
  ### INSERT CODE HERE        ###
  ### Spawn new turtles       ###
  ### Move them appropriately ###
  ###############################


  rospy.spin()

if __name__ == '__main__':
  run()