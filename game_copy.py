import pygame
import sys
#init game

pygame.init()


#Cài đặt cửa sổ
screen_width = 1024
screen_height = 720
#Xét kích thước màn hình
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game_demo")

#Cài đặt background
img_background = pygame.image.load("graphics/background_space.jpg")

#Cài đặt máy bay
img_air_craft = pygame.image.load("graphics/air_craft.png")
width_air_craft = img_air_craft.get_width()
height_air_craft = img_air_craft.get_height()
x_air_craft = screen_width/2 -width_air_craft / 2 #Tính toạ độ x trung tâm
y_air_craft = screen_height/2 - height_air_craft / 2 #Tính toạ độ y trung tâm


#Cài đặt laser
img_laser = pygame.image.load("graphics/laser.png").convert_alpha()    
rect_laser = pygame.Rect(x_air_craft,y_air_craft,img_laser.get_width(),img_laser.get_height())
running = True

while running:

    # rect_laser = pygame.Rect(rect_laser.x,rect_laser.y,width_air_craft,height_air_craft)
    #Đưa background lên màn hình    
    screen.blit(img_background,(0,0))
    #Đưa máy bay lên màn hình
    screen.blit(img_air_craft,(x_air_craft,y_air_craft))
    rect_air_craft = pygame.Rect(x_air_craft,y_air_craft,width_air_craft,height_air_craft)#Hình chữ nhật của máy bay

    #Chèn background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #Lấy toạ độ rê chuột
        if event.type == pygame.MOUSEMOTION:
            #Lấy toạ độ chuột
            mouse_x,mouse_y = pygame.mouse.get_pos()
            #Gán toạ độ hình bằng toạ độ chuột
            x_air_craft = mouse_x
            y_air_craft = mouse_y
            #vẽ lại hình chữ nhật 
            rect_air_craft = pygame.Rect(mouse_x,mouse_y,width_air_craft,height_air_craft)#Hình chữ nhật của máy bay
            screen.blit(img_air_craft,(x_air_craft,y_air_craft))
    # rect_laser = pygame.Rect(mouse_x,mouse_y,width_air_craft,height_air_craft)
    rect_laser.y -= 1
    screen.blit(img_laser,(rect_laser.x ,rect_laser.y ))    
    pygame.display.flip()
pygame.quit()
sys.exit()
