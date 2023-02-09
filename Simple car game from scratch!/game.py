import pygame 
from pygame.locals import *
import random  


size=width,height=(800,650)
road_w=int(width/1.6)
roadmark_w=int(width/80)


right_lane = width/2+road_w/4
left_lane = width/2-road_w/4

speed=1


pygame.init()

running=True

screen=pygame.display.set_mode((size))

pygame.display.set_caption("my first game")
screen.fill((60,220,0))


pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2 ,0,road_w,height))

pygame.draw.rect(
    screen,
    (255,240,60),
    (width/2-roadmark_w/2,0,roadmark_w,height))

pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2-road_w/2+roadmark_w*2,0,roadmark_w,height))

pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2+road_w/2-roadmark_w*3,0,roadmark_w,height))

pygame.display.update()

#this for first car 
car=pygame.image.load('car.png')
car_loc=car.get_rect()
car_loc.center=right_lane,height*0.8

#this for second car 
car2=pygame.image.load('otherCar.png')
car_loc2=car.get_rect()
car_loc2.center=left_lane ,height*0.2



counter=0 

while running:
    counter+=1
    if counter==1024:
        speed+=0.35
        counter=0
        print("level up",speed)
    car_loc2[1] +=speed

    if car_loc2[1]>height:
        car_loc2[1]=-200
        if random.randint(0,1)==0:
            car_loc2.center=right_lane,-200
        else:
            car_loc2.center=left_lane,-200
    
    # This if we whant to finish the game 
    if car_loc[0]==car_loc2[0] and car_loc2[1]>car_loc[1]-250:
        print("GAME OVER! YOU LOST ")
        break

    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        
        elif event.type==KEYDOWN:
            if event.key in  [K_a ,K_LEFT]:
                car_loc=car_loc.move([-int(road_w/2),0])
            if event.key in [K_d ,K_RIGHT]:
                car_loc=car_loc.move([int(road_w/2),0])

    pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2 ,0,road_w,height))

    pygame.draw.rect(
    screen,
    (255,240,60),
    (width/2-roadmark_w/2,0,roadmark_w,height))

    pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2-road_w/2+roadmark_w*2,0,roadmark_w,height))

    pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2+road_w/2-roadmark_w*3,0,roadmark_w,height))

    screen.blit(car,car_loc)
    screen.blit(car2,car_loc2)
    pygame.display.update()
pygame.quit()

