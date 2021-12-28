####################################################################
#################################################################### 초기 설정

import pygame, sys, random, time
from pygame.locals import *

pygame.init() #파이게임 초기화

#화면 크기 설정
screen_width = 1920 # 가로크기
screen_height = 1080 # 세로크기
RGB = ((22, 255, 255))
RGB2 = ((0,255,0))
RGB3 = ((114,255,92))

#게임 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#게임이름
pygame.display.set_caption("누가 내 물고기 다 가져갔어?")

#FPS
clock = pygame.time.Clock()

#각종 이미지 불러오기
# 오프닝1 ######################################
opening_background_image = pygame.image.load("images/opening_background.png").convert()
opening_background_image.set_colorkey(RGB3)
opening_character_back_image = pygame.image.load("images/opening_character_back.png").convert()
opening_character_back_image.set_colorkey(RGB3)
opening_character_angry_image = pygame.image.load("images/opening_character_angry.png").convert()
opening_character_angry_image.set_colorkey(RGB3)
opening_bucket_image = pygame.image.load("images/opening_bucket.png").convert()
opening_bucket_image.set_colorkey(RGB3)

# 펭귄1 ########################################
penguinR_image = [pygame.image.load("images/penguinR/1.png").convert(),
                     pygame.image.load("images/penguinR/2.png").convert(),
                     pygame.image.load("images/penguinR/3.png").convert(),
                     pygame.image.load("images/penguinR/4.png").convert(),
                     pygame.image.load("images/penguinR/5.png").convert()]
                     
penguinL_image = [pygame.image.load("images/penguinL/1.png").convert(),
                     pygame.image.load("images/penguinL/2.png").convert(),
                     pygame.image.load("images/penguinL/3.png").convert(),
                     pygame.image.load("images/penguinL/4.png").convert(),
                     pygame.image.load("images/penguinL/5.png").convert()]

for i in range(5) :
    penguinR_image[i] = pygame.transform.scale(penguinR_image[i], (125, 200))
    penguinR_image[i].set_colorkey(RGB3)
    penguinL_image[i] = pygame.transform.scale(penguinL_image[i], (125, 200))
    penguinL_image[i].set_colorkey(RGB3)

###############################################

# 보스1 #######################################
bossPenguin_image = pygame.image.load("images/bossPenguin_stay.png").convert()
bossPenguin_attack_image = pygame.image.load("images/bossPenguin_attack.png").convert()

bossPenguin_image = pygame.transform.scale(bossPenguin_image, (470, 750))
bossPenguin_attack_image = pygame.transform.scale(bossPenguin_attack_image, (470, 750))

# UI1 #########################################
# 충돌7 #####################################################################
heart_images = [pygame.image.load("images/heart/heart_1.png").convert(),
                pygame.image.load("images/heart/heart_2.png").convert(),
                pygame.image.load("images/heart/heart_3.png").convert(),
                pygame.image.load("images/heart/heart_4.png").convert()]
#############################################################################
water_images = [pygame.image.load("images/water/water_FULL.png").convert()]

for i in range(len(heart_images)) :
    heart_images[i] = pygame.transform.scale(heart_images[i], (120, 120))

heart_image = heart_images[0]
water_image = water_images[0]
###############################################
homescreen_image = pygame.image.load('images/homescreen.png').convert()

clearscreen_image = pygame.image.load('images/clear.png').convert()
howtoplay_image = pygame.image.load('images/How_to_play.png').convert()

start_image = pygame.image.load('images/start.png').convert()
start_image.set_colorkey(RGB2)
start_rect = start_image.get_rect()

end_image = pygame.image.load('images/end.png').convert()
end_image.set_colorkey(RGB2)
end_rect = end_image.get_rect()

replay_image = pygame.image.load('images/replay.png').convert()
replay_rect = replay_image.get_rect()

how_to_butten_image = pygame.image.load('images/how_to_butten.png').convert()
how_to_butten_rect = how_to_butten_image.get_rect()

badguy_image = pygame.image.load('images/E_missile.png').convert()
badguy_image.set_colorkey((255, 255, 255))

boss_small_missile = pygame.image.load('images/B_missile.png').convert()
boss_small_missile.set_colorkey((255, 255, 255))

boss_missile_image = pygame.image.load('images/boss_missile.png').convert()
boss_missile_image.set_colorkey((255, 255, 255))

enemy_image = pygame.image.load('images/vhxkq.png').convert()
enemy_image.set_colorkey((0, 0, 0))

boss_image = pygame.image.load('images/boss.png').convert()
boss_image.set_colorkey((255, 255, 255))

wall_normal = pygame.image.load('images/tile_middle.png').convert()
wall_normal2 = pygame.image.load('images/tile_middle2.png').convert()

wall_broken = pygame.image.load('images/wall_broken.png').convert()
wall_broken.set_colorkey((255, 255, 255))

newcharacter_image = pygame.image.load('images/new_character.png').convert()
newcharacter_image.set_colorkey(RGB)
newcharacter_size = newcharacter_image.get_rect().size
newcharacter_width = newcharacter_size[0]
newcharacter_height = newcharacter_size[1]

character_image = pygame.image.load('images/new_character.png').convert()
character_image.set_colorkey(RGB)
character_size = character_image.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character2_image = pygame.image.load('images/new_character.png').convert()
character2_image.set_colorkey(RGB)
character2_size = character_image.get_rect().size
character2_width = character_size[0]
character2_height = character_size[1]
last = character_image

character_attack_image = pygame.image.load('images/new_character.png').convert()
character_attack_image.set_colorkey(RGB)
character_attack_size = character_image.get_rect().size
character_attack_width = character_size[0]
character_attack__height = character_size[1]

character2_attack_image = pygame.image.load('images/new_character.png').convert()
character2_attack_image.set_colorkey(RGB)
character2_attack_size = character_image.get_rect().size
character2_attack_width = character_size[0]
character2_attack__height = character_size[1]

character_image_walk_1 = pygame.image.load('images/new_character.png').convert()
character_image_walk_1.set_colorkey(RGB)
character_image_walk_2 = pygame.image.load('images/new_character.png').convert()
character_image_walk_2.set_colorkey(RGB)
character_image_walk_1R = pygame.image.load('images/new_character.png').convert()
character_image_walk_1R.set_colorkey(RGB)
character_image_walk_2R = pygame.image.load('images/new_character.png').convert()
character_image_walk_2R.set_colorkey(RGB)

theif_image = pygame.image.load('images/Enemy.png').convert()
theif_image.set_colorkey((114, 255, 92))
theif_size = theif_image.get_rect().size
theif_width = character_size[0]
theif__height = character_size[1]

theif_image2 = pygame.image.load('images/Enemy_left.png').convert()
theif_image2.set_colorkey((114, 255, 92))
theif2_size = theif_image.get_rect().size
theif2_width = character_size[0]
theif2__height = character_size[1]

theif_attack_image = pygame.image.load('images/Enemy_attack.png').convert()
theif_attack_image.set_colorkey((0, 255, 0))

theif_attack_image2 = pygame.image.load('images/Enemy2_attack.png').convert()
theif_attack_image2.set_colorkey((0, 255, 0))

missile_image = pygame.image.load('images/missile.png').convert()
missile_image.set_colorkey((255, 255, 255))

portal_image = pygame.image.load('images/portal.png').convert()
portal_image.set_colorkey(RGB2)
un_portal_image = pygame.image.load('images/un_act_portal.png').convert()
un_portal_image.set_colorkey(RGB2)
boss_portal_image = pygame.image.load('images/boss_portal.png').convert()
boss_portal_image.set_colorkey(RGB2)

textbox_image = pygame.image.load('images/conText.png').convert()

textbox_image2 = pygame.image.load('images/conText2.png').convert()

textbox_image3 = pygame.image.load('images/conText3.png').convert()

textbox_image4 = pygame.image.load('images/conText4.png').convert()

