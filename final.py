import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (250, 0, 0)
BOUND = "(0, 162, 232, 255)"
FULL_HEALTH = 100
doorList = pygame.sprite.Group()
world = pygame.sprite.Group()
enemies = pygame.sprite.Group()

        
class door(pygame.sprite.Sprite):
    """ Creates a door to a randomly assigned location """
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("door.jpg").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.location = location

    def update(self, direction):
        if direction == "w":
            self.rect.y += 1
        if direction == "a":
            self.rect.x += 1
        if direction == "s":
            self.rect.y -= 1
        if direction == "d":
            self.rect.x -= 1

    def enter(self, player):
        pygame.sprite.Group.empty(world)
        pygame.sprite.Group.empty(enemies)
        if self.location == "infirmary.jpg":
            room = infirmary()
            world.add(room)
        if self.location == "TelePort.jpg":
            room = teleporter()
            world.add(room)
        if self.location == "temp.jpg":
            enemy1 = enemy(550, 100, player)
            enemy2 = enemy(550, 200, player)
            enemy3 = enemy(550, 300, player)
            enemies.add(enemy1)
            enemies.add(enemy2)
            enemies.add(enemy3)
            world.add(enemy1)
            world.add(enemy2)
            world.add(enemy3)
        if self.location == "armory.jpg":
            room = armory()
            world.add(room)
        try:
            return room
        except:
            return enemy1
            
class character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("child.jpg")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.health = FULL_HEALTH
        self.ammo = 600
        self.hasWeapon = False
        self.dead = False
        self.levelUp = True

    def die(self):
        self.dead = True

    def get_hurt(self):
        self.health -= 100
        if self.health <= 0:
            self.die()

