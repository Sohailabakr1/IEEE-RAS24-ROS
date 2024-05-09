#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D
import matplotlib.pyplot as plt
import numpy as np
import time
from first_tutorials.msg import V2V

def get_robot_pose(data):
    rospy.loginfo("I heard {}".format(data.theta * (180 / np.pi)))
    plt.plot(data.x, data.y, marker=(3, 0, data.theta * (180 / np.pi) - 90), markersize=20, linestyle='None', color='green')
    plt.axis('equal')
    plt.draw()
    plt.pause(0.01)

def listener():
    rospy.init_node('pioneer_control', anonymous=True)
    # rospy.Subscriber("pioneer_loc", Pose2D, get_robot_pose)
    car_pub = rospy.Publisher('car_channel', V2V, queue_size=10)
    passat_car_info = V2V()
    passat_car_info.name = "passat"
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        hello_str = "hello world%s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        car_pub.publish(passat_car_info)
        rate.sleep()

        # rospy.spin()

if __name__ == '__main__':
    listener()


