from tkinter import *
from time import *
from random import *
from replit import audio

root = Tk()
s = Canvas(root, width=600, height=600, background="#0099AA")

# START SCREEN/MENU
def startScreen():
  global start, w1, w2, w3, w4, w5, w6, w7, fins, title, c1, c2, c3, c4, c1_t, c2_t, c3_t, c4_t

  # Start the game is false 
  start = False
  
  # Create Whale 
  w1 = s.create_polygon(150, 100, 350, 125, 150, 175, fill="#79acd9", smooth=True)
  w2 = s.create_oval(25, 100, 225, 375, fill="#afd1f0", outline="")
  w3 = s.create_oval(-25, -50, 225, 350, fill="#508abf", outline="")
  w4 = s.create_polygon(150, 0, -50, 100, 0, 300, 150, 300, fill="#225380", smooth=True)
  w5 = s.create_oval(50, 250, 70, 270, fill="black")
  w6 = s.create_oval(175, 250, 190, 270, fill="black")
  w7 = s.create_oval(175, 250, 185, 260, fill="#cee1f2", outline="")

  # Create random fins
  fins = []
  for f in range(5):
      fins.append(create_fin(randint(300, 600), randint(0, 600)))

  # Title of game 
  title = s.create_text(300, 100, text="PENGUIN LIFE", font=('Helvetica','36','bold'), fill="white")

  # Button backgrounds and texts
  c1 = s.create_rectangle(200, 200, 400, 275, fill="white", outline="")
  c1_t = s.create_text(300, 235, text="EASY", font=('Helvetica','14','bold'), fill="black")
  c2 = s.create_rectangle(200, 300, 400, 375, fill="white", outline="")
  c2_t = s.create_text(300, 335, text="MEDUIM", font=('Helvetica','14','bold'), fill="black")
  c3 = s.create_rectangle(200, 400, 400, 475, fill="white", outline="")
  c3_t = s.create_text(300, 435, text="HARD", font=('Helvetica','14','bold'), fill="black")

  # Instructions button 
  c4 = s.create_rectangle(525, 525, 575, 575, fill="white", outline="")
  c4_t = s.create_text(550, 550, text="?", font=('Helvetica','14','bold'), fill="black")

  # Check for clicks on start screen 
  root.bind("<Button-1>", startScreenClick)
  
# Delete items in start screen
def deleteStartScreen():
  s.delete(w1, w2, w3, w4, w5, w6, w7, fins, title, c1, c2, c3, c4, c1_t, c2_t, c3_t, c4_t)
  for f in range(len(fins)):
    s.delete(fins[f])

def startScreenClick(event):
  global hunger_state, num_fins, num_baby, fish_food

  xMouse = event.x
  yMouse = event.y

	# Easy button is clicked (less fins and decreasing hunger)
  if 200 <= xMouse <= 400 and 200 <= yMouse <= 275:
    hunger_state = 0.175
    num_fins = 3
    num_baby = 1
    fish_food = 25
    deleteStartScreen()
    runGame()

	# Medium button is clicked 
  elif 200 <= xMouse <= 400 and 300 <= yMouse <= 375:
    hunger_state = 0.185
    num_fins = 4
    num_baby = 1
    fish_food = 20
    deleteStartScreen()
    runGame()

	# Hard button is clicked
  elif 200 <= xMouse <= 400 and 400 <= yMouse <= 475:
    hunger_state = 0.135
    num_fins = 6
    num_baby = 2
    fish_food = 20
    deleteStartScreen()
    runGame()

  elif 525 <= xMouse <= 575 and 525 <= yMouse <= 575:
    deleteStartScreen()
    instructions()
	
  else:
    pass

# INSTRUCTIONS
def instructions():
  global i, b, i1, i2, i3, i4, b1, b1_t
  i = s.create_text(300, 100, text="INSTRUCTIONS", font=('Helvetica','36','bold'), fill="white")
  b = s.create_rectangle(10, 175, 590, 350, fill="white", outline="")
  i1 = s.create_text(300, 225, text="You are a adult penguin searching for food for its hungry child.", font=('Helvetica','12'), fill="black")
  i2 = s.create_text(300, 250, text="Collect fish and bring it back to your child before it starves.", font=('Helvetica','12'), fill="black")
  i3 = s.create_text(300, 275, text="Beware! Killer whales may get you first...", font=('Helvetica','12'), fill="black")
  i4 = s.create_text(300, 300, text="Move using the arrow keys. Press q to quit.", font=('Helvetica','12'), fill="black")
  b1 = s.create_rectangle(25, 525, 75, 575, fill="white", outline="")
  b1_t = s.create_text(50, 550, text="<", font=('Helvetica','14','bold'), fill="black")

  root.bind("<Button-1>", instructionsClick)