textboxs_guide1 = pygame.image.load('images/Text.png').convert()

textboxs_guide2 = pygame.image.load('images/Text2.png').convert()

textboxs_guide3 = pygame.image.load('images/Text3.png').convert()

treasure_image = pygame.image.load('images/tkdwk.png').convert()
treasure_image.set_colorkey((0, 0, 0))

cave_trash_image = pygame.image.load('images/cave_trash.png').convert()
cave_trash_image.set_colorkey((255, 255, 255))

cave_trash2_image = pygame.image.load('images/cave_trash2.png').convert()
cave_trash2_image.set_colorkey((255, 255, 255))

space_trash_image = pygame.image.load('images/space_trash.png').convert()
space_trash_image.set_colorkey((255, 255, 255))

space_trash2_image = pygame.image.load('images/space_trash2.png').convert()
space_trash2_image.set_colorkey((255, 255, 255))

stage_museum = pygame.image.load('images/museum_ring.png').convert()
stage_museum_ring = pygame.image.load('images/museum_ring.png').convert()
stage_museum_no_ring = pygame.image.load('images/museum_ring.png').convert()
stage_cave = pygame.image.load('images/museum_ring.png').convert()
stage_broken_museum = pygame.image.load('images/museum_ring.png').convert()
stage_space = pygame.image.load('images/museum_ring.png').convert()
clear_News = pygame.image.load('images/museum_ring.png').convert()
bad_News = pygame.image.load('images/museum_ring.png').convert()
Main_Buttun = pygame.image.load('images/museum_ring.png').convert()
Main_Buttun_rect = Main_Buttun.get_rect()

################################################################## 쌔삥

playerTextureDefault=pygame.image.load('images/주인공_대기.png').convert() #오른방향 기본자세
playerTextureDefault.set_colorkey(RGB3)

LplayerTextureDefault=pygame.image.load('images/주인공_대기_반전.png').convert() #왼방향 기본자세
LplayerTextureDefault.set_colorkey(RGB3)

playerTexture=pygame.image.load('images/주인공_대기.png').convert()
playerTexture.set_colorkey(RGB3)

playerWalk1=pygame.image.load('images/player_walk_1.png').convert() #오른쪽 걷기
playerWalk1.set_colorkey(RGB3)
playerWalk2=pygame.image.load('images/player_walk_2.png').convert()
playerWalk2.set_colorkey(RGB3)
playerWalk3=pygame.image.load('images/player_walk_3.png').convert()
playerWalk3.set_colorkey(RGB3)
playerWalk4=pygame.image.load('images/player_walk_4.png').convert() #오른쪽 걷기
playerWalk4.set_colorkey(RGB3)
playerWalk5=pygame.image.load('images/player_walk_5.png').convert()
playerWalk5.set_colorkey(RGB3)


LplayerWalk1=pygame.image.load('images/주인공_1_반전.png').convert() #왼쪽 걷기
LplayerWalk1.set_colorkey(RGB3)

LplayerWalk2=pygame.image.load('images/주인공_2_반전.png').convert()
LplayerWalk2.set_colorkey(RGB3)

LplayerWalk3=pygame.image.load('images/주인공_3_반전.png').convert()
LplayerWalk3.set_colorkey(RGB3)

LplayerWalk4=pygame.image.load('images/주인공_4_반전.png').convert()
LplayerWalk4.set_colorkey(RGB3)

LplayerWalk5=pygame.image.load('images/주인공_5_반전.png').convert()
LplayerWalk5.set_colorkey(RGB3)

playerJump1=pygame.image.load('images/주인공_점프.png').convert() #오른쪽 점프
playerJump1.set_colorkey(RGB3)

playerJump2=pygame.image.load('images/주인공_점프.png').convert()
playerJump2.set_colorkey(RGB3)

playerJump3=pygame.image.load('images/주인공_점프.png').convert()
playerJump3.set_colorkey(RGB3)

LplayerJump1=pygame.image.load('images/주인공_점프_반전.png').convert() #왼쪽 점프
LplayerJump1.set_colorkey(RGB3)

LplayerJump2=pygame.image.load('images/주인공_점프_반전.png').convert()
LplayerJump2.set_colorkey(RGB3)

LplayerJump3=pygame.image.load('images/주인공_점프_반전.png').convert()
LplayerJump3.set_colorkey(RGB3)

playerAttack1=pygame.image.load('images/주인공_공격1.png').convert() #오른쪽 공격
playerAttack1.set_colorkey(RGB3)

playerAttack2=pygame.image.load('images/주인공_공격2.png').convert()
playerAttack2.set_colorkey(RGB3)

playerAttack3=pygame.image.load('images/주인공_공격3.png').convert()
playerAttack3.set_colorkey(RGB3)

LplayerAttack1=pygame.image.load('images/주인공_공격1_반전.png').convert() #왼쪽 공격
LplayerAttack1.set_colorkey(RGB3)

LplayerAttack2=pygame.image.load('images/주인공_공격2_반전.png').convert()
LplayerAttack2.set_colorkey(RGB3)

LplayerAttack3=pygame.image.load('images/주인공_공격3_반전.png').convert()
LplayerAttack3.set_colorkey(RGB3)

GAME_OVER = pygame.image.load('images/gameover.png').convert()

isWalk=False #뭔 행동을 하는지 판단

isJump=False

isAttack=False

walkAniTimer=0 #스프라이트 재생 타이머
jumpAniTimer=0
attackAniTimer=0

isplayerRight=True #오른쪽을 바라보고 있는지

#폰트들 설정
font = pygame.font.Font(None, 15)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 50)

#변수들 초기화
stage = 0
stop = 0
rewards = 0
high_score = 0
mapcounter = 1 #스테이지가 계속 호출되는 것을 막기 위한 변수
last_trash_spawn_time = 0
backCount = 0
# 오프닝6 #####
mapcounter = 2 #스테이지가 계속 호출되는 것을 막기 위한 변수
###############

# 투사체 발사 관련
ggg = 0
fff = 0
ddd = 0.9

missile_speed = 10 #캐릭터 샷스피드
e_missile_speed = 8 #포탑 샷스피드
fire_range = 50 #포탑 공격 사거리

#사운드 불러오기
shot_sound = pygame.mixer.Sound('sounds/휘두르는소리.wav')
walk_sound = pygame.mixer.Sound('sounds/걷는소리.wav')
broken_sound = pygame.mixer.Sound('sounds/깨지는소리.wav')
treasure_sound = pygame.mixer.Sound('sounds/treasure.wav')
portal_sound = pygame.mixer.Sound('sounds/portal.wav')
stage_music = pygame.mixer.Sound('sounds/stage_music.wav')
clear_sound = pygame.mixer.Sound('sounds/clear_sound.wav')

####################################################################
#################################################################### 클래스

