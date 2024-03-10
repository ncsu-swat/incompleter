#Source: https://stackoverflow.com/questions/63909122/nameerror-name-packet-is-not-defined-rlbot
from typing import Optional


from rlbot.agents.base_agent import BaseAgent, GameTickPacket, SimpleControllerState



import os
import time
import math
from rlbot.agents.base_agent import BaseAgent, SimpleControllerState
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.game_state_util import GameState, BallState, CarState, Physics, Vector3 as vector3, Rotator

import random

from rlbot.agents.base_script import BaseScript
from rlbot.utils.game_state_util import GameState



DIRECTORY_LOCATION = "C:\Logs\Recorder\log"
randNum = random.randint(0,9999999999) 

# Extending the BaseScript class is purely optional. It's just convenient / abstracts you away from
# some strange classes like GameInterface
class playerRecorder(BaseScript):
    
    def __init__(self): 
        super().__init__("playerRecorder")
        packet = self.get_game_tick_packet()
        self.writeFile = open(DIRECTORY_LOCATION+"\\"+"HumanLog"+str(car.team)+"-"+str(randNum), "w")

    def run(self):
        while True:
        
            packet = self.get_game_tick_packet()
        
            get_output(packet)
        
            sleep(1 / 3)
        
            print("test")  
    
    for car in packet.game_cars:
        if not car.is_bot:
            team = car.team
            index = car.index
            break

    def get_output(self, game_tick_packet):
       #***************************************************************    
        packet = self.get_game_tick_packet()
        
        goodTeam = str(car.team)
        
        goodLoc = packet.game_cars[car.index].physics.location
        goodLocX = str(goodLoc.x)
        goodLocY = str(goodLoc.y)
        goodLocZ = str(goodLoc.z)
        
        goodRot = packet.game_cars[car.index].physics.rotation
        goodRotP = str(goodRot.pitch)
        goodRotY = str(goodRot.yaw)
        goodRotR = str(goodRot.roll)
        
        goodVel = packet.game_cars[car.index].physics.velocity
        goodVelX = str(goodVel.x)
        goodVelY = str(goodVel.y)
        goodVelZ = str(goodVel.z)
        
        goodAngVel = packet.game_cars[car.index].physics.angular_velocity
        goodAngVelX = str(goodAngVel.x)
        goodAngVelY = str(goodAngVel.y)
        goodAngVelZ = str(goodAngVel.z)
        
        hasWC = str(packet.game_cars[car.index].has_wheel_contact)
        isSS = str(packet.game_cars[car.index].is_super_sonic)
        jumped = str(packet.game_cars[car.index].jumped)
        dJumped = str(packet.game_cars[car.index].double_jumped)
        bst = str(packet.game_cars[car.index].boost)        
        
        ballLoc = packet.game_ball.physics.location
        ballLocX = str(ballLoc.x)
        ballLocY = str(ballLoc.y)
        ballLocZ = str(ballLoc.z)        
        
        ballVel = packet.game_ball.physics.velocity
        ballVelX = str(ballVel.x)
        ballVelY = str(ballVel.y)
        ballVelZ = str(ballVel.z)
        
        self.writeFile.write(goodTeam+";"+
            goodLocX+","+goodLocY+","+goodLocZ+";"+
            goodRotP+","+goodRotY+","+goodRotR+";"+
            goodVelX+","+goodVelY+","+goodVelZ+";"+
            goodAngVelX+","+goodAngVelY+","+goodAngVelZ+";"+
            hasWC+";"+isSS+";"+jumped+";"+dJumped+";"+bst+";"+
            ballLocX+","+ballLocY+","+ballLocZ+";"+
            ballVelX+","+ballVelY+","+ballVelZ)
        self.writeFile.write("\n")
        
        
        ## WRITE OPPONENT
        badIndex = -1
        for i in range(len(packet.game_cars)):
            if i != car.index:
                badIndex = i
                break
                
        assert badIndex != car.index
        assert badIndex != -1
        
        badTeam = str(packet.game_cars[badIndex].team)
        
        badLoc = packet.game_cars[badIndex].physics.location
        badLocX = str(badLoc.x)
        badLocY = str(badLoc.y)
        badLocZ = str(badLoc.z)
        
        badRot = packet.game_cars[badIndex].physics.rotation
        badRotP = str(badRot.pitch)
        badRotY = str(badRot.yaw)
        badRotR = str(badRot.roll)
        
        badVel = packet.game_cars[badIndex].physics.velocity
        badVelX = str(badVel.x)
        badVelY = str(badVel.y)
        badVelZ = str(badVel.z)
        
        badAngVel = packet.game_cars[badIndex].physics.angular_velocity
        badAngVelX = str(badAngVel.x)
        badAngVelY = str(badAngVel.y)
        badAngVelZ = str(badAngVel.z)
        
        badhasWC = str(packet.game_cars[badIndex].has_wheel_contact)
        badisSS = str(packet.game_cars[badIndex].is_super_sonic)
        badjumped = str(packet.game_cars[badIndex].jumped)
        baddJumped = str(packet.game_cars[badIndex].double_jumped)
        badbst = str(packet.game_cars[badIndex].boost)       

        self.writeFile.write(badTeam+";"+
            badLocX+","+badLocY+","+badLocZ+";"+
            badRotP+","+badRotY+","+badRotR+";"+
            badVelX+","+badVelY+","+badVelZ+";"+
            badAngVelX+","+badAngVelY+","+badAngVelZ+";"+
            badhasWC+";"+badisSS+";"+badjumped+";"+baddJumped+";"+badbst)
        self.writeFile.write("\n")
        
        
        ## WRITE ACTION
        self.writeFile.write(str(action.throttle)+";"+str(action.steer)+";"+str(action.pitch)+";"+str(action.yaw)+";"+str(action.action.roll)+";"+str(action.jump)+";"+str(action.boost))
        self.writeFile.write("\n")
        ##*****************************************************

        return action