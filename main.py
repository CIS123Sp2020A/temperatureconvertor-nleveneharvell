#Nava Levene-Harvell
#Tempurature Converter 

import tkinter
import tkinter.messagebox

class TempConverter:
    def __init__(self):
        #main window
        self.mainWindow = tkinter.Tk()

        #two frames
        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        #user entry and label 
        self.promptLabel = tkinter.Label(self.topFrame,
                                        text = "Enter a temperature in Ferinheight:")
        self.tempEntry = tkinter.Entry(self.topFrame,
                                       width = 10)
        #pack the top
        self.promptLabel.pack(side = 'left')
        self.tempEntry.pack(side = 'left')

        #make the buttons
        self.calcButton = tkinter.Button(self.bottomFrame,
                                         text = "Convert",
                                         command = self.convert)
        self.quitButton = tkinter.Button(self.bottomFrame,
                                         text = "Quit",
                                         command = self.mainWindow.destroy)

        #pack buttons
        self.calcButton.pack(side = 'left')
        self.quitButton.pack(side = 'left')

        #pack frames
        self.topFrame.pack()
        self.bottomFrame.pack()

        tkinter.mainloop()

##convert f to c in temperature     
    def convert(self):

        #get temp val
        ferin = float(self.tempEntry.get())

        #convert f to c
        celsius = (ferin - 32) * (5/9)

        #display results
        tkinter.messagebox.showinfo("Results",
                                    str(ferin) +
                                    " Ferinheight is equal to " +
                                    str(celsius) + ' Celsuis.')

#instance of class
tempConv = TempConverter()
        
