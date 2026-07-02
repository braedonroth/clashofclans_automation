from clashbot.tools.simpleActions import Actions
from clashbot.attacking.edragRageAttack import begin_attack_sequence, find_base, edragRageStrategy
import cv2

# Samsung S23 - 1080x2340
length = 2340
width = 1080

def main():
   
    x = 5
    for i in range(x):
        begin_attack_sequence()
        find_base()
        edragRageStrategy()

    return 0


main()