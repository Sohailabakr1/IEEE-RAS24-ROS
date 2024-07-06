from my_first_service.srv import AddTwoIntSrv
from my_first_service.srv import AddTwoIntSrvRequest
from my_first_service.srv import AddTwoIntSrvResponse
import time
import rospy
def handel_add_two_ints(req):
    print("Returning[%s + %s = %s]"%(req.a ,req.b , (req.a +req.b)))
    time.sleap(5)
    sum_response = AddTwoIntSrvResponse(req.a +req.b)
    return sum_response

def add_two_ints_server():
    rospy.int_node("add_two_ints_server")
    s = rospy.service("add_two_ints", AddTwoIntsSrv,handel_add_two_ints)
    print("ready to add two ints.")
    rospy.spin()


if __name__=="__main__":
    add_two_ints_server()
