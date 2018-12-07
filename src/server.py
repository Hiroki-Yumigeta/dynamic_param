#!/usr/bin/env python

import rospy

from dynamic_reconfigure.server import Server
from dynamic_param.cfg import TutorialConfig

def callback(config, level):
    rospy.loginfo("""Reconfigure Request: {int_param}, {double_param},\ 
          {str_param}, {bool_param}, {size}""".format(**config))
    return config

if __name__ == "__main__":
    rospy.init_node("dynamic_tutorials", anonymous = True)

    srv = Server(TutorialConfig, callback)
    rospy.spin()