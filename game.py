import pygame
import random

import os


pygame.init()
print(pygame.font.get_fonts())

def createDisplay(disWidth, disHeight, title):
    gameDis = pygame.display.set_mode((disWidth, disHeight))
    pygame.display.set_caption(title)
    return gameDis

def drawBoundary():
    white = (254, 254, 254)
    y = 7
    for i in range(14):
        pygame.draw.rect(gameDis, white, [120, y, 4, 160])
        pygame.draw.rect(gameDis, white, [240, y, 4, 160])
        pygame.draw.rect(gameDis, white, [360, y, 4, 160])
        pygame.draw.rect(gameDis, white, [480, y, 4, 160])
        y += 90

def eventHandler2nd(x_change):
    for event in pygame.event.get():                              # handles events for gamePlay Screen
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -12
            if event.key == pygame.K_RIGHT:
                x_change = 12
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    return x_change

def eventHandler3rd():
    for event in pygame.event.get():                 # handle events for gameOver Screen
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def displayObject(ob1, ob2, ob3, ob4, ob5, speed):
    ob1.moveObject(speed)
    if ob1.yCordinate > 990:
        ob1.randomAllocation()
        while abs(ob1.yCordinate - ob2.yCordinate) < 120 or abs(ob1.yCordinate - ob3.yCordinate) < 120 or\
                abs(ob1.yCordinate - ob4.yCordinate) < 120 or abs(ob1.yCordinate - ob5.yCordinate) < 120:
            ob1.randomAllocation()

    ob2.moveObject(speed)
    if ob2.yCordinate > 990:
        ob2.randomAllocation()
        while abs(ob2.yCordinate - ob1.yCordinate) < 120 or abs(ob2.yCordinate - ob3.yCordinate) < 120 or\
                abs(ob2.yCordinate - ob4.yCordinate) < 120 or abs(ob2.yCordinate - ob5.yCordinate) < 120:
            ob2.randomAllocation()

    ob3.moveObject(speed)
    if ob3.yCordinate > 990:
        ob3.randomAllocation()
        while abs(ob3.yCordinate - ob2.yCordinate) < 120 or abs(ob3.yCordinate - ob1.yCordinate) < 120 or\
                abs(ob3.yCordinate - ob4.yCordinate) < 120 or abs(ob3.yCordinate - ob5.yCordinate) < 120:
            ob3.randomAllocation()

    ob4.moveObject(speed)
    if ob4.yCordinate > 990:
        ob4.randomAllocation()
        while abs(ob4.yCordinate - ob2.yCordinate) < 120 or abs(ob4.yCordinate - ob3.yCordinate) < 120 or\
                abs(ob4.yCordinate - ob1.yCordinate) < 120 or abs(ob4.yCordinate - ob5.yCordinate) < 120:
            ob4.randomAllocation()

    ob5.moveObject(speed)
    if ob5.yCordinate > 990:
        ob5.randomAllocation()
        while abs(ob5.yCordinate - ob2.yCordinate) < 120 or abs(ob5.yCordinate - ob3.yCordinate) < 120 or\
                abs(ob5.yCordinate - ob4.yCordinate) < 120 or abs(ob5.yCordinate - ob1.yCordinate) < 120:
            ob5.randomAllocation()

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.carImg = pygame.image.load("sprts.png")   #width = 90 height = 220
        self.width = self.carImg.get_width()
        self.height = self.carImg.get_height()

    def updatePositionOfCar(self):
        gameDis.blit(self.carImg, (self.x, self.y))

    def isCarInFrame(self):
        if self.x > display_width - 104:
            self.x = display_width - 104
        elif self.x < 12:
            self.x = 12

    def isCarCrashingObjects(self, ob1, ob2, ob3, ob4, ob5):
        netScore = 0
        netSafety = 0
        if self.x < ob1.xCordinate + 70 and self.x > ob1.xCordinate - 90 and self.y <= ob1.yCordinate + 50:
            netScore -= 5
            netSafety -= 5
            ob1.yCordinate = 990
        if self.x < ob2.xCordinate + 70 and self.x > ob2.xCordinate - 90 and self.y <= ob2.yCordinate + 50:
            netScore -= 5
            netSafety -= 5
            ob2.yCordinate = 990
        if self.x < ob3.xCordinate + 75 and self.x > ob3.xCordinate - 90 and self.y <= ob3.yCordinate + 55:
            netScore += 5
            ob3.yCordinate = 990
        if self.x < ob4.xCordinate + 70 and self.x > ob4.xCordinate - 90 and self.y <= ob4.yCordinate + 50:
            netScore -= 5
            netSafety -= 5
            ob4.yCordinate = 990
        if self.x < ob5.xCordinate + 70 and self.x > ob5.xCordinate - 90 and self.y <= ob5.yCordinate + 50:
            netScore -= 5
            netSafety -= 5
            ob5.yCordinate = 990

        return netScore, netSafety

            #ob4.yCordinate = 990
    # def isCarCrashingObjects(self, ob1, ob2, ob3, ob4, ob5):
    #     carMask = pygame.mask.from_surface(self.carImg)
    #     ob1Mask = pygame.mask.from_surface(ob1.objImg)
    #     ob2Mask = pygame.mask.from_surface(ob2.objImg)
    #     ob3Mask = pygame.mask.from_surface(ob3.objImg)
    #     ob4Mask = pygame.mask.from_surface(ob4.objImg)
    #     ob5Mask = pygame.mask.from_surface(ob5.objImg)
    #     ob1Offset = (round(self.x) - round(ob1.xCordinate), round(self.y) - round(ob1.yCordinate))
    #     ob2Offset = (round(self.x) - round(ob2.xCordinate), round(self.y) - round(ob2.yCordinate))
    #     ob3Offset = (round(self.x) - round(ob3.xCordinate), round(self.y) - round(ob3.yCordinate))
    #     ob4Offset = (round(self.x) - round(ob4.xCordinate), round(self.y) - round(ob4.yCordinate))
    #     ob5Offset = (round(self.x) - round(ob5.xCordinate), round(self.y) - round(ob5.yCordinate))
    #     ob1pt = carMask.overlap(carMask, ob1Offset)
    #     ob2pt = carMask.overlap(carMask, ob2Offset)
    #     ob3pt = carMask.overlap(carMask, ob3Offset)
    #     ob4pt = carMask.overlap(carMask, ob4Offset)
    #     ob5pt = carMask.overlap(carMask, ob5Offset)
    #     if ob1pt or ob2pt or ob3pt or ob4pt or ob5pt:
    #         return True
    #     return False

