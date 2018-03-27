from tkinter import *
from models_binance.save_data import SaveData

class Interface(SaveData):
   obj = SaveData()
   def frameSaveInfo(self):
      root = Tk()
      root.title("Robot")
      #L1 = Label(root, text="Currency pair").pack(side=LEFT)
      #E1 = Entry(root).pack(side=LEFT)
      button = Button(root, command=print('regtreg') ,text ="Save analitic info", width=20,height=2)
      button.bind("<Key>")
      button.pack()
      root.mainloop()


if __name__ == "__main__":
   obj = Interface().frameSaveInfo()