def instructionsClick(event):
  xMouse = event.x
  yMouse = event.y
  
  if 25 <= xMouse <= 75 and 525 <= yMouse <= 575:
    deleteInstructions()
    startScreen()

def deleteInstructions():
  s.delete(i, b, i1, i2, i3, i4, b1, b1_t)

def stopGame():
  global title, s1, b1, b2, b1_t, b2_t, name
  title = s.create_text(300, 100, text="GAME OVER", font=('Helvetica','36','bold'), fill="white")
  s1 = s.create_text(300, 200, text="TIME: "+str(deltaT), font=('Helvetica','18','bold'), fill="white")
  b1 = s.create_rectangle(200, 250, 400, 350, fill="white", outline="")
  b1_t = s.create_text(300, 300, text="TRY AGAIN", font=('Helvetica','18','bold'), fill="black")
  b2 = s.create_rectangle(25, 525, 75, 575, fill="white", outline="")
  b2_t = s.create_text(50, 550, text="☰", font=('Helvetica','14','bold'), fill="black")

  name = s.create_text(515, 575, text="Made by: Derek Sheen 2022", font=('Helvetica','8'), fill="white")

  root.bind("<Button-1>", stopGameClick)

def stopGameClick(event):
  xMouse = event.x
  yMouse = event.y
  
  if 25 <= xMouse <= 75 and 525 <= yMouse <= 575:
    deleteStopGame()
    startScreen()
  elif 200 <= xMouse <= 400 and 250 <= yMouse <= 350:
    deleteStopGame()
    runGame()

def deleteStopGame():
  s.delete(title, s1, b1, b2, b1_t, b2_t, name)

def playSound():
  global source
  source = audio.play_file("wind.mp3")
  source.set_loop(100)

def create_fin(x, y):
  fin = s.create_polygon(x, y, x+50, y-50, x+100, y-50, x+75, y-25, x+80, y, x+50, y, fill="#225380", smooth=True)

  return fin

def setInitialValues():
  global xPenguin, yPenguin, ballRadius, ballColour, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, penguin, gameStillGoing, iceFriction, isSliding, penguin_img, penguin_baby_img, originTime, fish_img, xFish, yFish, num_fish, xPool, yPool, pools, sound_count, source, penguin_state, xFins, yFins, fins, num_fish, xBaby, yBaby, hunger_baby, babies
  penguin_img = PhotoImage( file = "penguin.png" )
  penguin_baby_img = PhotoImage(file = "penguinBaby.png")
  fish_img = PhotoImage( file = "fish.png")
  xPenguin = 500
  yPenguin = 100
  xFish = randint(50, 550)
  yFish = randint(100, 350)
  ballRadius = 20
  ballColour = "blue"
  sound_count = 1
  xMouse = 0
  yMouse = 0
  xSpeed = 0
  ySpeed = 0
  num_fish = 0
  hunger_baby = []
  penguin_state = 0
  xPool = []
  yPool = []
  pools = []
  xFins = []
  yFins = []
  fins = []
  xBaby = []
  yBaby = []
  babies = []
  for b in range(num_baby):
    xBaby.append(randint(50, 550))
    yBaby.append(randint(450, 550))
    hunger_baby.append(100)
    babies.append(0)
    
  num_fins = 5
  originTime = int(time())+3
  penguin = 0
  iceFriction = 0.95
  isSliding = False
  gameStillGoing = True

  # Create fin x and y values
  for f in range(num_fins):
    xFins.append(randint(600, 1000))
    yFins.append(randint(25, 425))

  # Create land
  greens = ["#EEEEEE", "#AADDCC", "#55AAAA", "#009999"]
  y1 = 450
  y2 = 600
  w = 20
  for i in range(4):
    s.create_rectangle(0, y1, 600, y2, fill=greens[i], outline=greens[i])
    y2, y1 = y1, y1-w
    w //= 1.2

def keyHandler(event):
  global xSpeed, ySpeed, gameStillGoing, penguin_img, penguin_state
  # Land speed
  if yPenguin > 450:
    if penguin_state != 0:
      penguin_img = PhotoImage( file = "penguin.png" )
    penguin_state = 0
    speed = 3
  # Water speed
  else:
    speed = 6

  if event.keysym == "Left":
    xSpeed = -speed
    if penguin_state != 1 and yPenguin <= 450: 
      penguin_img = PhotoImage( file = "penguin2.png" )
      penguin_state = 1
  elif event.keysym == "Right":
    xSpeed = speed
    if penguin_state != 2 and yPenguin <= 450:
      penguin_img = PhotoImage( file = "penguin1.png" )
      penguin_state = 2
  if event.keysym == "Down":
    ySpeed = speed
  elif event.keysym == "Up":
    ySpeed = -speed
  if event.keysym == "q":
    gameStillGoing = False

