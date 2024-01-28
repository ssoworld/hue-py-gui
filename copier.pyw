#!/usr/bin/env python

import customtkinter as ctk
import PySimpleGUI as sg
import shutil
import json
from pathlib import Path
# ctk.set_appearance_mode('system')

# layout = [ [sg.Text("Hello world")],
#            [sg.Button('OK')] ]
          
# window = sg.Window('Window Title', layout)

# event, values = window.read()
class App(ctk.CTk):

   def __init__(self):
      super().__init__()
      self.geometry("500x500")
      self.title(self.updateTitle(self.readParam()))

      self.buttonA = ctk.CTkButton(self, command=self.buttonA_click, text="copy folder A")
      self.buttonB = ctk.CTkButton(self, command=self.buttonB_click, text="copy folder B")
      self.buttonA.grid(row=0, column=0, padx=20, pady=10)
      self.buttonB.grid(row=30, column=0, padx=20, pady=10)
      
         
   def buttonA_click(self):
      self.copyFolder("FolderA")
   
   def buttonB_click(self):
      self.copyFolder("FolderB")
      
   def copyFolder(self, folderName):
      self.rmDir("./Output")
      shutil.copytree(f'./{folderName}', "./Output")
      self.writeParam(folderName)
      self.title(self.updateTitle(folderName))
      
   def readParam(self):
      with open("./.params/params.json", "r") as inFile:
         obj = json.load(inFile)
      return obj.get("name")
   
   def writeParam(self, newValue):
      dict = {
         "name": newValue
      }
      
      with open("./.params/params.json", "w") as outfile:
         json.dump(dict, outfile)
      
   def updateTitle(self, name):
      return f'Example -  {name}'
   
   def rmDir(self, dirname):
      dirPath = Path(dirname)
      if dirPath.exists() and dirPath.is_dir():
         shutil.rmtree(dirPath)
   
app = App()
app.mainloop()