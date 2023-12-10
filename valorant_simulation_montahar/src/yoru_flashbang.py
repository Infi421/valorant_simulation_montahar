#!/usr/bin/env python3

import rospy
from valorant_simulation_montahar.msg import WorkDone
from std_msgs.msg import String

class YoruFlashbang:
    def __init__(self):
        rospy.init_node('yoru_flashbang', anonymous=True)
        self.work_done_sub = rospy.Subscriber('/work_done', WorkDone, self.work_done_callback)
        self.check_pub = rospy.Publisher('/check', String, queue_size=1)
        self.rate = rospy.Rate(1.0 / 60.0)

    def work_done_callback(self, data):
        message = data.message
        total_characters = data.total_characters
        final_string = "{} {}".format(message, total_characters)
        rospy.loginfo(final_string)
        self.check_pub.publish(final_string)
        self.rate.sleep()

if __name__ == '__main__':
    yoru_flashbang = YoruFlashbang()
    rospy.spin()