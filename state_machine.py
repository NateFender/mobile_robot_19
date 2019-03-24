#State Machine (Moore)
from robot_class import Robot
from wall_following import follow_right as WF
from motionToGoal import motionToGoal as MTG
import time

class State():
    def __init__(self):
        print("Current State: {}".format(self))

    def event(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__


class start_state(State):

    def event(self, event=None):
        #calibrate robot
        #if goal in front but front wall detected: WF
        #if goal in front and no front wall detected: MTG
        #if goal is not in front: GF
        pass


class goal_facing(State):

    def event(self, event=None):
        return motion_to_goal()
        #run goal facing
        #if goal is not in front and front sensor < 4 in: WF
        #If goal is in front: MTG
        #if goal not in front: GF

        pass

class motion_to_goal(State):

    def event(self, event=None):
        return wall_follow()
        #run motion to goal
        #if goal is not in front and front wall detected <= 10cm: WF
        #if goal in front and 5 in of Goal: Stop
        #if goal is not in front and no wall detected: GF
        pass

class wall_follow(State):

    def event(self, event=None):
        return proportion_control()
        #run wall following
        #if goal is in front and front wall is not detected: MTG
        pass


class stop_state(State):

    def event(self, event=None):
        print("Finished")
        return False
        #stop moving the robot
        #if goal is not in front: GF
        #if goal is in front > 5 inch:  MTG
        #else: stop
        pass


class State_Machine():
    #Moore Machine
    state = None
    def __init__(self):
        self.state = start_state()

    def run(self):
        while(self.state is not False):
            self.state = self.state.event()


## testing code
if __name__ == '__main__':
    rob = Robot()
    print("GIF:{0}, no_wall:{1}, <10cm:{2}, stop_r:{3}".format(rob.GIF, rob.no_wall, rob.less_than_10, rob.stop_r))
    MTG(True, rob)
    if (rob.check_goal_in_front()):
        rob.stop_range(True)
        
    print("GIF:{0}, no_wall:{1}, <10cm:{2}, stop_r:{3}".format(rob.GIF, rob.no_wall, rob.less_than_10, rob.stop_r))
    rob.stop()
    
    # test = State_Machine()

    # test.run()
