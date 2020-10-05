import webbrowser
import keyboard
import time

# yapımcının notu : # config yazmayanlara lutfen dokunmayınız
# eğer lag yaparsa exit() yapın yada görevi sonlandırın
zoom  = 'https://zoom.us' #config
x = 1
while True:
    time. sleep(1)
    webbrowser.open(zoom, new=0, autoraise=False)
    x += 1
if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            exit()




