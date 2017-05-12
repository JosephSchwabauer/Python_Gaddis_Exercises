"""
PYTHON GUI PRACTICE
Create a GUI that lists three words as buttons
upon clicking each button, an method is called
to display the english translation of the word
5/3/2017
"""
import tkinter

class latinGUI:
    def __init__(self):
    #create the main window, an instance of the tkinter module's Tk class
        self.main_window = tkinter.Tk()
        self.bottom_frame = tkinter.Frame()
        

   #create 5 frames 
        self.sinister_frame = tkinter.Frame(self.main_window)
        self.dexter_frame = tkinter.Frame(self.main_window)
        self.medium_frame = tkinter.Frame(self.main_window)
        self.top_frame = tkinter.Frame()
        self.prompt_label = tkinter.Label(self.top_frame, text="English Translationis:")


    #Create button widgets
        self.sinister_button = tkinter.Button(self.sinister_frame, text="sinister", command=self.translate_sin)
        self.medium_button = tkinter.Button(self.medium_frame, text="medium", command=self.translate_cen)
        self.dexter_button = tkinter.Button(self.dexter_frame, text="dexter", command=self.translate_dex)
 
    #pack the buttons
        self.sinister_button.pack()
        self.medium_button.pack()
        self.dexter_button.pack()
        
        
    #pack the frames
        self.prompt_label.pack(side='top')
        self.sinister_frame.pack(side="top")
        self.medium_frame.pack(side="top")
        self.dexter_frame.pack(side="top")
        
        self.top_frame.pack()

   
    #enter the tkinter main loop
        tkinter.mainloop()

    #method to define and pack labels for translation
    def translate_sin(self):
        self.left_label = tkinter.Label(self.top_frame, text= "left")
        self.left_label.pack(side="top")

    def translate_dex(self):
        self.right_label = tkinter.Label(self.top_frame, text= "right")
        self.right_label.pack(side="top")

    def translate_cen(self):
        self.medium_label = tkinter.Label(self.top_frame, text= "middle")
        self.medium_label.pack(side="top")

       
        
#create an instance of the latinGUI class
translate = latinGUI()
                                    
