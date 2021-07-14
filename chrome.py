from turtle import * 

from time import sleep
colormode(255) 
red=(234, 68, 53); green=(0, 172, 71); yellow=(255, 186, 0); 
blue=(66, 133, 244)
r=120 
seth(-150) 
up() 
#-------------RED -------------
color(red) 
begin_fill() 
fd(r) 
down() 
right(90) 
circle(-r, 120) 
fd(r*3**.5) 
left(120) 
circle(2*r, 120) 
left(60) 
fd(r*3**.5)
end_fill()

#-------------Green -------------

left(180) 
color(green) 
begin_fill()
fd(r*3**.5)
left(120) 
circle(2*r, 120) 
left(60) 
fd(r*3**.5)
left(180) 
circle(-r, 120) 
end_fill() 

#-------------Yellow -------------

left(180) 
circle(r,120)
color(yellow) 
begin_fill()
circle(r, 120)
right(180) 
fd(r*3**.5)
right(60) 
circle(-2*r, 120) 
right(120) 
fd(r*3**.5)
end_fill()

#-------------Blue Circle-------------

up() 
left(98) 
fd(15) 
seth(60) 
color(blue) 
down() 
begin_fill()
circle(distance(0,0)) 
end_fill() 
ht() 

done()
