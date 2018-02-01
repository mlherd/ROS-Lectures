#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def c1(content):
    path = "/home/melih/catkin_ws/src/file_reader_writer/scripts/" + "file.txt"
    print "sample"
    file = open(path, "a")
    file.write(content.data)
    file.close()

def filewriter():
    rospy.init_node('filewriter', anonymous=True)
    rospy.Subscriber("file_input", String, c1)
    rospy.spin()

if __name__ == '__main__':
    filewriter()
