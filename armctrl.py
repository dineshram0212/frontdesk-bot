#!/usr/bin/env python
# coding: utf-8
import random
import Arm_Lib
import threading
import cv2 as cv
from time import sleep


class arm_ctrl:
    def __init__(self):
        self.image = None
        self.num = 0
        self.status = 'waiting'
        self.arm = Arm_Lib.Arm_Device()
        self.grap_joint = 135
        self.joints = [90, 53, 33, 36, 90, 30]


    def arm_move(self, joints_target):
        '''
        Moving process
        '''
        joints_up = [90, 80, 35, 40, 90, self.grap_joint]
        # put up 
        self.arm.Arm_serial_servo_write6_array(joints_up, 1000)
        sleep(1)
        # Release clamping jaws 
        self.arm.Arm_serial_servo_write(6, 30, 500)
        sleep(0.5)
        # Move to object position 
        self.arm.Arm_serial_servo_write6_array(self.joints, 1000)
        sleep(1)
        # Grasp and clamp the clamping claw 
        self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
        sleep(0.5)
        # put up 
        self.arm.Arm_serial_servo_write6_array(joints_up, 1000)
        sleep(1)
        # rotate 
        self.arm.Arm_serial_servo_write(1, joints_target[0], 500)
        sleep(0.5)
        # Move to corresponding position 
        self.arm.Arm_serial_servo_write6_array(joints_target, 1000)
        sleep(1.5)
        # Release the object and release the clamping jaws
        self.arm.Arm_serial_servo_write(6, 30, 500)
        sleep(0.5)
        # raise  
        joints_up[0] = joints_target[0]
        self.arm.Arm_serial_servo_write6_array(joints_up, 500)
        sleep(0.5)
        # return to center 
        self.arm.Arm_serial_servo_write(1, 90, 500)
        sleep(0.5)
        # initial position 
        joints_0 = [90, 130, 0, 0, 90, 0]
        # move to initial position 
        self.arm.Arm_serial_servo_write6_array(joints_0, 1000)
        sleep(1)

    def arm_place(self, name):
        '''
        Manipulator movement function
        '''
        print("Placing Arm")
        if name == 1 :
            # Object placement position
            # joints_target = [115, 20, 80, 40, 90, self.grap_joint]
            joints_target = [117, 19, 66, 56, 90, self.grap_joint]
            # move 移动
            self.arm_move(joints_target)
            # Grab complete 
            self.status = 'waiting'
        if name == 2:
            # joints_target = [45, 80, 0, 40, 90, self.grap_joint]
            joints_target = [44, 66, 20, 28, 90, self.grap_joint]
            self.arm_move(joints_target)
            # Grab complete 
            self.status = 'waiting'
        if name == 3 :
            # joints_target = [137, 80, 0, 40, 90, self.grap_joint]
            joints_target = [136, 66, 20, 29, 90, self.grap_joint]
            self.arm_move(joints_target)
            # Grab complete 
            self.status = 'waiting'
        if name == 4 :
            # joints_target = [65, 20, 80, 40, 90, self.grap_joint]
            joints_target = [65, 22, 64, 56, 90, self.grap_joint]
            self.arm_move(joints_target)
            # Grab complete 
            self.status = 'waiting'


#     def arm_retrieve(self, name):
#         '''
#         Retrieve an object from a designated slot to the pickup position.
#         '''
#         pickup_position = [90, 130, 0, 0, 90, 0]  # Define the joints for the pickup position
#         print("Retrieving Arm")
#         if name == 1:
#             # Move to the slot of object 1, then retrieve it
#             joints_target = [117, 19, 66, 56, 90, self.grap_joint]
#             self.arm_move(joints_target)
#             # Grab the object
#             self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
#             sleep(0.5)
#             # Move to pickup position
#             self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
#             sleep(1.5)
#             # Release the object
#             self.arm.Arm_serial_servo_write(6, 30, 500)
#             sleep(0.5)
#             # Signal complete
#             self.status = 'waiting'


#         if name == 2:
#             joints_target = [44, 66, 20, 28, 90, self.grap_joint]
#             self.arm_move(joints_target)
#             # Grab the object
#             self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
#             sleep(0.5)
#             # Move to pickup position
#             self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
#             sleep(1.5)
#             # Release the object
#             self.arm.Arm_serial_servo_write(6, 30, 500)
#             sleep(0.5)
#             # Signal complete
#             self.status = 'waiting'

#         if name == 3:
#             joints_target = [136, 66, 20, 29, 90, self.grap_joint]
#             self.arm_move(joints_target)
#             # Grab the object
#             self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
#             sleep(0.5)
#             # Move to pickup position
#             self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
#             sleep(1.5)
#             # Release the object
#             self.arm.Arm_serial_servo_write(6, 30, 500)
#             sleep(0.5)
#             # Signal complete
#             self.status = 'waiting'

