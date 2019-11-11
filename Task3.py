#from gfxhat import lcd, backlight
#backlight.set_all(255, 255, 200)
#backlight.show()
#lcd.clear()
#lcd.show()

#Write a function generateDictionary that reads the file font3.txt and generate a dictionary where the key is the character ane the vaue is the 8*8 bit list representation of the character.
def generateDictionary():
    f = open("font3.txt","r")
    for row in f:
        key = row[-2]
        hexaDecimalValue = row[2:-3]
        b = bin(int(hexaDecimalValue, 16))
        c = b[2:]
        rows = 8
        col = 8
        newList = [c[col*i : col*(i+1)] for i in range(rows)]
        print(key, newList)
#invoke the function        
generateDictionary()



     
     
