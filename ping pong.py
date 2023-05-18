import turtle
window=turtle.Screen()
window.bgcolor("black")
window.title('ping pong')
window.setup(width=500,height=430)#ويدث طول والهاي هو العرض
window.tracer(0)
#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)#معناه ارسم شكل المضرب باسرع سرعة كل مرة تحدث فيها الشاشة
madrab1.shape("square")
madrab1.color('red')
madrab1.penup()#اذا تحرك الخط يرسم خطوط هذه الدالة تزيل ذلك الخط
madrab1.goto(-210,0)
madrab1.shapesize(stretch_wid=3,stretch_len=1)
#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)#معناه ارسم شكل المضرب باسرع سرعة كل مرة تحدث فيها الشاشة
madrab2.shape("square")
madrab2.color('blue')
madrab2.penup()#اذا تحرك الخط يرسم خطوط هذه الدالة تزيل ذلك الخط
madrab2.goto(210,0)
madrab2.shapesize(stretch_wid=3,stretch_len=1)
#ball
ball=turtle.Turtle()
ball.speed(0)#معناه ارسم شكل المضرب باسرع سرعة كل مرة تحدث فيها الشاشة
ball.shape("circle")
ball.color('white')
ball.penup()#اذا تحرك الخط يرسم خطوط هذه الدالة تزيل ذلك الخط
ball.goto(0,0)
ball.dx=0.2#معناه تحرك الكرية على جهة محور اكس يكون بمقدار ربع بيكسل
ball.dy=0.2#معناه تحرك الكرية على جهة محور واي يكون بمقدار ربع بكسل
#fonction of game
def up1():
  y=madrab1.ycor()#هذا يوجد لي مكان المضرب على جهة الواي في الشاشة
  y+=20
  madrab1.sety(y)
def down1():
  y=madrab1.ycor()#هذا يوجد لي مكان المضرب على جهة الواي في الشاشة
  y-=20
  madrab1.sety(y)
def up2():
  y=madrab2.ycor()#هذا يوجد لي مكان المضرب على جهة الواي في الشاشة
  y+=20
  madrab2.sety(y)
def down2():
  y=madrab2.ycor()#هذا يوجد لي مكان المضرب على جهة الواي في الشاشة
  y-=20
  madrab2.sety(y)
#keybord to game
window.listen()#معناه قادر يكون هناك ربط للعبة مع الكيبورد
window.onkeypress(up1,"z")
window.onkeypress(down1,"s")
window.onkeypress(up2,"Up")
window.onkeypress(down2,"Down")
#game loop
while True:
  window.update()#معناه كلما حدث اللوب  قم بتحديث الشاشة
  #move the ball
  ball.setx(ball.xcor()+ball.dx)#اختصرت نفس عمل الدوال up1 and 2 and down1 and 2
  ball.sety(ball.ycor()+ball.dy)
  #ball back to the inves place
  if ball.ycor()>205:
    ball.sety(205)
    ball.dy *= -1
  if ball.ycor()<-205:
    ball.sety(-205)
    ball.dy *= -1
  if ball.xcor()>240:
    ball.goto(0,0)
  if ball.xcor()<-240:
    ball.goto(0,0)
    #هل لمست الكرة المضرب
  if  230<ball.xcor()<240 and madrab2.ycor()-40<ball.ycor()<madrab2.ycor()+40:
    ball.setx(230)
    ball.dx *= -1
  if  -240<ball.xcor()<-230 and madrab1.ycor()-40<ball.ycor()<madrab1.ycor()+40:
    ball.setx(230)
    ball.dx *= -1