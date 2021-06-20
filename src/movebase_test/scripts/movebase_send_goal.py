
#! /usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseActionGoal
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovariance, Pose, Point, Quaternion

#topic move_base
topic_move_base = None
name_move_base = "/move_base/goal"

topic_odom = None
name_odom = "/odom"

# position, orientation
actual_pose = Pose()

def get_odom_from_topic( data ):
	global actual_pose
	actual_pose = data.pose.pose

def check_target_reached( target ):
	global actual_pose
	freq = rospy.Rate(2)
	tol = 0.001
	
	cycle = 0
	
	while ( ( target.position.x - actual_pose.position.x )**2 + ( target.position.y - actual_pose.position.y )**2 ) > tol:
		cycle = cycle + 1
		rospy.loginfo( "dist: %d" % ( ( target.position.x - actual_pose.position.x )**2 + ( target.position.y - actual_pose.position.y )**2 ) )
		freq.sleep()

def send_target( x, y ):
	global topic_move_base, name_move_base
	
	msg = MoveBaseActionGoal( )
	msg.goal.target_pose.header.frame_id = 'map'
	msg.goal.target_pose.pose.position.x = float(x)
	msg.goal.target_pose.pose.position.y = float(y)
	msg.goal.target_pose.pose.orientation.w = 1.0
	
	print(msg)
	
	topic_move_base.publish(msg)
	
	to_return = Pose()
	to_return.position.x = x
	to_return.position.y = y
	
	return to_return

def main():
	val_continue_ = True
	x = 0
	y = 0
	
	while val_continue_ and not rospy.is_shutdown():
		x = int(input( "target X = " ))
		y = int(input( "target Y = " ))
		
		tg = send_target( x, y )
		
		rospy.loginfo( "trying and reaching the target..." )
		check_target_reached( tg )
		rospy.loginfo( "target reached." )
		
		ans = input( "Continue? [Y/n]\t" )
		val_continue_ = ( ans == "Y" or ans == "y" )
	
	print( "\n" )

if __name__ == "__main__":
	rospy.init_node( "move_base_test" )
	topic_move_base = rospy.Publisher( name_move_base, MoveBaseActionGoal, queue_size=100 )
	topic_odom = rospy.Subscriber( name_odom, Odometry, get_odom_from_topic )
	try:
		main()
	except rospy.ROSException:
		pass