class Object:
    def __init__(self, xCordinate, yCordinate, imageFile):
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
        self.objImg = pygame.image.load(imageFile)
        self.width = self.objImg.get_width()
        self.height = self.objImg.get_height()


    def moveObject(self, speed):
        self.yCordinate += speed
        gameDis.blit(self.objImg, (self.xCordinate, self.yCordinate))
        return self.yCordinate

    def randomAllocation(self):                    #allocates random position to obstacles
        xStarting = [22.5, 142.5, 262.5, 382.5, 502.5, 22.5, 142.5, 382.5, 502.5, 262,5]
        yStarting = [-100, -500, -800, -1200, -1800, -2500, -3100, -3800, -4400, -5000]
        self.yCordinate = yStarting[random.randint(0, 7)]
        self.xCordinate = xStarting[random.randint(0, 8)]


def checkSpeed(netScore):              # maintains speed of obstacles during gameplay
    objSpeed = 15
    if netScore > 50 and netScore <= 80:
        objSpeed = 18
    elif netScore > 70 and netScore <= 110:
        objSpeed = 22
    elif netScore > 110 and netScore <= 160:
        objSpeed = 25
    elif netScore > 160 and netScore <= 200:
        objSpeed = 28
    elif netScore > 200 and netScore <= 240:
        objSpeed = 32
    elif netScore > 240 and netScore <= 300:
        objSpeed = 35
    elif netScore > 300:
        objSpeed = 40
    return objSpeed

