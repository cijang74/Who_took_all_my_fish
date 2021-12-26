# 라이브러리, 클래스 불러오기
import pygame

# 파이게임 초기화
pygame.init()

# 게임 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock() 

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# 이미지, 사운드 불러오기
test_image = pygame.image.load("images/이미지 이름.png").convert() # 이미지
fishing_music = pygame.mixer.Sound('sounds/사운드 이름.wav') # 사운드

# 변수
test = 0

# 클래스
class Test():
    def test(self):
        pass

# 이벤트 루프
running = True # running이 참일때 게임은 실행중

while running:
    dt = clock.tick(30) # 게임 화면의 초당 프레임 수
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

    pygame.display.update() # 루프 내에서 발생한 모든 이미지 변화를 업데이트

# pygame 종료
pygame.quit()