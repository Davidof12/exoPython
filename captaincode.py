#git config --local user.name "NOM"
#git config --local user.email "EMAIL"

import string
import random
import datetime
from random import randrange, uniform
import calendar
import time 

print("                                                                      ")
print("-  C A P T A I N  |  C O D E  - ")
print("                                                                      ")
print ("WELCOME_BIENVENUE_歓迎_BONI | DD3 INTELLIGENCE AGENCY | SPECIAL REPORT ")
print("                                                                      ")
print("------------------------------------------------------------------------")

now = datetime.datetime.now()
print ("TIME | ", now)
print("------------------------------------------------------------------------")
print("                                                                      ")
cal = calendar.month(2018, 8)
print(cal)
print("------------------------------------------------------------------------")

password  = "bristow15"
boncode = int and str(input("ENTER AGENT ID | "))

if password == boncode:
    print("AUTORISED ACCESS | ")
elif boncode != password:
    print("ACCESS DENIED | ")

dict = {'NAME': 'Agent Sydney Bristow', 'AGE': 28, 'STATUS': 'Active'}
dict['NAME'] = "Agent Sydney Bristow"; 
dict['AGE'] = 28; 
dict['LAST MISSION'] = "Industrie de la paix (african areas)"; 
dict['STATUS'] = "ACTIVE"; 

print("NAME: ", dict['NAME'])
print("AGE: ", dict['AGE'])
print("LAST MISSION: ", dict['LAST MISSION'])
print("STATUS: ", dict['STATUS'])

print("------------------------------------------------------------------------")
plain_text = input("CLASSIFIED MESSAGE | ")
print("------------------------------------------------------------------------")
encrypted_text = ("ENCRYPTON | To copy: ")
for c in plain_text:
    x = ord(c)
    x = x + 12 - 6 + 3 - 4 
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)
print("------------------------------------------------------------------------")
print("                                                                      ")
print("- C A P T A I N  |  D E C R Y P T O N  - ")
print("                                                                      ")
encrypted_text = input("INSERT ENCRYPTON | ")
print("                                                                      ")
plain_text = ("DECRYPTED MESSAGE | ") 
for c in encrypted_text:
    x = ord(c)
    x = x - 12 + 6 - 3 + 4 
    c2 = chr(x)
    plain_text = plain_text + c2
print("------------------------------------------------------------------------")
print ("ANALYSING... | ")
print("------------------------------------------------------------------------")
print("                                                                      ")
print(plain_text) 
print("------------------------------------------------------------------------")

choix = int(input ("COPY (1) OR DESTROY (2) THIS INTEL? "))

if choix == 1:
    print("                                                                      ")
    print ("THANKS. THIS INTEL AS BEEN CLASSIFIED")
    print("                                                                      ")
    print ("YOUR GENERATED FILE CODE IS: ", random.randrange(52,10000007))
    print("                                                                      ")
    print("*** This message will be destroy in 20 secondes ***") 
    print("                                                                      ")
    print ("// DD3 INTELLIGENCE AGENCY | TONI CAPTAIN INC. | SPECIAL REPORT // ")
    print("                                                                      ")
    StopIteration

roll_again = "yes"
var = "no"
f = int and str(input("DESTROY NOW? | (TAP ENTER): "))
[random.randrange(120) for x in range(12546)]

while roll_again == "yes":
    list = [ 'DD3', random.randrange(5458), 9.687, 'captain', random.randrange(108) ]
    tinylist = [random.randrange(5458), 'captain']
    print("                                                                      ")
    print (random.randrange(38768)) 
    OverflowError
    print("                                                                      ")
    print(list[2:])
    print("                                                                      ")
    print(list[1:3])
    print ("DO NOT DISCONNECT | INTEL DESTRUCTION LOADING ")
    print("                                                                      ")
    print(list[0])
    print(" *** This message will be destroy in 30 secondes *** ") 
    print(list + tinylist)
    print("                                                                      ")
    print(list) 
    print ("// DD3 INTELLIGENCE AGENCY | TONI CAPTAIN INC. | SPECIAL REPORT // ")

    var == roll_again 
    print("INTEL AS BEEN DESTROYED")
   

    print("                                                                      ")
    print (random.randrange(5876421358)) 
    print("                                                                      ")
    
    print ("INTEL AS BEEN DESTROYED")
    print("                                                                      ")
    print(" *** This message will be destroy in 30 secondes ***" ) 
    print("                                                                      ")
    print ("// DD3 INTELLIGENCE AGENCY | TONI CAPTAIN INC. | SPECIAL REPORT // ")



#####BOUTON ID
def add():
    a = float(num1In.get("1.0"))
    b = float(num2In.get("1.0"))
    ansOut['text'] = str(a + b)

#defines window
tk = Tkinter.Tk(None)

# creates a frame (a place on which to put components)
frame = Tkinter.Frame(tk, borderwidth=2)

#packs frame to fill window
frame.pack(expand=1)

#defines a label (static text to show purporse of input)
num1Lb = Tkinter.Label(frame, text = "AGENT ID | ")

#places component on a grid (colum span shows how many colums it goes through)
num1Lb.grid(row=0, column=0, columnspan=2)

#defines a text input box (a place to recieve text input)
num1In = Tkinter.Text(frame, height=1, width=31)

#places component on a grid
num1In.grid(row=0, column=2, columnspan=2)

#same as with number 1
num2Lb = Tkinter.Label(frame, text = "PASSWORD | ")
num2Lb.grid(row=1, column=0, columnspan=2)
num2In = Tkinter.Text(frame, height=1, width=31)
num2In.grid(row=1, column=2, columnspan=2)

#defines a button (fommand is function but without brackets)
btnAdd = Tkinter.Button(frame, text="Add", command=add)

#places component on a grid
btnAdd.grid(row=3, column=0, columnspan=1)


#starts window
tk.mainloop()


#####MISE EN PAGE APPLI TEST1
import Tkinter

app= Tkinter.Tk()
frame=Tkinter.Frame(app)
frame.pack()

rightframe=Tkinter.Frame(app,width="300")
rightframe.pack(side="right")

txtLabel=Tkinter.Label(frame,text="- CAPTAIN | CODE - ")
txtLabel.pack()

redbutton = Tkinter.Label(rightframe, text="ENCRYPTON", fg="blue")
redbutton.pack( side = "top")
greenbutton = Tkinter.Label(rightframe, text="DECRYPTON", fg="grey")
greenbutton.pack( side = "top")

leftframe=Tkinter.Frame(app)
leftframe.pack(side="bottom")

redbutton1 = Tkinter.Button(leftframe, text="ENCODE", fg="red")
redbutton1.pack( side = "left")
greenbutton1 = Tkinter.Button(leftframe, text="TARGETS", fg="brown")
greenbutton1.pack( side = "left")
bluebutton1 = Tkinter.Button(leftframe, text="MAPS", fg="blue")
bluebutton1.pack( side = "left" )

app.mainloop()


######MESSAGE LISTING

from Tkinter import *

class INTELLIGENCE_DATA_BASE(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                         relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)

    def curselection(self):
        return self.lists[0].curselection(  )

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: return apply(map, [None] + result)
        return result

    def index(self, index):
        self.lists[0].index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size(  )

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

if __name__ == '__main__':
    tk = Tk(  )
    Label(tk, text='INTELLIGENCE_DATA_BASE').pack(  )
    mlb = INTELLIGENCE_DATA_BASE(tk, (("CLASSIFIED MESSAGE |", 40), ("AGENT | ", 20), ("DATE | ", 10)))
    for i in range(1000):
      mlb.insert(END, 
          ("CONFIDENTIAL | : %d" % i, 'John Doe', '10/10/%04d' % (1900+i)))
    mlb.pack(expand=YES,fill=BOTH)
tk.mainloop( )


##### COLOR CODE
import Tkinter

FONT = ('helvetica',24,'bold')

def main():
    mainWindow = Tkinter.Tk()
    mainWindow.title("- COLOR CODE - ")
    mainFrame = Tkinter.Frame(mainWindow)
    mainFrame.pack(side=Tkinter.RIGHT, expand=Tkinter.YES, fill=Tkinter.BOTH)
    colorSpace = ColorCanvas(mainWindow)
    redScale   = Tkinter.Scale(mainFrame,orient = Tkinter.HORIZONTAL,from_=0,to=255,relief = Tkinter.RAISED,length=300,sliderlength=20,resolution=1, command=colorSpace.setRed)
    greenScale = Tkinter.Scale(mainFrame,orient = Tkinter.HORIZONTAL,from_=0,to=255,relief = Tkinter.RAISED,length=300,sliderlength=20,resolution=1, command=colorSpace.setGreen)
    blueScale  = Tkinter.Scale(mainFrame,orient = Tkinter.HORIZONTAL,from_=0,to=255,relief = Tkinter.RAISED,length=300,sliderlength=20,resolution=1, command=colorSpace.setBlue)
    redLabel = Tkinter.Label(mainFrame, text="RED |")
    greenLabel = Tkinter.Label(mainFrame, text="GREEN |")
    blueLabel = Tkinter.Label(mainFrame, text="BLUE |")
    colorSpace.addScales(redScale, greenScale, blueScale)
    colorSpace.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
    redLabel.pack(side=Tkinter.TOP)
    redScale.pack(side=Tkinter.TOP, expand=Tkinter.YES, fill=Tkinter.Y)
    greenLabel.pack(side=Tkinter.TOP)
    greenScale.pack(side=Tkinter.TOP, expand=Tkinter.YES, fill=Tkinter.Y)
    blueLabel.pack(side=Tkinter.TOP)
    blueScale.pack(side=Tkinter.TOP, expand=Tkinter.YES, fill=Tkinter.Y)
    mainWindow.protocol('WM_DELETE_WINDOW', mainWindow.destroy)
    mainWindow.mainloop()

class ColorCanvas(Tkinter.Canvas):
    def __init__(self, master, *args, **kwargs):
        Tkinter.Canvas.__init__(self, master, *args, **kwargs)
        self.__redScale, self.__greenScale, self.__blueScale = [False] * 3
        self.__t = self.create_text(10, 10, text='', font=FONT, anchor=Tkinter.NW)
        try:
            self.__red   = int(kwargs['background'][1:3], 16)
            self.__green = int(kwargs['background'][3:5], 16)
            self.__blue  = int(kwargs['background'][5:], 16)
        except:
            self.__red, self.__green, self.__blue = [0] * 3

    def addScales(self, redScale, greenScale, blueScale):
        self.__redScale, self.__greenScale, self.__blueScale = redScale, greenScale, blueScale

    def toHex(self, integer):
        if integer < 16:
            return '0%s' % hex(integer)[2:]
        else:
            return '%s' % hex(integer)[2:]

    def showHexColor(self, colorstring):
        if (self.__red + self.__green + self.__blue) / 3 > 128:
            textcolor = '#000000'
        else:
            textcolor = '#ffffff'
        self.itemconfigure(self.__t, text=colorstring, fill=textcolor)

    def setRed(self, event=None):
        if self.__redScale:
            self.__red = self.__redScale.get()
            colorstring = '#%s%s%s' % (self.toHex(self.__red), self.toHex(self.__green), self.toHex(self.__blue))
            self.configure(background=colorstring)
            self.showHexColor(colorstring)

    def setGreen(self, event=None):
        if self.__greenScale:
            self.__green = self.__greenScale.get()
            colorstring = '#%s%s%s' % (self.toHex(self.__red), self.toHex(self.__green), self.toHex(self.__blue))
            self.configure(background=colorstring)
            self.showHexColor(colorstring)

    def setBlue(self, event=None):
        if self.__blueScale:
            self.__blue = self.__blueScale.get()
            colorstring = '#%s%s%s' % (self.toHex(self.__red), self.toHex(self.__green), self.toHex(self.__blue))
            self.configure(background=colorstring)
            self.showHexColor(colorstring)

main()

### ENCODE YOUR SIZE
from Tkinter import *

def printer(event):
    global s # use global StringVar to show the results
    import random

    r_sample = random.sample(range(a.get(), b.get()), c.get())

    # set the s variable with the random sample
    s.set(",".join(map(str,r_sample)))
    return

root = Tk()

s = StringVar()

# IntVars added here
a = IntVar()
b = IntVar()
c = IntVar()


lab = Label(root, text="GARMENT LENGHT", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=a)
lab.pack()
ent.pack()

lab = Label(root, text="CHEST", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=b)
lab.pack()
ent.pack()

lab = Label(root, text="SLEEVES", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=c)
lab.pack()
ent.pack()

lab = Label(root, text="WAIST", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=c)
lab.pack()
ent.pack()

lab = Label(root, text="NECK", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=c)
lab.pack()
ent.pack()

lab = Label(root, text="PANT LENGHT", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=c)
lab.pack()
ent.pack()

but = Button(root, text="MADE BY MEASURE",
             width=20,height=5,
             bg="green",fg="yellow")
but.bind("<Button-1>", printer)
but.pack()

lab = Label(root, text="| YOUR SIZE CODE | ", font="Arial 10")
ent = Entry(root,width=20,bd=3, textvariable=s)
lab.pack()
ent.pack()

root.mainloop()

#### STORY APPAREL
from Tkinter import *           # Importing the Tkinter (tool box) library 
root = Tk()                     # Create a background window
                                # Create a list
print("| STORY APPAREL | ")
li = 'NEWS GADJET CAP JACKETS SWEAT TEE'.split()
listb = Listbox(root)           # Create a listbox widget
for item in li:                 # Insert each item within li into the listbox
    listb.insert(0,item)

listb.pack()                    # Pack listbox widget
root.mainloop()                 # Execute the main event handler


#### ENCODER INPUT
import os
import sys
import fileinput

print ("Text to search for:")
textToSearch = input( "> " ) 

print ("Text to replace it with:")
textToReplace = input( "> " )

print ("File to perform Search-Replace on:")
fileToSearch  = input( "> " )
#fileToSearch = 'D:\dummy1.txt'

tempFile = open( fileToSearch, 'r+' )

for line in fileinput.input( fileToSearch ):
    if textToSearch in line :
        print('Match Found')
    else:
        print('Match Not Found!!')
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()


input( '\n\n Press Enter to exit...' )


#### Afficheur d'heure et date
import Tkinter
import time

class Clock(Tkinter.Label):

    def __init__(self, parent=None, seconds=True, colon=False):
    
        Tkinter.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S')
        else:
            self.time     = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)

if __name__ == "__main__":

    window = Tkinter.Tk()
    frame  = Tkinter.Frame(window, width=400, height=400 )
    frame.pack()

    Tkinter.Label(frame, text="TIME | ").pack()

    clock1 = Clock(frame)
    clock1.pack()
    clock1.configure(bg='green',fg='yellow',font=("helvetica",35))

    Tkinter.Label(frame, text=" ").pack()

    Tkinter.Label(frame, text="DATE | ").pack()

    clock2 = Clock(frame, seconds=False, colon=True)
    clock2.pack()
    clock2.configure(bg='red',fg='white',font=("arial",20))

    Tkinter.Label(frame, text=" ").pack()

    Tkinter.Label(frame, text="| DD3 INTELLIGENCE AGENCY 2018 | ").pack()

window.mainloop()