class Character: #플레이어 클래스
    def __init__(self):
        # 초기 위치
        self.x = 130
        self.y = screen_height - 360

        self.switch = False
        self.backCount = 0
        
        self.dx = 0
        self.dy = 0
        self.range = 0
        self.stop = 0.0
        self.isJump = 0
        self.v = 1 # 속도
        self.m = 1  # 질량
        self.lastInput = 0 #벽에 닿기 직전 사용자가 어떤 방향키를 누르고 벽에 닿았는지 좌우상하 순으로 1, 2, 3, 4로 저장
        self.canMove_L = True #추가
        self.canMove_R = True #추가
        self.canMove_U = True #추가
        self.canMove_D = True #추가

        self.rect = pygame.Rect(self.x, self.y, 125, 200)
        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 200
        self.right = self.x + 125

        self.attac_speed = 0.6 #캐릭터 공격 속도(작을 수록 빨라짐)
        self.character_speed = 5 #캐릭터 이동 속도(클 수록 빨라짐)
        self.damage = 0 #캐릭터 공격 추가 데미지(클 수록 강해짐)
        self.hp = 3 #캐릭터 체력

        self.last_time = time.time()
        self.punch_time = time.time()-5

        # 충돌2 #################################
        self.rect = character_image.get_rect()
        self.height = 128
        self.width = 128

    def collision_check(self, penguin_rect) :
        if self.rect.top < penguin_rect.bottom and penguin_rect.top < self.rect.bottom and self.rect.left < penguin_rect.right and penguin_rect.left < self.rect.right :
            return True
        else :
            return False
        #########################################

    def respawn(self): #플레이어 리스폰 위치(오른쪽으로 이동했을 때)
        self.x = 130
        self.y = screen_height - 360
        self.range = 0

    def respawn2(self): #플레이어 리스폰 위치(우주 그림에서 나왔을 떄)
        self.x = 800
        self.y = screen_height - 360
        self.range = 0

    def move(self, walls): #플레이어 이동 함수 + 벽을 지나갈 수 없게 하는 함수
        # 충돌3 #####################################
        self.rect.left = self.x
        self.rect.top = self.y
        self.rect.right = self.x + self.width
        self.rect.bottom = self.y + self.height
        #############################################
        self.character_rect = pygame.Rect(self.x, self.y, 125, 200) ##추가
        ##이 부분부터 판정 알고리즘 수정
        wallCount = 0
        if(stage >= 1):
            for wallCount in range(len(walls)):
                character.check()

                if walls[wallCount].top <= character.bottom and walls[wallCount].bottom >= character.bottom and character.right > walls[wallCount].left and character.left < walls[wallCount].right:
                    self.canMove_R = True
                    self.canMove_L = True
                    self.canMove_U = True
                    self.canMove_D = False
                    character.y = walls[wallCount].top - 200
                    break

                elif walls[wallCount].right >= character.left and walls[wallCount].left < character.left and (walls[wallCount].top  < character.bottom or walls[wallCount].bottom  < character.top):
                    self.canMove_R = True
                    self.canMove_L = False
                    self.canMove_U = False
                    self.canMove_D = True
                    break
                    

                elif walls[wallCount].left <= character.right and walls[wallCount].right > character.right and (walls[wallCount].top  < character.bottom or walls[wallCount].bottom  < character.top):
                    self.canMove_R = False
                    self.canMove_L = True
                    self.canMove_U = False
                    self.canMove_D = True
                    break
                    
                else:
                    self.canMove_R = True
                    self.canMove_L = True
                    self.canMove_U = True
                    self.canMove_D = True

                
        if len(walls) == 0: # 마지막 벽이 깨질 때 벽에 붙어 있으면 이후 위의 for문이 안돌아 다시 self.canMove를 True로 돌리는 코드가 없었음, 또 다른 버그 생길 수도 있음
            self.canMove_L = True
            self.canMove_R = True
            self.canMove_U = True
            self.canMove_D = True
        #여기까지 판단 알고리즘

        
        if pressed_keys[K_LEFT] and self.x > 0 and self.canMove_L == True: #세번째 조건 바뀜
            if istext_on == False:

                self.x -= self.character_speed
                self.bottom = self.y + 200
                self.right = self.x + 125
                self.lastInput = 1

                if (time.time() - self.stop)>0.4:
                    pygame.mixer.Sound.play(walk_sound)
                    self.stop = time.time()
            
        if pressed_keys[K_RIGHT] and self.x < 1920 and self.canMove_R == True:
            if istext_on == False:
                self.range = 0
                
                self.x += self.character_speed
                self.bottom = self.y + 200
                self.right = self.x + 125
                self.lastInput = 2 # 마지막으로 누른 키가 오른쪽이면 2번을 저장시킴

                if (time.time() - self.stop)>0.4:
                    pygame.mixer.Sound.play(walk_sound)
                    self.stop = time.time()

        if pressed_keys[K_LALT] and self.canMove_U == True:
            if istext_on == False:
                self.lastInput = 3

                if character.isJump == 2:
                    character.jump(1)
                    
                if character.isJump == 0:
                    character.jump(1)
                    
                elif character.isJump == 1:
                    character.jump(2)
    
    def jump(self, j):
        self.isJump = j

    def update(self):
        wallCount = 0
        if(stage >= 1):
            for wallCount in range(len(walls)):
                if ((character.top < walls[wallCount].bottom) and (walls[wallCount].top < character.bottom)) and ((character.left < walls[wallCount].right) and (walls[wallCount].left < character.right)):
                    self.canMove_D = False
                    break
                else:
                    self.canMove_D = True

        # isJump 값이 0보다 큰지 확인
        if self.isJump > 0:

            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                F = (0.5 * self.m * (self.v * self.v))
                
            elif self.v <= 0:
                # 속도가 0보다 작을때는 아래로 내려감
                F = -(0.5 * self.m * (self.v * self.v))

            # 좌표 수정 : 위로 올라가기 위해서는 y 좌표를 줄여준다.
            self.y -= round(F)
            self.bottom = self.y + 200
            self.right = self.x + 125

            # 속도 줄여줌
            self.v -= 0.2

            # 바닥에 닿았을때, 변수 리셋
            if self.y > screen_height - 360 and self.canMove_D == True:
                self.y = screen_height - 360
                self.isJump = 0

                if self.y != screen_height - 360 and self.canMove_D == True and self.isJump == 0:
                    pass

                else: 
                    self.v = 7

            elif self.canMove_D == False:
                self.isJump = 0
                self.v = 7

    def check(self):
        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 200
        self.right = self.x + 125


    def draw(self):
        screen.blit(playerTexture, (self.x, self.y))
    
    def fire(self): #미사일 발사(총구의 방향에서 발사되게 조정해놓음)
        if self.range == 0:
            missiles.append(Missile(self.x + 84, self.y + 64, self.range))

        if self.range == 180:
            missiles.append(Missile(self.x+20, self.y + 64, self.range))

class Theif:
    def __init__(self,t):
        if stage <= 1:
            self.x = 1500
            self.y = screen_height - 300
            self.hp = 9999
        if stage == 2:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 9999
        if stage == 3:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        if stage == 6:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        if stage == 7:
            self.x = 1900
            self.y = screen_height - 300
            self.hp = 10
        self.t = t

    def stage1_move(self):
        self.x += 18

    def stage2_move(self):
        self.y -= 18

    def stage3_move(self,x):
        self.x = x
        self.x += 18

    def draw(self):
        if self.t == "attack":
            screen.blit(theif_attack_image, (self.x, self.y))
        else:
            screen.blit(theif_image, (self.x, self.y))

    def draw2(self):
        if self.t == 'attack':
            screen.blit(theif_attack_image2, (self.x, self.y))
        else:
            screen.blit(theif_image2, (self.x, self.y))
    
    def hit(self, missiles): #도둑 피격 판정
        return self.y < missiles.y + 26 and missiles.y < self.y + 128 and self.x < missiles.x + 8 and missiles.x < self.x + 128

    def fire(self): #십자방향으로 포탑 총알 발사
        if character.x > self.x:
            badguys.append(Badguy_Left(self.x + 80, self.y + 40))
        else:
            badguys.append(Badguy_Right(self.x + 25, self.y + 40))

class Missile: # 미사일 클래스
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def move(self):
        if self.r == 0:
            self.x += missile_speed # 총알 샷스피드가 높을수록 미사일의 샷스피드가 빨라짐

        if self.r == 180:
            self.x -= missile_speed

    def off_screen(self): #총알이 화면을 벗어났을 때 없애주는 함수
        if (self.x < character.x - 80): #여기 상수항이 사정거리
            return True
        if (self.x > character.x + 190):
            return True

    def draw(self):
        
        if self.r == 0:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 180:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 90:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

        if self.r == 270:
            rotated = pygame.transform.rotate(missile_image, self.r)
            screen.blit(rotated, (self.x, self.y))

