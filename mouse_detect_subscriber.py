#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool

def r_mousecallback(data):
    rospy.loginfo('the right click boi %d', data.data)
def l_mousecallback(data):
    rospy.loginfo('the left click boi %d ', data.data)
def m_mousecallback(data):
    rospy.loginfo('the middle click man %d ', data.data)

def mouse_sub_fun():
    rospy.init_node('mouse_sub', anonymous=False)
    rospy.Subscriber('mouse_topic_l', Bool, l_mousecallback)
    rospy.Subscriber('mouse_topic_r', Bool, r_mousecallback)
    rospy.Subscriber('mouse_topic_m', Bool, m_mousecallback)
    rospy.spin()

if __name__=='__main__':
    mouse_sub_fun()
