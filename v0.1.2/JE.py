import os
import time
os.system ("sudo pigpiod")
time.sleep (1)
import pigpio
import pygame

escinput=input('An welchem pin ist der ESC angeschlossen?')
print ('Dein ESC liegt an am PIN:')
print (escinput)
ESC=4
pi = pigpio.pi();
pi.set_servo_pulsewidth (ESC, 0)
max_value = 2000
min_value = 700

print ("Geschrieben am 6. Dezember 2018 mit folgendem PI")
time.sleep (0.5)
print ("Raspberry Pi 3B")
time.sleep (0.5)
print ("Mein os:")
time.sleep (0.5)
print ("PRETTY_NAME=Raspbian GNU/Linux 9 (stretch)")
print ("NAME=Raspbian GNU/Linux")
print ("VERSION_ID=9")
print ("VERSION=9 (stretch)")
print ("ID=raspbian")
print ("ID_LIKE=debian")
print ("HOME_URL=http://www.raspbian.org/")
print ("SUPPORT_URL=http://www.raspbian.org/RaspbianForums")
print ("BUG_REPORT_URL=http://www.raspbian.org/RaspbianBugs")
print ()
print ()
time.sleep (1)

print ("Hinweis: Falls dieses Skript nicht funktioniert, musst die die pygame library installieren. Dies geschieht mit dem Command:")
print ("sudo apt-get install python-pygame")
print ()
time.sleep (1)
print ("Aber das ist bei der vollen Version Raspbian eigentlich immer dabei. Falls du die willst: apt-get upgrade")
print ()
print ("Du kannst bis jetzt nur die Pfeiltasten benutzten")
print ()
input ("Drücke Enter zum ausführen des Scriptes")



print ()
print ("MENÜ:")
time.sleep (0.5)
print ("1. Kalibrierung")
time.sleep (0.5)
print ("2. ESC Programmierung (irrelevant)")
time.sleep (0.5)
print ("3. Steuerung")
time.sleep (0.5)
print ("4. ARM")
time.sleep (0.5)
print ("5. Beenden")
time.sleep (0.5)
print ("Zur Auswahl bitte Zahl eingeben und ENTER drücken. Aktuell funktioniert nur 3")

def steuerung():
    pygame.init()
    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.key.set_repeat(1, 25)
    pygame.display.set_caption("While Key Pressed für Jakob")
    clock = pygame.time.Clock()
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    gameDisplay.fill (black)
    pygame.display.update()
    speed = 500
    print ("Pfeiltaste HOCH zum erhöhen der Geschwindigkeit, Pfeiltaste RUNTER zum verringern")
    while True:
    #Das sorgt dafür, dass die FPS angepasst werden und der PI mehr leistung hat. Kannst ja mal damit rumspielen und auf die Prozessor auslastung gucken. (Und natürlich das key repeat anpassen)
        clock.tick(25)
        pi.set_servo_pulsewidth(ESC, speed)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if speed < 2500:
                        speed += 25
                        print (speed)
                    else:
                        print ("Maximale Geschwindigkeit erreicht")
                if event.key == pygame.K_DOWN:
                    if speed > 500:
                        speed -= 25
                        print (speed)
                    else:
                        print ("Minimale Geschwindigkeit erreicht")
        #Das ist optinal. Da hatte ich zu viel Freizeit
            #elif event.type == pygame.KEYUP:
                #if event.key == pygame.K_UP:
                    #print ()
                #if event.key == pygame.K_DOWN:
                    #print ()

inp = input()
if inp == "3":
    print ("Du hast STEUERUNG gewählt. Das programm ist noch etwas träge")
    time.sleep (2)
    steuerung()
else:
    print ("Noch nicht implemitiert")
