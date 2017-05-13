"""
Write a GUI program that converts Celsius temperatures to Fahrenheit
temperatures. The user should be able to enter a Celsius temperature,
click a button, and then see the equivalent Fahrenheit temperature.
Use the following formula to make the conversion:

    F = (9/5)(C)+32

F is the Fahrenheit temperature and C is the Celsius temperature.
"""
"""
Joseph Schwabauer
More Practice with tkinter using Python
5/9/2017
"""
import tkinter

class CtoF:
    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        #create three frames
        self.celsius_frame = tkinter.Frame(self.main_window)
        self.submit_frame = tkinter.Frame(self.main_window)
        self.fahrenheit_frame = tkinter.Frame(self.main_window)
        self.answer_frame = tkinter.Frame(self.main_window)

        #create and pack label and entry for the Celcius widgets
        self.celsius_label = tkinter.Label(self.celsius_frame, text="Enter degrees in Celsius")
        self.celsius_entry = tkinter.Entry(self.celsius_frame, width=10)
        self.celsius_label.pack(side="left")
        self.celsius_entry.pack(side="left")

        #create and pack button widget
        self.submit_button = tkinter.Button(self.submit_frame, text="submit", command=self.calcCtoF)
        self.submit_button.pack()

        #create the pack label for the Fahrenheit widget and the answer 
        self.fahrenheit_label = tkinter.Label(self.fahrenheit_frame, text="Degrees in Fahrenheit: ")
        self.answer = tkinter.StringVar()
        self.answer_label = tkinter.Label(self.answer_frame, textvariable = self.answer)
        self.fahrenheit_label.pack(side="left")
        self.answer_label.pack(side="left")

        
        #pack the frames
        self.celsius_frame.pack()
        self.submit_frame.pack()
        self.fahrenheit_frame.pack()
        self.answer_frame.pack()
        
        #start the main loop
        tkinter.mainloop()

    def calcCtoF(self):
        self.celsius = float(self.celsius_entry.get())

        #convert celsius to fahrenheit
        self.calc = (9/5) * self.celsius + 32

        #store the value of self.calc in the StringVar object referenced by answer
        self.answer.set(self.calc)


myCtoF = CtoF()
        

        
