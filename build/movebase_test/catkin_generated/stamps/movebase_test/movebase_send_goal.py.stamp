
#! /usr/bin/env python

import rospy
from move_base.msg import MoveBaseActionGoal

#topic move_base
topic_move_base = None
name_move_base = "/move_base/goal"

def send_target( x, y ):
	global topic_move_base, name_move_base
	
	print( "bong!" )

def main():
	val_continue_ = True
	x = 0
	y = 0
	
	while val_contine and not rospy.is_shutdown():
		x = int(input( "target X = " ))
		y = int(input( "target Y = " ))
		
		send_target( x, y )
		
		ans = input( "Continue? [Y/n]" )
		val_continue_ = ( ans == "Y" or ans == "y" )

if __name__ == "__main__":
	rospy.init_node( "move_base_test" )
	topic_move_base = rospy.Publisher( name_move_base, MoveBaseActionGoal, queue_size=100 )
	main()
