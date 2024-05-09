#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from first_tutorials.msg import V2V

def talker():
    pub = rospy.Publisher('chatter',String,queue_size=10)
    car_pub = rospy.Publisher('car_channel',V2V,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate= rospy.Rate(1) 
    passat_car_info = V2V()
    passat_car_info.name ="passat"

    while not rospy.is_shutdown():
        hello_str="hello world%s"%rospy.get_time()
        #rospy.loginfo(hello_str)
        pub.publish(hello_str)
        car_pub.publish(passat_car_info)
        rate.sleep()
if __name__== '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
