import subprocess
import time
from clashbot.tools.simpleActions import Actions

'''# Samsung S23 - 1080x2340
length = 2340
width = 1080'''
# Galaxy Tab S8 - 2560x1600
length = 2560
width = 1600
screen = Actions.screenshot()

class baseMaintenance():
    """
    This is a nearly functional skeleton for handling daily base upgrades,
    because the cords for screenshots are unknown and 
    Actions.read_text_from_region() is kind of unreliable
    """
    def upgrades():
        
        # Screenshot Builder Tab to know how many builders are avaliable
        sc = Actions.screenshot()
        values = Actions.read_text_from_region(screenshot=sc, x1=0, y1=0, x2=0, y2=0)
        # Once I know the values, put whatever logic needed to get these variables
        avaliableB, totalB = values

        workingB = totalB - avaliableB
        Actions.tap(1280, 100) # Open Builder Tab

        # Select next suggested upgrade
        nxtUpgradeY =  306 + ((workingB - 1) * 70) + 140
        Actions.tap(1280, nxtUpgradeY)



    
# Take basic screenshot, no tabs open
# Take sc w/ builder tap open
# Take sc w/ research tab open
#
# Find avaliable builder count, resource count, and all suggested upgrades
# Upgrade priority
#   1. Builder Tab/Buildings heros
#   2. Research Tab
#   3. Pet House & Blacksmith (include loop to find pet house)



