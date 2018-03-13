import random
import sys
from Tkinter import *
 
class Model:
  def __init__(self,row,col):
    self.width=col
    self.height=row
    self.items=[[0 for c in range(col)] for r in range(row)]
 
  def setItemValue(self,r,c,value):

    self.items[r][c]=value;
 
  def checkValue(self,r,c,value):
    if self.items[r][c]!=-1 and self.items[r][c]==value:
      self.items[r][c]=-1 
      return True
    else:
      return False
     
  def countValue(self,r,c,value):
    count=0
    if r-1>=0 and c-1>=0:
      if self.items[r-1][c-1]==1:count+=1
    if r-1>=0 and c>=0:
      if self.items[r-1][c]==1:count+=1
    if r-1>=0 and c+1<=self.width-1:
      if self.items[r-1][c+1]==1:count+=1
    if c-1>=0:
      if self.items[r][c-1]==1:count+=1
    if c+1<=self.width-1 :
      if self.items[r][c+1]==1:count+=1
    if r+1<=self.height-1 and c-1>=0:
      if self.items[r+1][c-1]==1:count+=1
    if r+1<=self.height-1 :
      if self.items[r+1][c]==1:count+=1
    if r+1<=self.height-1 and c+1<=self.width-1:
      if self.items[r+1][c+1]==1:count+=1
    return count
 
   
class Mines(Frame):
  def __init__(self,m,master=None):
    Frame.__init__(self,master)
    self.model=m
    self.initmine()
    self.grid()
    self.createWidgets()
 
  
   
  def createWidgets(self):
    #top=self.winfo_toplevel()
    #top.rowconfigure(self.model.height*2,weight=1)
    #top.columnconfigure(self.model.width*2,weight=1)
    self.rowconfigure(self.model.height,weight=1)
    self.columnconfigure(self.model.width,weight=1)
    self.buttongroups=[[Button(self,height=1,width=2) for i in range(self.model.width)]
              for j in range(self.model.height)]
    for r in range(self.model.width):
      for c in range(self.model.height):
        self.buttongroups[r][c].grid(row=r,column=c)
        self.buttongroups[r][c].bind('<Button-1>',self.clickevent)
        self.buttongroups[r][c]['padx']=r
        self.buttongroups[r][c]['pady']=c
 
  def showall(self):
    for r in range(model.height):
      for c in range(model.width):
        self.showone(r,c)
 
  def showone(self,r,c):
    if model.checkValue(r,c,0):
      self.buttongroups[r][c]['text']=model.countValue(r,c,1)
    else:
      self.buttongroups[r][c]['text']='Mines'
 
  def recureshow(self,r,c):
    if 0<=r<=self.model.height-1 and 0<=c<=self.model.width-1:
      if model.checkValue(r,c,0) and model.countValue(r,c,1)==0:
        self.buttongroups[r][c]['text']=''
        self.recureshow(r-1,c-1)
        self.recureshow(r-1,c)
        self.recureshow(r-1,c+1)
        self.recureshow(r,c-1)
        self.recureshow(r,c+1)
        self.recureshow(r+1,c-1)
        self.recureshow(r+1,c)
        self.recureshow(r+1,c+1)
      elif model.countValue(r,c,1)!=0:
        self.buttongroups[r][c]['text']=model.countValue(r,c,1)
    else:
      pass
         
       
  def clickevent(self,event):
    r=int(str(event.widget['padx']))
    c=int(str(event.widget['pady']))
    if model.checkValue(r,c,1):
      self.showall()
    else:
      self.recureshow(r,c)
     
     
  def initmine(self):
    r=random.randint(1,model.height/model.width+2)
    for r in range(model.height):
      for i in range(2):
        rancol=random.randint(0,model.width-1)
        model.setItemValue(r,rancol,1)
 
   
  def printf(self):
    for r in range(model.height):
      for c in range(model.width):
        print model.items[r][c],
      print '/n'
       
 
def new(self):
  pass
 
if __name__=='__main__':
  model=Model(10,10)
  root=Tk()
   
  
  menu = Menu(root)
  root.config(menu=menu)
  filemenu = Menu(menu)
  menu.add_cascade(label="File", menu=filemenu)
  filemenu.add_command(label="New",command=new)
  filemenu.add_separator()
  filemenu.add_command(label="Exit", command=root.quit)
 
  
  m=Mines(model,root)
  
  root.mainloop()import random
