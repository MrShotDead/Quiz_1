import pgzrun
WIDTH=1000
HEIGHT=800
rect = Rect(100,50,800,100)
ans_1 = Rect (61,175,325,175)
ans_2 = Rect (600,175,325,175)
ans_3 = 
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(rect,"yellow")
    screen.draw.filled_rect(ans_1,"yellow")
    screen.draw.filled_rect(ans_2,"yellow")
pgzrun.go()