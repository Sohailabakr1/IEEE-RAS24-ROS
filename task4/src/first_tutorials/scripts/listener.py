#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def my_callback(my_string):
    rospy.loginfo('I heard %s',my_string.data)
    
def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String,my_callback)
    rospy.spin()





if __name__== '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass 