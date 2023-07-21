import turtle as t


t.setup(600,600)
t.hideturtle()
t.color('red')
t.pensize(4)

t.up()
t.goto(-250,-150)
t.down()
t.goto(-200,-150)
t.up()
t.goto(-225,-150)
t.down()
t.goto(-225,280)
t.fd(250)
t.lt(-90)
t.fd(50)

def krivo(pokusaj):
    if pokusaj==1:
        t.lt(-90)
        t.circle(40)
    if pokusaj==2:
        t.up()
        t.goto(25,150)
        t.down()
        t.circle(80)

rijec=t.textinput('Vješala','Unesi riječ za pogađanje')
greska=0
while greska<10:
    unos=t.textinput('Vješala','Unesi slovo za pogađanje ili cijelu riječ')
    if len(unos)==1:
        if not unos in rijec:
            greska=greska+1
            krivo(greska)
    else: 
        if unos==rijec:
            print('Pobjeda')
            break
        else:
            greska=greska+1
            krivo(greska)





        
