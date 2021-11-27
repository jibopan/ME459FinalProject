import  pygame, time, random


class MainGame():
    #create the window of the game
    window = None
    SCREEN_WIDTH = 1600
    SCREEN_HEIGHT = 900
    # create our tank
    TANK_P1 = None
    # TANK_P1.stop = True
    # TANK_P1.live = True
    # create enemy's tank
    EnemyTank_list = []
    # create amount of enemy's tank
    EnemyTank_count = 5
    # list to store our tank's ammo
    Bullet_list = []
    # list to store enemy's tank's ammo
    Enemy_bullet_list = []
    # list to store the effect of the explode
    Explode_list = []
    # list of wall
    Wall_list = []
    def startgame(self):

    def endgame(self):
        exit()
