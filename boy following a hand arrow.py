from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
# 이벤트 함수
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass
# 랜덤한 위치 생성
def random_xy():
    global mouse_x, mouse_y
    mouse_x = random.randint(100, 900)
    mouse_y = random.randint(100, 700)

# 캐릭터 이동 함수
def character_move():
    global x, y

    speed = 0.05
    x += (mouse_x - x) * speed
    y += (mouse_y - y) * speed

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

# 처음 랜덤 설정
random_xy()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(mouse_x, mouse_y)
    character_move()
    if(mouse_x>=x):
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100,  0, 'h', x, y, 100, 100)

    update_canvas()
    frame = (frame + 1) % 8
    delay(0.03)

    handle_events()

    # 새로운 랜덤 위치 생성
    if abs(x - mouse_x) < 5 and abs(y - mouse_y) < 5:
        random_xy()

close_canvas()