def keyUpHandler(event):
  global isSliding
  isSliding = True

def updatePosition():
  global xPenguin, yPenguin, xSpeed, ySpeed, xFish, yFish, num_fish, hunger_baby, gameStillGoing

  xPool.append(xFish - 30)
  yPool.append(yFish - 30)

  if xPenguin > xFish-24 and xPenguin < xFish+24 and yPenguin > yFish-24 and yPenguin < yFish+24:
    xFish = randint(50, 550)
    yFish = randint(50, 350)
    num_fish += 1
    
  for b in range(num_baby):
    if num_fish > 0 and xBaby[b]-25 < xPenguin < xBaby[b]+25 and yBaby[b]-25 < yPenguin < yBaby[b]+25:
      if hunger_baby[b] > 85:
        break
      elif hunger_baby[b]+fish_food > 100:
        hunger_baby[b] = 100
      else:
        hunger_baby[b] += fish_food
      num_fish -= 1

  # Borders
  if xPenguin < 20 and xSpeed < 0:
    xSpeed = 0
  elif xPenguin > 580 and xSpeed > 0:
    xSpeed = 0
  if yPenguin < 20 and ySpeed < 0:
    ySpeed = 0
  elif yPenguin > 580 and ySpeed > 0:
    ySpeed = 0
  
  xPenguin += xSpeed 
  yPenguin += ySpeed 

  for b in range(num_baby):
    hunger_baby[b] -= hunger_state

  if yPenguin > 450:
    iceFriction = 0.98
  else:
    iceFriction = 0.95

  if isSliding: 
    xSpeed *= iceFriction
    ySpeed *= iceFriction

  for f in range(len(xFins)):
    if xFins[f] < xPenguin < xFins[f]+100 and yFins[f] > yPenguin > yFins[f]-50:
      gameStillGoing = False
    if xFins[f]+100 < 0:
      xFins[f] = randint(600, 1000)
      yFins[f] = randint(25, 425)
    xFins[f] -= 4

def drawBall():
  global penguin, seconds, fish, score_text, pool, hunger_bar, gameStillGoing, penguin_baby, deltaT, babies
  hunger_bar = []

  fish = s.create_image(xFish, yFish, image = fish_img)
  penguin = s.create_image(xPenguin, yPenguin, image = penguin_img)
  for b in range(num_baby):
    babies[b] = s.create_image(xBaby[b], yBaby[b], image = penguin_baby_img)

  hunger_y = 10
  for b in range(num_baby):
    if hunger_baby[b] < 10-2*hunger_state:
      gameStillGoing = False
    elif hunger_baby[b] < 33:
      hunger_bar.append(s.create_rectangle(10, hunger_y, 2*hunger_baby[b], hunger_y + 15, fill="red"))
    elif hunger_baby[b] < 66:
      hunger_bar.append(s.create_rectangle(10, hunger_y, 2*hunger_baby[b], hunger_y + 15, fill="orange"))
    else:
      hunger_bar.append(s.create_rectangle(10, hunger_y, 2*hunger_baby[b], hunger_y + 15, fill="green"))
    hunger_y += 20

  deltaT = int(time()) - originTime
  seconds = s.create_text(550, 25, text="Time: "+str(deltaT))
  score_text = s.create_text(525, 40, text="Collected Fish: "+str(num_fish))

  for f in range(len(xFins)):
    fins.append(create_fin(xFins[f], yFins[f]))

def countdown():
  for i in range(1, 4):
    start_time = s.create_text(300, 300, text=str(i), font=('Helvetica','75','bold'), fill="white")
    s.update()
    sleep(1)
    s.delete(start_time)
  

def runGame():
  root.bind("<Button-1>", "")
  setInitialValues()
  playSound()
  
  drawBall()
  s.update()
  
  countdown()
  
  while gameStillGoing == True:
    updatePosition()  #This only moves the ball once
    
    s.update()
    sleep(0.03)
    s.delete(penguin, seconds, fish, score_text)
    for b in range(num_baby):
      s.delete(babies[b])
      s.delete(hunger_bar[b])
    for f in range(len(fins)):
      s.delete(fins[f])
    drawBall()
    
  s.delete("all")
  source.paused = True
  stopGame()

root.after(0, startScreen)

s.bind("<Key>", keyHandler)
s.bind("<KeyRelease>", keyUpHandler)

s.pack()
s.focus_set()
root.mainloop()
