import pygame
import sys
from random import randint, uniform
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
# rect_laser = pygame.Rect(x_air_craft,y_air_craft,img_laser.get_width(),img_laser.get_height())
time_shoot = 100
speed_laser = 5
time = pygame.time.Clock()
start_time = 0
lst_laser = []


#Cài đặt thiên thạch meteor 
img_meteor = pygame.image.load("graphics/meteor.png")
speed_meteor = 1
lst_meteor = []
time_fall = 500
start_time_fall = 0

running = True




while running:

    # rect_laser = pygame.Rect(rect_laser.x,rect_laser.y,width_air_craft,height_air_craft)
    #Đưa background lên màn hình    
    screen.blit(img_background,(0,0))
   
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
    

    

            
    #Bắn đạn
    current_time = pygame.time.get_ticks()
    if current_time - start_time > time_shoot : 
        start_time = current_time
        new_laser = pygame.Rect(x_air_craft + img_air_craft.get_width()/2.2,y_air_craft,img_laser.get_width(),img_laser.get_height())
        lst_laser.append(new_laser)

    #Thiên thạch rơi
    current_time_fall = pygame.time.get_ticks()
    if current_time_fall - start_time_fall > time_fall : 
        start_time_fall = current_time_fall
        #Random toạ độ thiên thạch 
        x = randint(-100, screen_width + 100)        
        y = 0       
        new_meteor = pygame.Rect(x,y,img_meteor.get_width(),img_meteor.get_height())
        lst_meteor.append(new_meteor)


   

    for laser in lst_laser: 
        laser.y -= speed_laser 
        screen.blit(img_laser,(laser.x ,laser.y))
        if laser.y < 0:
            lst_laser.remove(laser)    




    for metoer in lst_meteor: 
        
        metoer.x += -2
        metoer.y += speed_meteor
        screen.blit(img_meteor,(metoer.x ,metoer.y))
        if metoer.y == screen_height + 100:
            lst_meteor.remove(metoer)    



        for laser in lst_laser:
            if metoer.colliderect(laser): 
                lst_laser.remove(laser)
                lst_meteor.remove(metoer)
        


    #Đưa máy bay lên màn hình
    screen.blit(img_air_craft,(x_air_craft,y_air_craft))
    rect_air_craft = pygame.Rect(x_air_craft,y_air_craft,width_air_craft,height_air_craft)#Hình chữ nhật của máy bay
    pygame.display.flip()
pygame.quit()
sys.exit()
