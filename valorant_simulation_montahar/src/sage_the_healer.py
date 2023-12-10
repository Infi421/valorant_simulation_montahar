#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from valorant_simulation_montahar.msg import WorkDone

class SageTheHealer:
    def __init__(self):
        rospy.init_node('sage_the_healer', anonymous=True)
        self.riot_hq_sub = rospy.Subscriber('/riot_hq', String, self.riot_hq_callback)
        self.work_done_pub = rospy.Publisher('/work_done', WorkDone, queue_size=1)

    def riot_hq_callback(self, data):
        message = data.data
        # Exclude spaces from character count
        total_characters = sum(1 for char in message if char != ' ')
        work_done_msg = WorkDone(message=message, total_characters=total_characters)
        self.work_done_pub.publish(work_done_msg)

if __name__ == '__main__':
    sage_the_healer = SageTheHealer()
    rospy.spin()
