#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
 

class AgentController:
    def __init__(self, name):
        self.name = name
        rospy.init_node('agent_controller', anonymous=True)
        self.riot_hq_pub = rospy.Publisher('/riot_hq', String, queue_size=1)
        self.rate = rospy.Rate(0.2)  # 0.2 Hz, 5 seconds

    def send_hello_message(self):
        hello_message = "Hello " + self.name
        rospy.loginfo(hello_message)
        self.riot_hq_pub.publish(hello_message)

    def run(self):
        while not rospy.is_shutdown():
            self.send_hello_message()
            self.rate.sleep()

if __name__ == '__main__':
    agent_controller = AgentController("Montahar")
    agent_controller.run()