#         if name == 4:
#             joints_target = [65, 22, 64, 56, 90, self.grap_joint]
#             self.arm_move(joints_target)
#             # Grab the object
#             self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
#             sleep(0.5)
#             # Move to pickup position
#             self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
#             sleep(1.5)
#             # Release the object
#             self.arm.Arm_serial_servo_write(6, 30, 500)
#             sleep(0.5)
#             # Signal complete
#             self.status = 'waiting'


    def move_to_face_capture(self):
        '''
        Move the arm to a specific position optimized for facial recognition.
        '''
        face_capture_position = [90, 110, 40, 40, 110, 0]  # Joints position for face capture
        self.arm.Arm_serial_servo_write6_array(face_capture_position, 1000)
        sleep(1)  # Ensure there's enough time for the arm to move before continuing
        self.status = 'waiting'
        print("Arm moved to face capture position.")

        
    def arm_move_reverse(self, joints_target):
        '''
        Reverse moving process
        '''
        joints_up = [90, 80, 35, 40, 90, self.grap_joint]
        # return to center 
        self.arm.Arm_serial_servo_write(1, 90, 500)
        sleep(0.5)
        # raise  
        joints_up[0] = joints_target[0]
        self.arm.Arm_serial_servo_write6_array(joints_up, 500)
        sleep(0.5)
        # Release the object and release the clamping jaws
        self.arm.Arm_serial_servo_write(6, 30, 500)
        sleep(0.5)
        # Move to corresponding position 
        self.arm.Arm_serial_servo_write6_array(joints_target, 1000)
        sleep(1.5)
        # rotate 
        self.arm.Arm_serial_servo_write(1, 90, 500)
        sleep(0.5)
        # put up 
        self.arm.Arm_serial_servo_write6_array(joints_up, 1000)
        sleep(1)
        # Grasp and clamp the clamping claw 
        self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
        sleep(0.5)
        # Move to object position 
        self.arm.Arm_serial_servo_write6_array(self.joints, 1000)
        sleep(1)
        # Release clamping jaws 
        self.arm.Arm_serial_servo_write(6, 30, 500)
        sleep(0.5)
        # put up 
        self.arm.Arm_serial_servo_write6_array(joints_up, 1000)
        sleep(1)
    
    def arm_retrieve(self, name):
        '''
        Retrieve an object from a designated slot to the pickup position.
        '''
        pickup_position = [90, 130, 0, 0, 90, 0]  # Define the joints for the pickup position
        print("Retrieving Arm")
        if name == 1:
            # Move to the slot of object 1, then retrieve it
            joints_target = [117, 19, 66, 56, 90, self.grap_joint]
            self.arm_move_reverse(joints_target)  # Reverse the movement to retrieve the object
            # Grab the object
            self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
            sleep(0.5)
            # Move to pickup position
            self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
            sleep(1.5)
            # Release the object
            self.arm.Arm_serial_servo_write(6, 30, 500)
            sleep(0.5)
            # Signal complete
            self.status = 'waiting'

        if name == 2:
            # Move to the slot of object 2, then retrieve it
            joints_target = [44, 66, 20, 28, 90, self.grap_joint]
            self.arm_move_reverse(joints_target)  # Reverse the movement to retrieve the object
            # Grab the object
            self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
            sleep(0.5)
            # Move to pickup position
            self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
            sleep(1.5)
            # Release the object
            self.arm.Arm_serial_servo_write(6, 30, 500)
            sleep(0.5)
            # Signal complete
            self.status = 'waiting'

        if name == 3:
            # Move to the slot of object 3, then retrieve it
            joints_target = [136, 66, 20, 29, 90, self.grap_joint]
            self.arm_move_reverse(joints_target)  # Reverse the movement to retrieve the object
            # Grab the object
            self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
            sleep(0.5)
            # Move to pickup position
            self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
            sleep(1.5)
            # Release the object
            self.arm.Arm_serial_servo_write(6, 30, 500)
            sleep(0.5)
            # Signal complete
            self.status = 'waiting'

        if name == 4:
            # Move to the slot of object 4, then retrieve it
            joints_target = [65, 22, 64, 56, 90, self.grap_joint]
            self.arm_move_reverse(joints_target)  # Reverse the movement to retrieve the object
            # Grab the object
            self.arm.Arm_serial_servo_write(6, self.grap_joint, 500)
            sleep(0.5)
            # Move to pickup position
            self.arm.Arm_serial_servo_write6_array(pickup_position, 1000)
            sleep(1.5)
            # Release the object
            self.arm.Arm_serial_servo_write(6, 30, 500)
            sleep(0.5)
            # Signal complete
            self.status = 'waiting'
