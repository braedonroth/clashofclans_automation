from tools.simpleActions import Actions
import time

# Galaxy Tab S8 - 2560x1600
length = 2560
width = 1600
"""
The logic behind this attack is super simple since I wanted to get some 
working product going. Consequently you could use this file for any
single troop army comp. 

"""
class edragRageAttack:
    """
    Methods: 
    begin_attack_search() - Navigates you to clouds for battle search
    find_base() - Presses next until adequete base is found
    strategy_loop() - Deploys the entire army

    Ex.)
    attack = edragRageAttack(run=True)
    attack.run_all()
    """
    def __init__(self):
        pass

    def run_all(self):
        """Runs the full attack pipeline in order, gated by self.run."""
        self.begin_attack_search()
        self.find_base()
        self.strategy_loop()

    def begin_attack_search(self):
        """
        While on empty homebase screen (no tabs open), this function 
        gets you attacking and into the cloud search sequence. 
        """
        print("Beginning nav to search clouds")
        # Home Base Attack Button - Big Square
        Actions.tap(x=232, y=1440)
        # Battle Button, to start a raid
        Actions.tap(x=349, y=1120)
        # Army confirmation screen
        Actions.tap(x=2199, y=1304)
        
    def find_base(self):
        """
        Keeps pressing 'Next' until find base with enough loot
        """
        while True:
            screen = Actions.screenshot()
            
            # combine gold and elixir values to attack if 800k+
            # if not, skip
            gold = Actions.read_text_from_region(screenshot=screen, x1=0, y1=183, x2=314, y2=228)
            elixir = Actions.read_text_from_region(screenshot=screen, x1=0, y1=253, x2=314, y2=298)
            gold = Actions.clean_ocr_number(gold)
            elixir = Actions.clean_ocr_number(elixir)
            total = gold + elixir
        
            if total < 800000:
                Actions.tap(2199, 1269) # Next
                time.sleep(1)
            else: 
                print("Base Found")
                break
            
            

    def strategy_loop(self, dragons=10, armyCompIcons=6, secondaryDeployQty=None):

        # CV map the base with red-border outline
        
        # x,y found by trial and error 
        start = 300
        inc = 200
        if secondaryDeployQty is None:
            deployQty = 5
        else:
            deployQty = secondaryDeployQty


        firstIcon = True  
        for i in range(armyCompIcons):
            Actions.tap(start, 1400)  # select first troop icon (L -> R)
            start += inc

            if firstIcon: # deploy all the dragons
                for _ in range(dragons):
                    Actions.tap(300, 700, pause_s=0.2)
                firstIcon = False
            else: # deploy the rest of the army
                for _ in range(deployQty):
                    Actions.tap(300, 700, pause_s=0.2)


        time.sleep(170) # Wait for attack to conclude
        Actions.tap(1170, 1300) 

        return 0

