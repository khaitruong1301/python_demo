import pygame
import sys
pygame.init()
#Cài đặt cửa sổ xét kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game_demo")

#Biến trò chơi (chạy hoặc dừng)
runing = True
while runing:
    #Nhận sự kiện của pygame
    event = pygame.event.poll()
    #Khi người dùng chọn dấu x
    if event.type == pygame.QUIT:
        runing = False

    #Cài đặt game ...
    
    # Cập nhật màn hình
    pygame.display.flip()
pygame.quit()
sys.exit()