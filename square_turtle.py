#!/usr/bin/env python3

# Import Dependencies
import rospy 
from geometry_msgs.msg import Twist 

def move_turtle_square(): 
    rospy.init_node('turtlesim_square_node', anonymous=True)
    
    # Init publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 
    rospy.loginfo("Turtles are great at drawing squares!")

    ########## YOUR CODE GOES HERE ##########
    while not rospy.is_shutdown():
        side_length = 2.0  # Define the length of each side of the square
        duration = side_length / 1.0  # Calculate the duration to move one side (adjust speed)

        # Loop to draw each side of the square
        for _ in range(4):
            # Move forward
            cmd_vel_msg = Twist() 
            cmd_vel_msg.linear.x = 1.0  # Linear velocity
            velocity_publisher.publish(cmd_vel_msg) # Publish!
            rospy.sleep(duration)  # Sleep for the duration of one side

            # Stop
            cmd_vel_msg = Twist() 
            velocity_publisher.publish(cmd_vel_msg) # Publish!

            # Rotate
            cmd_vel_msg.angular.z = 1.57  # Angular velocity (positive for clockwise)
            velocity_publisher.publish(cmd_vel_msg) # Publish!
            rospy.sleep(1.0)  # Sleep for one second (adjust as needed for rotation)
            
            # Stop
            cmd_vel_msg = Twist() 
            velocity_publisher.publish(cmd_vel_msg) # Publish!

    ###########################################

if __name__ == '__main__': 
    try: 
        move_turtle_square() 
    except rospy.ROSInterruptException: 
        pass