class infirmary(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("health.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300

    def update(self, direction):
        if direction == "w":
            self.rect.y += 1
        if direction == "a":
            self.rect.x += 1
        if direction == "s":
            self.rect.y -= 1
        if direction == "d":
            self.rect.x -= 1

    def reaction(self, player):
        player.health = FULL_HEALTH
        
        
class armory(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("weapon.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300

    def update(self, direction):
        if direction == "w":
            self.rect.y += 1
        if direction == "a":
            self.rect.x += 1
        if direction == "s":
            self.rect.y -= 1
        if direction == "d":
            self.rect.x -= 1

    def reaction(self, player):
        player.hasWeapon = True
        while self.player.ammo < 600 or added < 200:
            player.ammo += 1
            added += 1

class teleporter(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("teleporter.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 300

    def update(self, direction):
        if direction == "w":
            self.rect.y += 1
        if direction == "a":
            self.rect.x += 1
        if direction == "s":
            self.rect.y -= 1
        if direction == "d":
            self.rect.x -= 1

    def reaction(self, player):
        player.levelUp = True

class enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png")
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        

    def update(self, direction):
        if direction == "w":
            self.rect.y += 1
        if direction == "a":
            self.rect.x += 1
        if direction == "s":
            self.rect.y -= 1
        if direction == "d":
            self.rect.x -= 1
            
    def chase(self, image, x, y):
        if x < 0:
            x = x*-1 + self.rect.x
        else:
            x = self.rect.x
        if y < 0:
            y = y*-1 + self.rect.y
        else:
            y = self.rect.y
        North = str(image.get_at((x + 25, y)))
        East = str(image.get_at((x + 50, y + 25)))
        South = str(image.get_at((x + 25,y + 50)))
        West = str(image.get_at((x, y + 25)))
        if self.rect.x > self.player.rect.x:
            if not West == BOUND:
                self.rect.x -= 1
            elif not North == BOUND:
                self.rect.y -= 1
            elif not South == BOUND:
                self.rect.y += 1

        else:
            if not East == BOUND:
                self.rect.x += 1
            elif not South == BOUND:
                self.rect.y += 1
            elif not North == BOUND:
                self.rect.y -= 1

        if self.rect.y > self.player.rect.y:
            if not North == BOUND:
                self.rect.y -= 1
            elif not East == BOUND:
                self.rect.x += 1
            elif not West == BOUND:
                self.rect.x -= 1

        else:
            if not South == BOUND:
                self.rect.y += 1
            elif not West == BOUND:
                self.rect.x -= 1
            elif not East == BOUND:
                self.rect.x += 1

    def reaction(player):
        player.get_hurt()

class Maze(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("map.jpg").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

class main():
    def __init__(self):
        pygame.init()

        screen_width = 640
        screen_height = 480
        screen = pygame.display.set_mode([screen_width, screen_height])

        play = True
        clock = pygame.time.Clock()
        
        #creating a static effect
        overlay = pygame.image.load("overlay.png").convert()
        overlay.set_colorkey(WHITE)

        #center the maze for starting position
        maze = Maze()
        mazePos = maze.image.get_rect().size
        maze.rect.x = screen_width/2 - mazePos[0]/2
        maze.rect.y = screen_height/2 - mazePos[1]/2

        #make it easier to change levels
        background = maze.image
        backgroundX = maze.rect.x
        backgroundY = maze.rect.y

        #center the player
        playerList = pygame.sprite.Group()
        player = character()
        player_pos = player.image.get_rect().size
        player.rect.x = screen_width/2 - player_pos[0]/2
        player.rect.y = screen_height/2 - player_pos[1]/2
        playerList.add(player)

        #set font
        font = pygame.font.SysFont("Times New Roman", 25)
        endFont = pygame.font.SysFont("Times New Roman", 50)
        
        #create doors
        location = ["infirmary.jpg", "temp.jpg", "TelePort.jpg"]
        random.shuffle(location)

        door1 = door(location[0])
        door1.rect.x = screen_width/2 -650
        door1.rect.y = screen_height/2 + 485
        door1.image = pygame.transform.rotate(door1.image, -45)
        doorList.add(door1)
        world.add(door1)

        door2 = door(location[1])
        door2.rect.x = 450
        door2.rect.y = 775
        doorList.add(door2)
        world.add(door2)

        door3 = door(location[2])
        door3.rect.x = -60
        door3.rect.y = -1300
        door3.image = pygame.transform.rotate(door3.image, 10)
        doorList.add(door3)
        world.add(door3)

        mazeEnemy = enemy(0, 0, player)
        enemies.add(mazeEnemy)
        world.add(mazeEnemy)

        level = 0
        speed = 1
        delay = 0
        inRoom = False
        txtDelay = 0

        #play game
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
            
            try:
                screen.fill(BLACK)
                North = str(background.get_at((backgroundX*-1 + 320, backgroundY*-1 + 215)))            
                East = str(background.get_at((backgroundX*-1 + 345, backgroundY*-1 + 240)))
                South = str(background.get_at((backgroundX*-1 + 320, backgroundY*-1 + 265)))
                West = str(background.get_at((backgroundX*-1 + 295, backgroundY*-1 + 240)))
                keys = pygame.key.get_pressed()
                    
                if not North == BOUND and keys[pygame.K_w]:
                    backgroundY += speed
                    world.update("w")
                        
                if not East == BOUND and keys[pygame.K_d]:
                    backgroundX -= speed
                    world.update("d")
                        
                if not South == BOUND and keys[pygame.K_s]:
                    backgroundY -= speed
                    world.update("s")
                        
                if not West == BOUND and keys[pygame.K_a]:
                    backgroundX += speed
                    world.update("a")
            except:
                if backgroundX <= 0:
                    backgroundX += 1
                    world.update("a")
                if backgroundX >= 0:
                    backgroundX -= 1
                    world.update("d")
                if backgroundY <= 0:
                    backgroundY += 1
                    world.update("w")
                if backgroundY >= 0:
                    backgroundY -= 1
                    world.update("s")
            
            
                
            #check if caught by enemies
            if pygame.sprite.spritecollide(player, enemies, False):
                enemy.reaction(player)
                
            #entering room
            if delay == 0:
                if keys[pygame.K_e] and pygame.sprite.spritecollide(player, doorList, False):
                    if not inRoom:
                        #save maze position
                        mazeX = backgroundX
                        mazeY = backgroundY
                        if pygame.sprite.collide_rect(player, door1):
                            background = pygame.image.load(door1.location).convert()
                            obj = door1.enter(player)
                        
                        if pygame.sprite.collide_rect(player, door2):
                            background = pygame.image.load(door2.location).convert()
                            obj = door2.enter(player)
                        
                        if pygame.sprite.collide_rect(player, door3):
                            background = pygame.image.load(door3.location).convert()
                            obj = door3.enter(player)
                        
                        delay = 200
                        pygame.sprite.Group.empty(doorList)
                        background.set_colorkey(WHITE)
                        backgroundX = 0
                        backgroundY = 0
                    
                        escape = door("maze.jpg")
                        escape.rect.x = 4
                        escape.rect.y = 4
                        world.add(escape)
                        doorList.add(escape)
                        inRoom = True

                    if inRoom:
                        #leaving room
                        if pygame.sprite.collide_rect(player, escape):
                            delay = 200
                            background = maze.image
                            backgroundX = mazeX
                            backgroundY = mazeY
                            pygame.sprite.Group.empty(world)
                            pygame.sprite.Group.empty(enemies)
                            world.remove(escape)
                            doorList.remove(escape)
                            doorList.add(door1)
                            doorList.add(door2)
                            doorList.add(door3)
                            world.add(door1)
                            world.add(door2)
                            world.add(door3)
                            try:
                                doorList.add(door4)
                                world.add(door4)
                            except:
                                pass
                            world.add(mazeEnemy)
                            enemies.add(mazeEnemy)
                            inRoom = False
                
                if keys[pygame.K_c] and pygame.sprite.collide_rect(player, obj):
                    obj.reaction(player)
                    delay = 200
                    world.remove(obj)
                    
                        
            else:
                delay -= 1

            for i in enemies:
                i.chase(background, backgroundX, backgroundY)
            screen.blit(background, [backgroundX, backgroundY])
            world.draw(screen)
            screen.blit(player.image, [player.rect.x, player.rect.y])
            if not inRoom:
                overX = random.randint(-10, 0)
                overY = random.randint(-10, 0)
                screen.blit(overlay, [overX, overY])
            healthLbl = font.render("Health: " + str(player.health), 1, WHITE)
            screen.blit(healthLbl, [0, screen_height - 25])
            if player.hasWeapon:
                ammoLbl = font.render("Ammo: " + str(player.ammo), 1, WHITE)
                screen.blit(ammoLbl, [screen_width - 125, screen_height - 25])
            if player.levelUp:
                player.levelUp = False
                txtDelay = 100
                level += 1
                levelUpTxt = endFont.render("Level " + str(level), 1, RED)

            if not txtDelay <= 0:
                txtDelay -= 1
                screen.blit(levelUpTxt, [screen_width/2 - 100, screen_height/2 -25])
            if player.dead:
                play = False
                end = endFont.render("Game Over", 1, RED)
                screen.blit(end, [screen_width/2 - 100, screen_height/2 -25])
            
            pygame.display.flip()

main()

