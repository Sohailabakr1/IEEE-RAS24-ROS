import sys
import rospy
from my_first_service.srv import AddTwoIntSrv
from my_first_service.srv import AddTwoIntSrvRequest
from my_first_service.srv import AddTwoIntSrvResponse

def add_two_ints_clients(x,y):
    rospy.wait_for_service("add_two_ints")
    try:
        add_two_ints = rospy.Serviceproxy("add_two_ints",AddTwoIntSrv)
        resp1 = add_two_ints(x,y)
        return resp1.sum
    excepect rospy.ServiceProxy as e:
    print("Service call failed: %s" %e)
     
if __name__ =="__main__" :
   if len(sys.argv)== 3:
           x= int (sys.argv)[1]== 3
           y= int (sys.argv[2])
eles:
sys.exit(1)
print("Requestiong %s+%s"%(x,y))
print("%s + %s=%s"%(x,y,add_two_ints_client(x,y)))
       