class Cave_Trash:
    def __init__(self):
        self.x = random.randint(50, 1870)
        self.y = -100
        self.dy = random.randint(2, 6)
        self.rr = random.randint(1,2)

    def move(self):
        self.dy += 0.1
        self.y += self.dy # 배드가이의 움직임
             
    def draw(self):
        if self.rr == 1:
            screen.blit(cave_trash_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(cave_trash2_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.y > 1200) # 화면을 넘어갔을 때

    def touching(self, missile):
        self.cave_trach_rect = pygame.Rect(self.x, self.y, 80, 200) ##추가
        return self.cave_trach_rect.colliderect(missile.character_rect)##추가

class Space_Trash:
    def __init__(self):
        self.x = 2000
        self.y =  random.randint(50, 1030)
        self.rr = random.randint(1,2)
        self.dx = random.choice((2, 6))

    def move(self):
        self.dx += 0.1
        self.x -= self.dx # 배드가이의 움직임
             
    def draw(self):
        if self.rr == 1:
            screen.blit(space_trash_image, (self.x, self.y)) # 그리기
        if self.rr == 2:
            screen.blit(space_trash2_image, (self.x, self.y)) # 그리기

    def off_screen(self):
        return (self.x < -200) # 화면을 넘어갔을 때

    def touching(self, missile):
        self.space_trach_rect = pygame.Rect(self.x, self.y, 80, 80) ##추가
        return self.space_trach_rect.colliderect(missile.character_rect)##추가

class TextBox:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def draw(self):
        if self.t == "one":
            screen.blit(textbox_image, (self.x, self.y))
        if self.t == "two":
            screen.blit(textbox_image2, (self.x, self.y))
        if self.t == "three":
            screen.blit(textbox_image3, (self.x, self.y))
        if self.t == "four":
            screen.blit(textbox_image4, (self.x, self.y))

class Wall: #벽 클래스
    def __init__(self, x, y, b_type):
        self.x = x
        self.y = y
        self.hp = stage * 6
        
        if (b_type == "normal"):
            self.wall_state = wall_normal #기본은 기본 벽 텍스처

        elif (b_type == "under"):
            self.wall_state = wall_normal2 #기본은 기본 벽 텍스처

        self.wall_rect = pygame.Rect(self.x, self.y, 80, 80) #벽 범위
        self.top = self.y
        self.left = self.x
        self.bottom = self.y + 80
        self.right = self.x + 80

    def draw(self):
        screen.blit(self.wall_state, (self.x, self.y))

    def hit(self, missiles): #벽 피격 판정(미사일: 10*32, 벽: 40*40)
        if missiles.r == 0:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 180:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 90:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40
        if missiles.r == 270:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40

class Enemy: #포탑 클래스
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = stage
        self.last_badguy_spawn_time = time.time() 

    def draw(self):
        screen.blit(enemy_image, (self.x, self.y))

    def hit(self, missiles): #벽 피격 판정(미사일: 10*32, 포탑: 40*40)
        if missiles.r == 0:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 180:
            return self.y < missiles.y + 26 and missiles.y < self.y + 40 and self.x < missiles.x + 8 and missiles.x < self.x + 40
        if missiles.r == 90:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40
        if missiles.r == 270:
            return self.y < missiles.y + 8 and missiles.y < self.y + 40 and self.x < missiles.x + 26 and missiles.x < self.x + 40

    def fire(self): #십자방향으로 포탑 총알 발사
        badguys.append(Badguy_Down(self.x + 8, self.y + 5))
        badguys.append(Badguy_Up(self.x + 8, self.y + 15))
        badguys.append(Badguy_Left(self.x + 5, self.y + 8))
        badguys.append(Badguy_Right(self.x + 15, self.y + 8))

class Boss_Down1: #보스 미사일 큰거
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(boss_missile_image, (self.x, self.y))

    def off_screen(self):
        if (self.y < -800):
            return True
        elif (self.y > 728):
            return True
        elif (self.x < -800):
            return True
        elif (self.x > 1288):
            return True

    def touching_c(self, caracter): #캐릭터와 충돌했을 떄
        return self.y + 40 < caracter.y + 40 and caracter.y < self.y + 180 and self.x + 40 < caracter.x + 30 and caracter.x < self.x + 220

class Boss_small_Down1: #보스 미사일 작은거
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(boss_small_missile, (self.x, self.y))

    def off_screen(self):
        if (self.y < -800):
            return True
        elif (self.y > 728):
            return True
        elif (self.x < -800):
            return True
        elif (self.x > 1288):
            return True

    def touching_c(self, caracter):
        return self.y < caracter.y + 40 and caracter.y < self.y + 25 and self.x - 10 < caracter.x + 30 and caracter.x < self.x + 35

class Badguy_Down: #포탑 미사일(아래 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y += e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles): #내 캐릭터의 미사일에 닿았을 때
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        return self.y < caracter.y + 40 and caracter.y < self.y + 25 and self.x < caracter.x + 30 and caracter.x < self.x + 25

class Badguy_Up: #포탑 미사일(위 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.y -= e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        return self.y < caracter.y + 30 and caracter.y < self.y + 25 and self.x < caracter.x + 30 and caracter.x < self.x + 25

class Badguy_Left: #포탑 미사일(왼쪽 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.x += e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        self.badguy_L_rect = pygame.Rect(self.x, self.y, 45, 45) ##추가
        return self.badguy_L_rect.colliderect(caracter.character_rect)##추가

class Badguy_Right: #포탑 미사일(오른쪽 방향)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 0

    def move(self):
        self.x -= e_missile_speed
             
    def draw(self):
        screen.blit(badguy_image, (self.x, self.y))

    def off_screen(self):
        if (self.x < -100):
            return True
        elif (self.x > 2100):
            return True

    def touching_m(self, missiles):
        return self.y < missiles.y + 26 and missiles.y < self.y + 25 and self.x < missiles.x + 8 and missiles.x < self.x + 25

    def touching_c(self, caracter):
        self.badguy_R_rect = pygame.Rect(self.x, self.y, 45, 45) ##추가
        return self.badguy_R_rect.colliderect(caracter.character_rect)##추가


class Stage: #스테이지 클래스
    def __init__(self):
        self.x = 0
        self.y = 0

    def homescreen(self): #게임 메인화면(시작화면)
        screen.blit(homescreen_image, (self.x, self.y))
        Button(start_image,1500,200,300,150,start_image,1500,200,'start')
        Button(end_image,1500,420,300,150,end_image,1500,420,'end')

    def clearscreen(self): #게임 클리어 화면
        screen.blit(clearscreen_image, (self.x, self.y))
        Button(replay_image,210,300,313,97,replay_image,210,300,'replay')
        Button(end_image,780,520,313,97,end_image,780,520,'end')

    #스테이지 편하게 만들기 위한 함수들
    def makeWall_garo(self, x, y, i, b_type):
        for z in range (0, i + 1):   
            walls.append(Wall(x + 80 * z, y, b_type))

    def makeWall_sero(self, x, y, i, b_type):
        for z in range (0, i+1):   
            walls.append(Wall(x, y - 80 * z, b_type))

    #각 스테이지들에서의 오브젝트 배치

    def stage1(self):
        screen.blit(stage_museum, (0, 0))
        textboxs.append(TextBox(1400,620,"one"))
        textboxs.append(TextBox(30,620,"two"))

    def stage2(self):
        # 오프닝5 ##############################
        #screen.blit(stage_museum_ring, (0, 0))
        screen.blit(opening_background_image, (0, 0))
        ########################################

    def stage3(self):
        pass

    def stage4(self):
        pass
        
    def stage5(self):
        pass

    def stage6(self):
        pass     

    def stage7(self):
        textboxs.append(TextBox(1400,620,"three"))
        textboxs.append(TextBox(720,620,"four"))
    def stage8(self):
        pass

    def stage9(self):
        pass

    def stage10(self):
        pass

class Button: #버튼 클래스
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, type):
        mouse = pygame.mouse.get_pos()

        if type == 'start':
            start_rect.left = x
            start_rect.top = y

        elif type == 'end':
            end_rect.left = x
            end_rect.top = y

        elif type == 'replay':
            Main_Buttun_rect.left = x
            Main_Buttun_rect.top = y

        elif type == 'howto':
            how_to_butten_rect.left = x
            how_to_butten_rect.top = y

        if x + width > mouse[0] > x and y + height > mouse[1] > y: #이미지 위에 마우스를 올리면 이미지 좌표 바꿔주기
            screen.blit(img_act,(x_act, y_act))

        else:
            screen.blit(img_in,(x,y))