def startGame():                            # start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDis.fill(black)
        font1 = pygame.font.Font("comic.ttf", 120)                 #designing text and buttons
        font2 = pygame.font.Font("comicbd.ttf", 75)                 #start and quit
        carGame = font1.render("Car Game", True, (60, 230, 250))
        start = font2.render("Start", True, (123, 32, 112))
        quit = font2.render("Quit", True, (123, 32, 112))
        gameDis.blit(carGame, (30, 150))
        gameDis.blit(start, (210, 350))
        gameDis.blit(quit, (225, 470))
        mousePos = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        if 210 < mousePos[0] < 415 and 360 < mousePos[1] < 435:
            start = font2.render("Start", True, (142, 40, 122))
            gameDis.blit(start, (210, 350))
            if mouseClick[0] is 1:
                pass
                score = gameOn()
                return score

        if 220 < mousePos[0] < 390 and 480 < mousePos[1] < 570:
            quit = font2.render("Quit", True, (142, 40, 122))
            gameDis.blit(quit, (225, 470))
            if mouseClick[0] is 1:
                pygame.quit()
                quit()

        pygame.display.update()
        clock1.tick(60)


def gameOn():
    ob1.yCordinate = -100                          #resetting obstacles and car position
    ob2.yCordinate = -100
    ob3.yCordinate = -800
    ob4.yCordinate = -100
    ob5.yCordinate = -100
    ob1.xCordinate = 22.5
    ob2.xCordinate = 142.5
    ob3.xCordinate = 262.5
    ob4.xCordinate = 382.5
    ob5.xCordinate = 502.5
    car.x, car.y = (display_width) * 0.43, (display_height) * 0.75
    # cars = []
    # ge = []
    # nets = []
    # for genomid, g in genomes:
    #     net = neat.nn.FeedForwardNetwork.create(g, config)
    #     nets.append(net)
    #     ge.append(g)
    #     cars.append(Car((display_width) * 0.43, (display_height) * 0.75))
    #     g.fitness = 0

    objSpeed = 20
    x_change = 0
    netScore = 10
    netSafety = 100
    while True:                        # game on loop
        gameDis.fill(grey)
        drawBoundary()
        displayObject(ob1, ob2, ob3, ob4, ob5, objSpeed)
        x_change = eventHandler2nd(x_change)
        for event in pygame.event.get():
            print('mainLoop')
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # for car in cars:
        #     x = cars.index(car)
        #     netSc = car.isCarCrashingObjects(ob1, ob2, ob3, ob4, ob5)
        #     if netSc == -5:
        #         ge[x].fitness -= 0.05
        #         cars.pop(x)
        #         ge.pop(x)
        #         nets.pop(x)
        #     else:
        #         ge[x].fitness += 0.05
        #         output = nets[x].activate((car.x, abs(car.x - ob1.xCordinate), abs(car.x - ob2.xCordinate), abs(car.x - ob4.xCordinate), abs(car.x - ob5.xCordinate), abs(car.x - ob3.yCordinate)))
        #         if output[0] > 0.5:
        #             x_change = 12
        #         if output[1] > 0.5:
        #             x_change = -12
        #         if output[2] > 0.5:
        #             x_change = 0
        car.x += x_change
        score, safety = car.isCarCrashingObjects(ob1, ob2, ob3, ob4, ob5)
        netSafety += safety
        netScore += score
        car.isCarInFrame()
        car.updatePositionOfCar()
        showScore(netScore)
        showSafety(netSafety)
        objSpeed = checkSpeed(netScore)
        if netSafety == 0:
            gameOver(netScore)
            return netScore
        pygame.display.update()
        clock2.tick(60)

