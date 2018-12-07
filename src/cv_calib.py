#!/usr/bin/env python
import rospy
import numpy as np
import cv2
import rosparam
import rospkg
from dynamic_reconfigure.server import Server
from dynamic_param.cfg import cv_paramConfig

def draw(config,set=False):
    if set:
        srv.update_configuration({'Red':config['Red']})
        srv.update_configuration({'Green':config['Green']})
        srv.update_configuration({'Blue':config['Blue']})
    else:
        img[:,:,0] = config['Red']
        img[:,:,1] = config['Green']
        img[:,:,2] = config['Blue']

def callback(config, level):
    # rospy.loginfo(config)
    draw(config)
    return config


if __name__ == "__main__":
    rospy.init_node("opencv_calibration", anonymous = True)
    img = np.zeros((300,300,3), np.uint8)
    cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    srv = Server(cv_paramConfig, callback)
    try:
        default = rosparam.load_file(rospkg.RosPack().get_path('dynamic_param')+'/config/param.yaml')
        # rospy.loginfo(default[0][0])
        draw(default[0][0],set=True)
    except rosparam.RosParamException:
        rospy.logwarn('calibration file [param.yaml] is not found')
    
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        cv2.imshow('result',img)
        cv2.waitKey(1)
        r.sleep()
    cv2.destroyAllWindows()