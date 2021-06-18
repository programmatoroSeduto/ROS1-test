#! usr/bin/env python

import rospy

# rospy.loginfo( "defining { %s, %s }", "", str() )

# init node
rospy.init_node( "test_param_server_py" )

# elimina le variabili se sono definite, e in caso eliminale
if ( rospy.has_param( "test_name" ) ):
	rospy.loginfo( "deleting: /name" )
	rospy.delete_param( "/name" )

if ( rospy.has_param( "/test_dict/n1" ) ):
	rospy.loginfo( "deleting namespace: /test_dict/*" )
	rospy.delete_param( "/test_dict/n" + str(1) )
	rospy.delete_param( "/test_dict/n" + str(2) )
	rospy.delete_param( "/test_dict/n" + str(3) )

# singola var stringa
'''
/test_name
'''
rospy.loginfo( "defining { %s, %s }", "name", "mario giordano" )
rospy.set_param( "test_name", "mario giordano" )

# definizione usando il dictionary
'''
/test_dict/n1
/test_dict/n2
/test_dict/n3
'''
rospy.loginfo( "defining { %s, %s }", "test_dict", str( { "n1" : "orologio", "n2" : "parrucchino", "n3" : "buonasera" } ) )
rospy.set_param( "test_dict", { "n1" : "orologio", "n2" : "parrucchino", "n3" : "buonasera" } )
