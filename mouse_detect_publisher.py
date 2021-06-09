#!/usr/bin/env python
import rospy
from std_msgs.msg import Bool
import struct
file = open( "/dev/input/mice", "rb" );

def mouse_pub_fun():
    mouse_object_right = rospy.Publisher('mouse_topic_r', Bool, queue_size=10)
    mouse_object_left = rospy.Publisher('mouse_topic_l', Bool, queue_size = 10)
    mouse_object_middle =rospy.Publisher('mouse_topic_m', Bool, queue_size = 10)
    rospy.init_node('mouse_pub', anonymous=False)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        buf = file.read(3);
        button = ord( buf[0] );
        bLeft = button & 0x1;
        bMiddle = ( button & 0x4 ) > 0;
        bRight = ( button & 0x2 ) > 0;
        x,y = struct.unpack( "bb", buf[1:] );
        mouse_object_right.publish(bRight)
        rate.sleep()
        mouse_object_left.publish(bLeft)
        rate.sleep()
        mouse_object_middle.publish(bMiddle)
        rate.sleep()

if __name__=='__main__':
    try:
        mouse_pub_fun()
    except rospy.ROSInterruptException:
        pass