# 오프닝11 ##################################################3
class Opening_Character :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

        self.stay_time = 0
        self.time_flg = True

    def move(self) :
        if self.time_flg :
            self.stay_time = time.time()
            self.time_flg = False
        else :
            if (time.time() - self.stay_time >= 2) :
                self.x += 20
    def draw(self) :
        screen.blit(opening_character_angry_image, (self.x, self.y))

# 펭귄2 #######################################################################
class Penguin:
    def __init__(self, x, y):   # x, y는 펭귄 초기 위치
        
        # 펭귄 크기
        self.width = 125
        self.height = 200

        # 펭귄 위치
        self.x = x
        self.y = y

        # 펭귄 방향
        self.image_time = time.time()
        self.image_num = 0
        self.penguin_image = penguinL_image[self.image_num]
        self.isLeft = True
        self.isRight = False

        # 펭귄 렉트값 (지금은 안 씀)
        self.penguin_rect = self.penguin_image.get_rect()
        self.penguin_rect.left = self.x
        self.penguin_rect.top = self.y

        # 펭귄 속도
        self.speed = 5

        # 펭귄 HP
        self.hp = 1

    # 오프닝10 ###################################################
        self.opening_speed = 2
    def opening_move(self) :
        if (self.isLeft and self.x <= 555) :
            self.opening_speed = 10
            self.isLeft = False
            self.isRight = True
            self.image_num = 0
            self.image_time = time.time()
        elif (self.isRight and self.x >= 1920) :
            self.isLeft = True
            self.isRight = False
            self.image_num = 0
            self.image_time = time.time()
        if (self.isLeft) :
            self.x -= self.opening_speed
        elif(self.isRight) :
            self.x += self.opening_speed
    ##############################################################

    def move(self, min_x, max_x) :    # 이동 범위: min_x ~ max_x
        # 충돌1 ##########################################
        self.penguin_rect.left = self.x
        self.penguin_rect.top = self.y
        self.penguin_rect.right = self.x + self.width
        self.penguin_rect.bottom = self.y + self.height
        ##################################################
        # 펭귄 범위 한정(710~1210), 방향 전환
        if (self.isLeft and self.x <= min_x) :
            self.isLeft = False
            self.isRight = True
            self.image_num = 0
            self.image_time = time.time()
        elif (self.isRight and self.x + self.width >= max_x) :
            self.isLeft = True
            self.isRight = False
            self.image_num = 0
            self.image_time = time.time()

        # 펭귄 이동
        if (self.isLeft) :
            self.x -= self.speed
        elif (self.isRight) :
            self.x += self.speed

    def draw(self):
        # 애니메이션
        if (self.isLeft and time.time() - self.image_time >= 0.05) :  # 오른쪽
            if (self.image_num < 4) :
                self.image_num += 1
            else :
                self.image_num = 0
            self.penguin_image = penguinL_image[self.image_num]
            self.image_time = time.time()
        elif (self.isRight and time.time() - self.image_time >= 0.05) :  # 오른쪽
            if (self.image_num < 4) :
                self.image_num += 1
            else :
                self.image_num = 0
            self.penguin_image = penguinR_image[self.image_num]
            self.image_time = time.time()
        # 그리기
        screen.blit(self.penguin_image, (self.x, self.y))

    def hit(self, missiles) :
        return self.y < missiles.y + 26 and missiles.y < self.y + self.height and self.x < missiles.x + 8 and missiles.x < self.x + self.width
###############################################################################

# 보스2 ##########################################################

