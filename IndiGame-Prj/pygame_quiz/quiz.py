import random
import pygame

##################################################
# 기본 초기화 (반드시 해야 하는 것들)

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Indi game') # 게임 이름

# FPS
clock = pygame.time.Clock()

##################################################
# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
background = pygame.image.load("C:/Users/ko/OneDrive/문서/Python mini Prj/quiz/quiz_background.jpg")
# 캐릭터 만들기
character = pygame.image.load("C:/Users/ko/OneDrive/문서/Python mini Prj/quiz/puppy.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 똥 만들기
poo = pygame.image.load("C:/Users/ko/OneDrive/문서/Python mini Prj/quiz/poo.png")
poo_size = poo.get_rect().size
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = random.randint(0, (screen_width - poo_width))
poo_y_pos = 0
poo_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40)
score = 0

# 이동 위치
to_x = 0
character_speed = 10

running = True
while running :
    dt = clock.tick(60)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                to_x += character_speed
            elif event.key == pygame.K_LEFT :
                to_x -= character_speed
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    poo_y_pos += poo_speed

    if poo_y_pos > screen_height :
        score += 1
        poo_y_pos = 0
        poo_x_pos = random.randint(0, (screen_width - poo_width))
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos
    
    if character_rect.colliderect(poo_rect) :
        print("충돌했어요!")
        print("%d점 입니다." % score)
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(poo, (poo_x_pos, poo_y_pos)) # 캐릭터 그리기

    score_board = game_font.render(str(int(score)), True, (0,0,0))

    screen.blit(score_board, (10, 10))

    pygame.display.update()

pygame.quit()