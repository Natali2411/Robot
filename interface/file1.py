from tkinter import *

class Interface():
   def frameSaveInfo(self):
      root = Tk()
      root.title("Robot")
      L1 = Label(root, text="Currency pair").pack(side=LEFT)
      E1 = Entry(root).pack(side=LEFT)
      button = Button(root, text ="Save analitic info", width=20,height=2).pack(side=BOTTOM)
      root.mainloop()


if __name__ == "__main__":
   obj = Interface().frameSaveInfo()