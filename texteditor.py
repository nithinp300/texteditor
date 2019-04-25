from Tkinter import *
import tkFileDialog
root = Tk("Text Editor")
text = Text(root)
text.grid()
savelocation = "none"

# creates a new file and writes to it
def saveas():
	global text
	global savelocation
	t = text.get("1.0", "end-1c")
	savelocation = tkFileDialog.asksaveasfilename()
	file1 = open(savelocation, "w")
	file1.write(t)
	file1.close()
button = Button(root, text="Save As", command=saveas)
button.grid()

# opens a textedit file
def openfile():
	global text
	global savelocation
	savelocation = tkFileDialog.askopenfilename()
	file1 = open(savelocation, "r")
	text.insert("1.0", file1.read())
	file1.close()
button = Button(root, text="Open", command=openfile)
button.grid()

# overwrites the file that is currenly opened
def save():
	global text
	t = text.get("1.0", "end-1c")
	file1 = open(savelocation, "w")
	file1.write(t)
	file1.close()
button = Button(root, text="Save", command=save)
button.grid()

# changes font style
def fontArial():
	global text
	text.config(font="Arial")
def fontCourier():
	global text
	text.config(font="Courier")
font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
arial = IntVar()
courier = IntVar()
font.menu.add_checkbutton(label="Arial", variable=arial,
command=fontArial)
font.menu.add_checkbutton(label="Courier", variable=courier,
command=fontCourier)

root.mainloop()