class Boss_Penguin:
    def __init__(self,t):
        self.x = 1500
        self.y = 300
        self.width = 470
        self.height = 750
        self.hp = 20
        self.t = t

    def draw(self):
        if self.t == "attack":
            screen.blit(bossPenguin_attack_image, (self.x, self.y))
        else:
            screen.blit(bossPenguin_image, (self.x, self.y))

    def hit(self, missiles): # 피격 판정
        return self.y < missiles.y + 26 and missiles.y < self.y + self.height and self.x < missiles.x + 8 and missiles.x < self.x + self.width

    def fire(self): # 왼쪽 방향으로 총알 발사
        badguys.append(Badguy_Right(self.x + 15, self.y + random.randint(750//4, 750//4*3)))

##################################################################

character = Character()
Map = Stage()
penguin = Penguin(960, 710) # 매개변수: 펭귄 초기 위치

# 한번만 쓸 것들
theif = Theif("")

badguys = []
enemys = []
walls = []
textboxs = []
boss = []
missiles = []
boss_missiles = [] #배열로 여러개 만들것들
cave_trashs = []
space_trashs = []
isdead = False
####################################################################
#################################################################### 게임루프
# 타이틀UI-1 ###########
isRunning = True

# 오프닝7 ########################################################
opening_character_run = False
opening_angry_flg = False
opening_flg = True
opening_angry = Opening_Character(300, 800)
opening_penguin = Penguin(1920, 800)
##################################################################

# 펭귄3 ##########################################################
penNum_stage3 = 2
penNum_stage6 = 1
penguin3 = Penguin(1050, 660) # 매개변수: 펭귄 초기 위치
penguin3_2 = Penguin(960, 340)
penguin6 = Penguin(960, 740)
##################################################################

# 보스3 ##########################################################
penNum_stage7 = 1
bossPenguin = Boss_Penguin("")
spawn = False
##################################################################

while 1:
    dt = clock.tick(60) #초당 프레임수는 60이다.
    pressed_keys = pygame.key.get_pressed() # 코딩 편하게 할려고 미리 써 놓은거 (게임과는 상관 X)

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("왼쪽 누름")
                isplayerRight=False
                isWalk=True
                character.range = 180
                walkAniTimer=time.time()
            if event.key==pygame.K_RIGHT:
                print("오른쪽 누름")
                isplayerRight=True
                isWalk=True
                character.range = 0
                walkAniTimer=time.time()
            if event.key==pygame.K_LALT:
                print("왼쪽 알트키 누름")
                isJump=True
                jumpAniTimer=time.time()
            if event.key==pygame.K_LSHIFT:
                print("왼쪽 쉬프트키 누름")
                isAttack=True
                attackAniTimer=time.time()

        if event.type==pygame.KEYUP: #키 땠을 때
            if event.key==pygame.K_LEFT:
                print("왼쪽 땜")
                isWalk=False
                playerTexture=LplayerTextureDefault
            if event.key==pygame.K_RIGHT:
                print("오른쪽 땜")
                isWalk=False
                playerTexture=playerTextureDefault
            if event.key==pygame.K_LALT:
                print("왼쪽 알트키 땜")
                #isJump=False
                #playerTexture=playerTextureDefault
            if event.key==pygame.K_LSHIFT:
                print("왼쪽 쉬프트키 땜")

        if event.type == QUIT:
            sys.exit() # X 누르면 나가기

        if event.type == KEYDOWN and event.key == K_LSHIFT:
            if stage >= 1 and istext_on == False:
                character.fire() # SPACE 누르면 총알 발사
                pygame.mixer.Sound.play(shot_sound)

    #스테이지 설정들
    if stage == 0: #시작화면 스테이지 값: 0
        Map.homescreen()
        if pygame.mouse.get_pressed()[0] and start_rect.collidepoint(pygame.mouse.get_pos()):
            stage += 2
        elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
            # 타이틀UI1 ########################
            #sys.exit()
            isRunning = False
            ####################################

    if stage == 11 and mapcounter == 11: #클리어 화면 스테이지 값: 11
            enemys.clear()
            badguys.clear()
            walls.clear()
            Map.clearscreen()

            score = (character.hp * 100) - (int(start_time - time.time())) #점수 계산
            if high_score < score:
                    high_score = score

            #점수 화면에 띄우기
            c_txt2 = font3.render(str(int(score)), True, (0, 0, 0))
            c_txt3 = font3.render('Score: ', True, (0, 0, 0))
            c_txt4 = font3.render(str(int(high_score)), True, (0, 0, 0))
            c_txt5 = font3.render('High Score: ', True, (0, 0, 0))

            screen.blit(c_txt2, (325, 400))
            screen.blit(c_txt3, (210, 400))
            screen.blit(c_txt4, (980, 400))
            screen.blit(c_txt5, (780, 400))

            #boss_music_loop.stop()
            pygame.mixer.Sound.play(clear_sound)
            mapcounter += 1
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit() # X누르면 나가기

                if pygame.mouse.get_pressed()[0] and Main_Buttun_rect.collidepoint(pygame.mouse.get_pos()):
                    last_fire = 0
                    stage = 0
                    score = 0
                    mapcounter = 2  # 오프닝7 #####
                    mapcounter = 1
                    missile_speed = 10
                    character = Character()
                    Map = Stage()
                    badguys = []
                    enemys = []
                    walls = []
                    boss = []
                    missiles = []
                    boss_missiles = []
                    Map.homescreen()
                    time.sleep(0.5)
                    break

                elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
                    
                pygame.display.update() #화면에 나타내기
    
    if stage > 0:
        if stage == 1:
            screen.blit(stage_museum_no_ring, (0, 0))
            theif.draw()
        if stage == 2:  # 오프닝2 - 배경 ##################
            screen.blit(opening_background_image, (0, 0))

        if stage == 3:
            screen.blit(stage_cave, (0, 0))
        if stage == 4:
            screen.blit(stage_museum, (0, 0))
        if stage == 5:
            screen.blit(stage_broken_museum, (0, 0))
        if stage == 6:
            screen.blit(stage_space, (0, 0))
        if stage == 7:
            screen.blit(stage_broken_museum, (0, 0))
        if stage == 8:
            screen.blit(clear_News, (0, 0))
        # 오프닝8 #########################
        if stage >= 3 :
            character.move(walls)
            character.draw()
            character.update()
        ###################################

        # 한 번만 체크하는거
        if stage == 1 and mapcounter == 1:
            start_time = time.time()
            Map.stage1()
            character.v = 2
            character.m = 1.2
            theif.x = 1500
            theif.y = screen_height - 300
            treasure_txt = False
            mapcounter += 1
            stage_music_loop = pygame.mixer.Sound(stage_music)
            stage_music_loop.play(-1) #음악 반복 재생

        if stage == 2 and mapcounter == 2:
            Map.stage2()
            theif.x = 300
            theif.y = screen_height - 300
            mapcounter += 1
            character.hp += 1

        if stage == 3 and mapcounter == 3:
            Map.stage3()
            Map.makeWall_garo(0, 1000, 24, "under")
            Map.makeWall_garo(0, 920, 14, "normal")
            Map.makeWall_garo(1120, 920, 10, "under")
            Map.makeWall_garo(1120, 840, 10, "normal")

            Map.makeWall_garo(0, 520, 11, "normal")

            character.v = 2
            character.m = 1.2

            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            # 충돌8 #############
            character.hp = 4
            #character.hp += 1
            #####################

        if stage == 4 and mapcounter == 4:
            Map.stage4()
            theif.x = 300
            theif.y = screen_height - 300
            mapcounter += 1
            character.hp += 1

        if stage == 5 and mapcounter == 5:
            Map.stage5()
            mapcounter += 1
            character.hp += 1

        if stage == 6 and mapcounter == 6:
            Map.stage6()
            walls.clear()

            Map.makeWall_garo(0, 1000, 24, "under")
            Map.makeWall_garo(0, 920, 24, "normal")

            Map.makeWall_sero(320, 760, 0, "normal")
            Map.makeWall_sero(640, 520, 0, "normal")
            Map.makeWall_sero(800, 280, 0, "normal")

            Map.makeWall_garo(1040, 280, 10, "normal")

            character.v = 2
            character.m = 1.2

            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            # 충돌9 #############
            character.hp = 4
            #character.hp += 1
            #####################

        if stage == 7 and mapcounter == 7:
            Map.stage7()
            walls.clear()

            Map.makeWall_garo(0, 1000, 24, "under")
            Map.makeWall_garo(0, 920, 24, "normal")
            character.v = 2
            character.m = 1.2
            theif.x = 1500
            theif.y = screen_height - 300
            theif.hp = 10
            mapcounter += 1
            # 충돌10 #############
            character.hp = 4
            #character.hp += 1
            #####################

        if stage == 8 and mapcounter == 8:
            Map.stage8()
            mapcounter += 1
            character.hp += 1

        if stage == 9 and mapcounter == 9:
            Map.stage9()
            mapcounter += 1
            character.hp += 1

        if stage == 10 and mapcounter == 10:
            Map.stage10()
            mapcounter += 1
            character.hp += 1

        #대화형 텍스트 박스 관련
        istext_on = False
        t = 0
        if stage == 1 and t < len(textboxs):
            textboxs[t].draw()
            istext_on = True
            if pressed_keys[K_z]:
                if (time.time() - stop) > character.attac_speed:
                    del textboxs[t]
                    stop = time.time()

        # 보스4 - 공격 준비 ################
        if stage == 7 and t < len(textboxs):
            textboxs[t].draw()
            istext_on = True
            if pressed_keys[K_z]:
                if (time.time() - stop) > character.attac_speed:
                    del textboxs[t]
                    stop = time.time()
                spawn = True
        ####################################

        #스테이지 안내형 텍스트 박스 관련
        if stage == 3:
            pass

        if stage == 4:
            if character.x < 970 and character.x > 820:
                screen.blit(textboxs_guide2, (800, 620))

            if character.x < 1600 and character.x > 1450:
                screen.blit(textboxs_guide3, (1430, 620))
                if pressed_keys[K_z]:
                    stage = 5

        if stage == 5:
            if character.x < 970 and character.x > 820:
                screen.blit(textboxs_guide1, (800, 620))
                if pressed_keys[K_UP]:
                    stage = 6
                    character.respawn()
        
        # 도둑의 움직임과 관련된 함수
        if stage == 1 and theif.x < 1920:
            if len(textboxs) == 0:
                theif.stage1_move()
                theif.draw()

        if stage == 3:
            # 펭귄4 ##################################################
            if penNum_stage3 > 0 :
                if (isdead == False):
                    # 충돌4 ##############################################
                    if character.collision_check(penguin3.penguin_rect) :
                        print("HIT!!")
                        if (character.x < penguin3.x) :
                            character.x -= 200
                        else :
                            character.x += 200
                        character.hp -= 1
                    ######################################################
                    if penguin3.hp != 0 :
                        penguin3.move(1050, 1850) # 이동 범위(x값)
                        penguin3.draw()
                        while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                            if penguin3.hit(missiles[tt]):
                                del missiles[tt]
                                penguin3.hp -= 1
                                print(penguin3.hp)
                                tt -= 1
                                del penguin3
                                penNum_stage3 -= 1
                                isdead = True
                            tt+=1

                # 충돌4 ##############################################
                if character.collision_check(penguin3_2.penguin_rect) :
                    print("HIT!!")
                    if (character.x < penguin3_2.x) :
                        character.x -= 200
                    else :
                        character.x += 200
                    character.hp -= 1
                ######################################################
                if penguin3_2.hp != 0 :
                    penguin3_2.move(0, 600) # 이동 범위(x값)
                    penguin3_2.draw()
                    while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                        if penguin3_2.hit(missiles[tt]):
                            del missiles[tt]
                            penguin3_2.hp -= 1
                            print(penguin3_2.hp)
                            tt -= 1
                            del penguin3_2
                            penNum_stage3 -= 1
                        tt+=1
            else:
                screen.blit(portal_image, (200, 400))
                if character.x < 600 and character.x > 200: # 포탈 범위
                    if pressed_keys[K_UP]:
                        stage = 6
                        mapcounter = 6
                        character.respawn()
            ##########################################################

        if stage == 4 and theif.y > 350:
            theif.stage2_move()
            theif.draw()

        if stage == 6:
            # 스테이지2 ##############################################
            if penNum_stage6 > 0 :
                # 충돌5 ##############################################
                if character.collision_check(penguin6.penguin_rect) :
                    print("HIT!!")
                    if (character.x < penguin6.x) :
                        character.x -= 200
                    else :
                        character.x += 200
                    character.hp -= 1
                ######################################################
                if penguin6.hp != 0 :
                    penguin6.move(710, 1800) # 이동 범위(x값)
                    penguin6.draw()
                    while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                        if penguin6.hit(missiles[tt]):
                            del missiles[tt]
                            penguin6.hp -= 1
                            print(penguin6.hp)
                            tt -= 1
                            del penguin6
                            penNum_stage6 -= 1
                        tt+=1

            else:
                screen.blit(portal_image, (1550, 180))
                if character.x < 1720 and character.x > 1440: # 포탈 범위
                    if pressed_keys[K_UP]:
                        mapcounter = 7
                        stage = 7
                        character.respawn()

        if stage == 7:
             # 보스5 - 피격 #############################
            if penNum_stage7 > 0 :
                # 충돌11 ##################################
                if character.x + character.width >= 1500 :
                    character.x = 1400
                    print("x:",character.x)
                ###########################################
                if bossPenguin.hp == 0 :
                    del bossPenguin
                    penNum_stage7 -= 1
                    spawn = False
                else :
                    bossPenguin.draw()
                    while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                        if bossPenguin.hit(missiles[tt]):
                            del missiles[tt]
                            bossPenguin.hp -= 1
                            print(bossPenguin.hp)
                            tt -= 1
                        tt+=1
            ############################################

        if stage == 3:
            cc = 0
            while cc < len(cave_trashs): #i가 현재 배드가이의 개체수 보다 작을 때 동안 반복
                cave_trashs[cc].move()# 움직임
                cave_trashs[cc].draw()# 그리기
    
                if cave_trashs[cc].off_screen(): #만약에 화면을 넘어가면
                    del cave_trashs[cc] # 배드가이 삭제
                    cc -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성
                elif cave_trashs[cc].touching(character):##추가
                    character.hp -= 1##추가
                    del cave_trashs[cc]##추가
                    cc -= 1##추가
                cc += 1

        if stage == 6:
            ss = 0
            while ss < len(space_trashs): #i가 현재 배드가이의 개체수 보다 작을 때 동안 반복
                space_trashs[ss].move()# 움직임
                space_trashs[ss].draw()# 그리기
                
                if space_trashs[ss].off_screen(): #만약에 화면을 넘어가면
                    del space_trashs[ss] # 배드가이 삭제
                    ss -= 1 # 삭제되면 i를 1 감소시킴으로서 또 다른 배드가이 생성
                elif space_trashs[ss].touching(character):##추가
                    character.hp -= 1##추가
                    del space_trashs[ss]##추가
                    ss -= 1##추가
                ss += 1

        #포탈 관련: 닿으면 캐릭터를 리스폰 위치로 옮기고 스테이지 1 증가
        # 스테이지1 #################################################
        if character.x > 1920 - 140 and ((stage == 3 and penNum_stage3 == 0) or (stage == 6 and penNum_stage6 == 0)): # 좌표 조건식으로 변경
            if stage == 3 :
                stage = 6
                mapcounter = 6
            elif stage == 6 :
                stage += 1
            character.respawn()

            enemys.clear()
            badguys.clear()
            walls.clear()
            missiles.clear()
        ##############################################################
        tt = 0
        # 펭귄5 ###############################################################
        '''
        if theif.hp != 0 and stage >= 3:
            while tt < len(missiles): #미사일과 도둑이 닿으면 hp 1 감소
                if theif.hit(missiles[tt]):
                    del missiles[tt]
                    theif.hp -= 1
                    print(theif.hp)
                    theif.x = random.randint(100,1800)
                    if stage == 6:
                        theif.y = random.randint(100, 800)
                    tt -= 1
                tt+=1
        '''
        #######################################################################
        
        if theif.hp == 0: # hp0돼면 ㅌㅌ
            theif.stage3_move(theif.x)
            if stage == 7:
                enemys.clear()
                badguys.clear()
                walls.clear()
                missiles.clear()
                screen.blit(clear_News, (0, 0))

        e = 0 # 포탑 판단
        while e < len(enemys):
            m_ = 0
            enemys[e].draw()

            while m_ < len(missiles): #캐릭터의 미사일과 충돌하면 체력 1 감소
                if enemys[e].hit(missiles[m_]):
                    enemys[e].hp -= (1 + character.damage)
                    del missiles[m_]
                    j -= 1
                m_ += 1
            
            if time.time() - enemys[e].last_badguy_spawn_time > 1.5: #만약 포탑 사정거리 범위 내에 캐릭터가 있다면
                if (character.x - fire_range < enemys[e].x and character.x + fire_range + 40 > enemys[e].x + 40) or (character.y - fire_range < enemys[e].y and character.y + fire_range + 40 > enemys[e].y + 40):
                    enemys[e].fire()
                    enemys[e].last_badguy_spawn_time = time.time()

            if enemys[e].hp <= 0: #체력이 0이하가 되면 삭제
                    del enemys[e]
            e += 1
        
        ra = random.random()
        if time.time() - last_trash_spawn_time > ra + ddd and stage == 7: #만약 포탑 사정거리 범위 내에 캐릭터가 있다면
            if spawn == True:
                bossPenguin.t = "attack"
                bossPenguin.fire()
                ddd -= 0.002
                last_trash_spawn_time = time.time()

        i = 0 #포탑 총알 판단: 그리기, 화면 넘어가면 삭제
        while i < len(badguys):
            badguys[i].move()
            badguys[i].draw()

            if badguys[i].off_screen():
                del badguys[i]
                i -= 1
            i += 1

        i = 0 #포탑 총알 판단: 캐릭터와 충돌 했을 때 hp감소, 삭제
        while i < len(badguys):
            if badguys[i].touching_c(character): #만약 포탑 총알과 캐릭터가 닿았다면
                del badguys[i]
                character.hp -= 1
                i -= 1
            i += 1

        b = 0 #보스 판단
        while b < len(boss):
            m_ = 0
            boss[b].draw()

            while m_ < len(missiles): #미사일과 보스가 닿으면 hp 1 감소
                if boss[b].hit(missiles[m_]):
                    boss[b].hp -= (1 + character.damage)
                    del missiles[m_]
                    j -= 1
                m_ += 1

            if time.time() - boss[b].last_badguy_spawn_time > 1:
                boss[b].fire_big()
                boss[b].fire_small()
                boss[b].last_badguy_spawn_time = time.time()

            if boss[b].hp <= 0: #보스 체력이 0 이하가 되면 삭제
                    del boss[b]
            b += 1

        ib = 0 #보스 총알 판단: 그리기, 화면 넘어가면 삭제
        while ib < len(boss_missiles):
            boss_missiles[ib].move()
            boss_missiles[ib].draw()
            if boss_missiles[ib].off_screen():
                del boss_missiles[ib]
                ib -= 1
            ib += 1
        
        ib = 0 #보스 총알 판단: 캐릭터와 충돌 했을 때 hp감소, 삭제
        while ib < len(boss_missiles):
            if boss_missiles[ib].touching_c(character):
                del boss_missiles[ib]
                character.hp -= 1
                ib -= 1
            ib += 1

        w = 0 # 벽 판단: 그리기, 캐릭터 미사일과 충돌 했을 대 hp 감소, 삭제
        while w < len(walls):
            m = 0
            index = 0
            walls[w].draw()
            
            while m < len(missiles): #미사일과 충돌했을 때 hp 감소
                if walls[w].hit(missiles[m]):
                    walls[w].hp -= (1 + character.damage)
                    del missiles[m]
                    j -= 1
                
                if walls[w].hp <= stage * 6 / 2: #벽의 체력(stage * 6)이 절반이 되면 금간 이미지로 변경
                    walls[w].wall_state=wall_broken
                m += 1

            if walls[w].hp <= 0: #벽 체력이 0 이하가 되면 삭제(밑에도 추가하면 리스트 오류남)
                del walls[w]
            w += 1

        w = 0 # 벽 판단: 그리기, 포탑 미사일과 충돌 했을 대 hp 감소, 삭제
        while w < len(walls):
            index = 0
            walls[w].draw()
            
            while index < len(badguys):
                if walls[w].hit(badguys[index]):
                    walls[w].hp -= 1
                    del badguys[index]
                    j -= 1
                
                if walls[w].hp <= stage * 6 / 2:
                    walls[w].wall_state=wall_broken
                index += 1
            w += 1

        j = 0 #캐릭터 미사일 판단: 그리기, 화면 밖으로 나가면 삭제하기
        while j < len(missiles):
            missiles[j].move()
            if missiles[j].off_screen():
                del missiles[j]
                j -= 1
            j += 1

        #기본 인터페이스 정보
        if stage >= 1 and stage <= 10:
            # UI2 ##########################################################
            # 충돌6 #######################################
            if character.hp > 0 and character.hp <= 4 :
                heart_image = heart_images[character.hp - 1]
            ###############################################
            screen.blit(heart_image, (10, 10))
            screen.blit(water_image, (150, 10))
            ################################################################
            # hp_str_text = font3.render('HP', True, (255,128,128))
            # screen.blit(hp_str_text, (10,10))
            # hp_text = font3.render(str(int(character.hp)), True, (255,128,128))
            # screen.blit(hp_text, (70,10))

        # 오프닝9 ########################
        if stage == 2 :
            if opening_flg and not(opening_angry_flg) and not(opening_character_run) :
                screen.blit(opening_character_back_image, (300, 850))
                if (opening_penguin.isLeft and opening_penguin.x <= 555) :
                    del opening_bucket_image
                elif (opening_penguin.isLeft and opening_penguin.x > 555) :
                    screen.blit(opening_bucket_image, (425, 900))
                opening_penguin.opening_move()
                opening_penguin.draw()
                if (opening_penguin.isRight and opening_penguin.x >= 1920) :
                    del opening_penguin
                    opening_angry_flg = True
            elif opening_flg and opening_angry_flg and not(opening_character_run) :
                del opening_character_back_image
                opening_angry_flg = False
                opening_character_run = True
            elif opening_flg and not(opening_angry_flg) and opening_character_run :
                opening_angry.move()
                opening_angry.draw()
                if opening_angry.x >= 1920 :
                    opening_flg = False
            else :
                mapcounter = 3
                stage = 3
                
        ##################################

        #캐릭터의 체력이 0이되어 게임 오버되었을 때 각종 게임 정보들 화면에 띄우기
        if character.hp <= 0:
                enemys.clear()
                badguys.clear()
                walls.clear()
                #stage_music_loop.stop()
                screen.blit(bad_News,(0,0))
                Button(Main_Buttun,210,620,313,97,Main_Buttun,210,620,'replay')

                score = (character.hp * 100) - (int(start_time - time.time())) #점수 계산
                if high_score < score:
                        high_score = score

                #점수 화면에 띄우기

                mapcounter += 1
                while 1:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            sys.exit() # X누르면 나가기

                    if pygame.mouse.get_pressed()[0] and Main_Buttun_rect.collidepoint(pygame.mouse.get_pos()):
                        last_fire = 0
                        stage = 0
                        score = 0
                        fff
                        ggg

                        mapcounter = 1
                        missile_speed = 10
                        character = Character()
                        Map = Stage()
                        theif = Theif("")
                        badguys = []
                        enemys = []
                        walls = []
                        boss = []
                        cave_trashs = []
                        space_trashs = []
                        missiles = []
                        boss_missiles = []
                        last_trash_spawn_time = 0
                        ggg = 0
                        fff = 0
                        ddd = 0.9
                        Map.homescreen()
                        time.sleep(0.5)
                        break

                    elif pygame.mouse.get_pressed()[0] and end_rect.collidepoint(pygame.mouse.get_pos()):
                        sys.exit()
                        
                    pygame.display.update() #화면에 나타내기
                    
    # if character.y != screen_height - 300 and character.canMove_D == True and character.isJump == 0:
    #     character.v -= 2
    #     for kk in range (character.y <= screen_height - 300):
    #         character.y -= character.v * character.m

    if isWalk==True and isplayerRight==False and isJump==False and isAttack==False: #왼쪽 이동
        if time.time()-walkAniTimer<0.2:
            playerTexture=LplayerWalk1
        elif time.time()-walkAniTimer<0.4:
            playerTexture=LplayerWalk2
        elif time.time()-walkAniTimer<0.6:
            playerTexture=LplayerWalk3
        else:
            walkAniTimer=time.time()

    if isWalk==True and isplayerRight==True and isJump==False and isAttack==False: #오른쪽 이동
        if time.time()-walkAniTimer<0.2:
            playerTexture=playerWalk1
        elif time.time()-walkAniTimer<0.4:
            playerTexture=playerWalk2
        elif time.time()-walkAniTimer<0.6:
            playerTexture=playerWalk3
        else:
            walkAniTimer=time.time()

    if isJump==True and isplayerRight==False and isAttack==False: #왼쪽 점프
        if time.time()-jumpAniTimer<0.2:
            playerTexture=LplayerJump1
        elif time.time()-jumpAniTimer<0.4:
            playerTexture=LplayerJump2
        elif time.time()-jumpAniTimer<0.6:
            playerTexture=LplayerJump3
        else:
            isJump=False
            playerTexture=LplayerTextureDefault

    if isJump==True and isplayerRight==True and isAttack==False: #오른쪽 점프
        if time.time()-jumpAniTimer<0.2:
            playerTexture=playerJump1
        elif time.time()-jumpAniTimer<0.4:
            playerTexture=playerJump2
        elif time.time()-jumpAniTimer<0.6:
            playerTexture=playerJump3
        else:
            isJump=False
            playerTexture=playerTextureDefault

    if isAttack==True and isplayerRight==False: #왼쪽 공격
        if time.time()-attackAniTimer<0.1:
            playerTexture=LplayerAttack1
        elif time.time()-attackAniTimer<0.2:
            playerTexture=LplayerAttack2
        elif time.time()-attackAniTimer<0.3:
            playerTexture=LplayerAttack3
        else:
            isAttack=False
            playerTexture=LplayerTextureDefault

    if isAttack==True and isplayerRight==True: #오른쪽 공격
        if time.time()-attackAniTimer<0.1:
            playerTexture=playerAttack1
        elif time.time()-attackAniTimer<0.2:
            playerTexture=playerAttack2
        elif time.time()-attackAniTimer<0.3:
            playerTexture=playerAttack3
        else:
            isAttack=False
            playerTexture=playerTextureDefault

    pygame.display.update() #화면 업데이트