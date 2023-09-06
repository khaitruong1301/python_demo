import pygame
import sys
from random import randint, uniform
#init game

pygame.init()


#Cài đặt cửa sổ
screen_width = 1920
screen_height = 1080
#Xét kích thước màn hình
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game_demo")

#Cài đặt background
img_background = pygame.image.load("graphics/background_space.jpg")
img_background = pygame.transform.scale(img_background, (screen_width, screen_height))

#Cài đặt máy bay
img_air_craft = pygame.image.load("graphics/air_craft.png")
width_air_craft = img_air_craft.get_width()
height_air_craft = img_air_craft.get_height()
x_air_craft = screen_width/2 -width_air_craft / 2 #Tính toạ độ x trung tâm
y_air_craft = screen_height/2 - height_air_craft / 2 #Tính toạ độ y trung tâm





#Cài đặt laser
img_laser = pygame.image.load("graphics/laser.png").convert_alpha()    
# rect_laser = pygame.Rect(x_air_craft,y_air_craft,img_laser.get_width(),img_laser.get_height())
time_shoot = 300
speed_laser = 25
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

#font 
font = pygame.font.Font('graphics/subatomic.ttf',32)
#live 
live = 2
# live_title = font.render(f'''Live: ${live}''','#fff')

#score
score = 0
# score_title = font.render(f'''Score: ${live}''','#fff')

#lvl
level = 1

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
    

    pygame.time.Clock().tick(60)
    

            
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


   
    #xử lý bắn đạn
    for laser in lst_laser: 
        laser.y -= speed_laser 
        screen.blit(img_laser,(laser.x ,laser.y))
        if laser.y < 0:
            lst_laser.remove(laser)    
 


    #Xử lý thiên thạch rơi
    for metoer in lst_meteor: 
        
        metoer.x += -2
        metoer.y += speed_meteor
        screen.blit(img_meteor,(metoer.x ,metoer.y))
        if metoer.y == screen_height:
            lst_meteor.remove(metoer)    


        #Xử lý đạn bắn thiên thạch tăng điểm
        for laser in lst_laser:
            if metoer.colliderect(laser) : 
                lst_laser.remove(laser)
                if metoer in lst_meteor:
                    lst_meteor.remove(metoer)
                    score += 10
                if score % 100 == 0 : 
                    level += 1
                #Tăng số lượng rơi
                time_fall -= 10 * level      
                #Tăng tốc độ rơi
                speed_meteor +=  level * 0.1     


    #Đưa máy bay lên màn hình
    screen.blit(img_air_craft,(x_air_craft,y_air_craft))
    #Hiển thị điểm
    score_title = font.render(f'''Score: {score}''',True,'white')
    screen.blit(score_title, ((screen_width//2 - score_title.get_width()//2 ) , screen_height - 100) )
    #Hiển thị lvl
    level_title = font.render(f'''Level: {level}''',True, 'white')
    screen.blit(level_title, (10 , 10) )
    #Hiển thị mạng
    live_title = font.render(f'''Live: {live}''',True, 'white')
    screen.blit(live_title , (screen_width - live_title.get_width() - 10, 10 ))

    rect_air_craft = pygame.Rect(x_air_craft,y_air_craft,width_air_craft,height_air_craft)#Hình chữ nhật của máy bay
    pygame.display.flip()
pygame.quit()
sys.exit()
