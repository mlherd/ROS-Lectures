#!/usr/bin/env python
import rospy
from std_msgs.msg import String

global msg
msg = ""
pub = rospy.Publisher('display', String, queue_size = 5)

def c1(content):
    global msg
    path = "/home/melih/catkin_ws/src/file_reader_writer/scripts/" + content.data
    try:
        file = open(path, "r")
        msg = file.read()
        pub.publish(msg)
        file.close()
    except:
        print "file is not there"
        
def filereader():
    rospy.init_node('filereader', anonymous=True)
    rospy.Subscriber("file_name", String, c1)
    rospy.spin()

if __name__ == '__main__':
    filereader()
