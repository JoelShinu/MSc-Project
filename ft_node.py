import numpy as np
import rpi_abb_irc5
import time
import sys
import os
import general_robotics_toolbox as rox
import collections
import scipy.io
import matplotlib.pyplot as plt

from OnRobot import *

from robodk.robomath import PosePP as p
from robodk.robomath import ForceTorque as ft


ft.sensor = RobotPost(r"""OnRobot""",r"""OnRobot HEX""",6, axes_type=['R','R','R','R','R','R'], ip_com=r"""127.0.0.1""", api_port=20500, prog_ptr=1729039691744, robot_ptr=1728956569872)

Fx = []
Fy = []
Fz = []
Tx = []
Ty = []
Tz = []

time_rate = 1/200
time = time * 1/200

for time in ft.sensor:
    
    values = (OnRobot.sensor(time))
    Fx.add = values(1)
    Fy.add = values(2)
    Fz.add = values(3)
    Tx.add = values(4)
    Ty.add = values(5)
    Tz.add = values(6)

    return values



