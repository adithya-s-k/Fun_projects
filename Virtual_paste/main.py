import keyboard
import time

# The program gives you 5 seconds to place the curser on the application where you want to by pass the pasting restrictions.

time.sleep(5)

f = open("paste.txt","r",encoding='utf-8')

paste_text = f.readlines()
print(paste_text)

for i in paste_text:
        keyboard.write(str(i))

f.close()