def gameOver(netScore):
    while True:
        eventHandler3rd()
        gameDis.fill(grey)
        font1 = pygame.font.Font("comicz.ttf", 80)           # designing text and buttons
        font2 = pygame.font.Font("comici.ttf", 70)
        font3 = pygame.font.Font("comicbd.ttf", 75)
        game = font1.render("GAME OVER", True, cyan)
        yourScore = font2.render("Your Score: " + str(netScore), True, blue)
        continueGame = font3.render("Continue", True, (123, 32, 112))
        quit = font3.render("Quit", True, (123, 32, 112))
        gameDis.blit(game, (50, 200))
        gameDis.blit(yourScore, (40, 350))
        gameDis.blit(continueGame, (150, 500))
        gameDis.blit(quit, (225, 600))

        mousePos = pygame.mouse.get_pos()                   # mouse hover and inputs
        mouseClick = pygame.mouse.get_pressed()
        if 150 < mousePos[0] < 450 and 520 < mousePos[1] < 590:
            continueGame = font3.render("Continue", True, (142, 40, 122))
            gameDis.blit(continueGame, (150, 500))
            if mouseClick[0] is 1:
                score = gameOn()
                return score

        if 230 < mousePos[0] < 385 and 620 < mousePos[1] < 700:
            quit = font3.render("Quit", True, (142, 40, 122))
            gameDis.blit(quit, (225, 600))
            if mouseClick[0] is 1:
                pygame.quit()
                quit()
        pygame.display.update()
        clock3.tick(60)


def showScore(netScore):                                  #display score on gameon Screen
    font = pygame.font.Font("freesansbold.ttf", 22)
    score = font.render("Score: " + str(netScore), True, (0, 0, 0))
    gameDis.blit(score, (10, 10))

def showSafety(netSafety):                                #display car safety on gameon Screen
    font = pygame.font.Font("freesansbold.ttf", 22)
    safety = font.render("Safety: " + str(netSafety) + "%", True, (0, 0, 0))
    gameDis.blit(safety, (440, 10))


# def run(config_file):
#     """
#     runs the NEAT algorithm to train a neural network to play flappy bird.
#     :param config_file: location of config file
#     :return: None
#     """
#     config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                          neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                          config_file)
#
#     # Create the population, which is the top-level object for a NEAT run.
#     p = neat.Population(config)
#
#     # Add a stdout reporter to show progress in the terminal.
#     p.add_reporter(neat.StdOutReporter(True))
#     stats = neat.StatisticsReporter()
#     p.add_reporter(stats)
#
#     # Run for up to 50 generations.
#     winner = p.run(gameOn, 600)
#
#     # show final stats
#     print('\nBest genome:\n{!s}'.format(winner))



display_width = 600
display_height = 900
gameDis = createDisplay(600, display_height, "myGame")
clock1 = pygame.time.Clock()
clock2 = pygame.time.Clock()
clock3 = pygame.time.Clock()
barrier = "box.fw.png"
coin = "ring.fw.png"
cyan = (0, 254, 254)
white = (255, 255, 255)
blue = (0, 0, 244)
black = (0, 0, 0)
grey = (118, 118 , 118)
ob1 = Object(22.5, -100, barrier)
ob2 = Object(142.5, -100, barrier)
ob3 = Object(262.5, -100, coin)
ob4 = Object(382.5, -100, barrier)
ob5 = Object(502.5, -100, barrier)
car = Car((display_width) * 0.43, (display_height) * 0.75)

# if __name__ == '__main__':
#     # Determine path to configuration file. This path manipulation is
#     # here so that the script will run successfully regardless of the
#     # current working directory.
#     local_dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_dir, 'config-feedforeward.txt')
#     run(config_path)

startGame()
pygame.quit()
quit()