import sys
from Tkinter import *
 
class Model:
  def __init__(self,row,col):
    self.width=col
    self.height=row
    self.items=[[0 for c in range(col)] for r in range(row)]
 
  def setItemValue(self,r,c,value):

    self.items[r][c]=value;
 
  def checkValue(self,r,c,value):
    if self.items[r][c]!=-1 and self.items[r][c]==value:
      self.items[r][c]=-1 
      return True
    else:
      return False
     
  def countValue(self,r,c,value):
    count=0
    if r-1>=0 and c-1>=0:
      if self.items[r-1][c-1]==1:count+=1
    if r-1>=0 and c>=0:
      if self.items[r-1][c]==1:count+=1
    if r-1>=0 and c+1<=self.width-1:
      if self.items[r-1][c+1]==1:count+=1
    if c-1>=0:
      if self.items[r][c-1]==1:count+=1
    if c+1<=self.width-1 :
      if self.items[r][c+1]==1:count+=1
    if r+1<=self.height-1 and c-1>=0:
      if self.items[r+1][c-1]==1:count+=1
    if r+1<=self.height-1 :
      if self.items[r+1][c]==1:count+=1
    if r+1<=self.height-1 and c+1<=self.width-1:
      if self.items[r+1][c+1]==1:count+=1
    return count
 
   
class Mines(Frame):
  def __init__(self,m,master=None):
    Frame.__init__(self,master)
    self.model=m
    self.initmine()
    self.grid()
    self.createWidgets()
 
  
   
  def createWidgets(self):
    #top=self.winfo_toplevel()
    #top.rowconfigure(self.model.height*2,weight=1)
    #top.columnconfigure(self.model.width*2,weight=1)
    self.rowconfigure(self.model.height,weight=1)
    self.columnconfigure(self.model.width,weight=1)
    self.buttongroups=[[Button(self,height=1,width=2) for i in range(self.model.width)]
              for j in range(self.model.height)]
    for r in range(self.model.width):
      for c in range(self.model.height):
        self.buttongroups[r][c].grid(row=r,column=c)
        self.buttongroups[r][c].bind('<Button-1>',self.clickevent)
        self.buttongroups[r][c]['padx']=r
        self.buttongroups[r][c]['pady']=c
 
  def showall(self):
    for r in range(model.height):
      for c in range(model.width):
        self.showone(r,c)
 
  def showone(self,r,c):
    if model.checkValue(r,c,0):
      self.buttongroups[r][c]['text']=model.countValue(r,c,1)
    else:
      self.buttongroups[r][c]['text']='Mines'
 
  def recureshow(self,r,c):
    if 0<=r<=self.model.height-1 and 0<=c<=self.model.width-1:
      if model.checkValue(r,c,0) and model.countValue(r,c,1)==0:
        self.buttongroups[r][c]['text']=''
        self.recureshow(r-1,c-1)
        self.recureshow(r-1,c)
        self.recureshow(r-1,c+1)
        self.recureshow(r,c-1)
        self.recureshow(r,c+1)
        self.recureshow(r+1,c-1)
        self.recureshow(r+1,c)
        self.recureshow(r+1,c+1)
      elif model.countValue(r,c,1)!=0:
        self.buttongroups[r][c]['text']=model.countValue(r,c,1)
    else:
      pass
         
       
  def clickevent(self,event):
    r=int(str(event.widget['padx']))
    c=int(str(event.widget['pady']))
    if model.checkValue(r,c,1):
      self.showall()
    else:
      self.recureshow(r,c)
     
     
  def initmine(self):
    r=random.randint(1,model.height/model.width+2)
    for r in range(model.height):
      for i in range(2):
        rancol=random.randint(0,model.width-1)
        model.setItemValue(r,rancol,1)
 
   
  def printf(self):
    for r in range(model.height):
      for c in range(model.width):
        print model.items[r][c],
      print '/n'
       
 
def new(self):
  pass
 
if __name__=='__main__':
  model=Model(10,10)
  root=Tk()
   
  
  menu = Menu(root)
  root.config(menu=menu)
  filemenu = Menu(menu)
  menu.add_cascade(label="File", menu=filemenu)
  filemenu.add_command(label="New",command=new)
  filemenu.add_separator()
  filemenu.add_command(label="Exit", command=root.quit)
 
  
  m=Mines(model,root)
  
  root.mainloop()
