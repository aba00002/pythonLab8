from gfxhat import lcd,  fonts, backlight
from click import getchar

backlight.set_all(255, 255, 200)
backlight.show()
lcd.clear()
lcd.show()

#Write a program that reads a character from the user and displays the associate character on the gfxHat at the coordinates of your choice. Characters not present in the dictionary are ignored and a message is displayed on the computer screen.
x = 3
y = 3
k = getchar()
try:
    f = open("font3.txt","r")
    for row in f:
        key = row[-2]
        hexaDecimalValue = row[2:-3]
        b = bin(int(hexaDecimalValue, 16))
        c = b[2:]
        rows = 8
        col = 8
        newList = [c[col*i : col*(i+1)] for i in range(rows)]
        if key == k:
            for i in range(0, len(newList)):
                for j in range(0, len(newList[i])):
                    lcd.set_pixel(x+j,y+i,newList[i][j])
                    lcd.show()

except:
    print("Looks like you didnt enter an existing key. Please enter again")