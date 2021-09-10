import tkinter as tk
from tkinter.font import Font
import datetime
import os


CURRENT_PATH = os.getcwd()

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!Error")
    popup.geometry("300x100")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):


        #Spinbox for hours
        self.spin_hour = tk.Spinbox(self, from_=0, to=23, width=5, justify=tk.RIGHT,
                                    font=Font(family='Helvetica', size=18, weight='bold'))
        self.spin_hour.grid(row=0, column=0, pady=(10,90))

        #Spinbox for minutes
        self.spin_min = tk.Spinbox(self, from_=0, to=59, width=5, justify=tk.RIGHT,
                                   font=Font(family='Helvetica', size=18, weight='bold'))
        self.spin_min.grid(row=0, column=1, pady=(10,90))

        #Hour/s Label
        self.labelHour = tk.Label(self, text="Hour/s")
        self.labelHour.place(x=30, y=43)

        #Minute/s Label
        self.labelMinute = tk.Label(self, text="Minute/s")      
        self.labelMinute.place(x=110, y=43)


        #Shutdown Button
        self.shutdown_photo = tk.PhotoImage(file = CURRENT_PATH + "\\data\\Shutdown.png", width=36, height=36)

        self.buttonShut = tk.Button(self, image= self.shutdown_photo, state=tk.NORMAL,
                                    command= lambda: [self.shutdown_func(), self.callback()])
        self.buttonShut.grid(row=1, column=0, pady=(0,40))


        #Reboot Button
        self.reboot_photo = tk.PhotoImage(file = CURRENT_PATH + "\\data\\Reboot.png", width=36, height=36)

        self.buttonReboot = tk.Button(self, image= self.reboot_photo, state=tk.NORMAL,
                                      command= lambda: [self.reboot_func(), self.callback()])
        self.buttonReboot.grid(row=1, column=1, pady=(0,40))
        
        #Cancel Button
        self.buttonCancel = tk.Button(self, text='Cancel', command=self.cancel_func, width=15)
        self.buttonCancel.place(x=27, y=190)
        
        #Timer Label
        self.labelOne = tk.Label(self, text="Welcome!", borderwidth=3, relief="ridge", width=20, height=3)
        self.labelOne.place(x=10, y=70)

        #Default value for timer
        self.remaining = 0

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining == -1:
            self.labelOne.configure(text="Welcome!")
        
        elif self.remaining <= 0:
            self.labelOne.configure(text="Time's up!")
        else:
            self.labelOne.configure(text=str(datetime.timedelta(seconds=self.remaining)))
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
         

    def get_sec(self):
        """Get Seconds from time."""
        return int(self.spin_hour.get()) * 3600 + int(self.spin_min.get()) * 60


    def shutdown_func(self):
        if self.get_sec() == 0:
            popupmsg('Set time')
        if int(self.spin_hour.get()) > 23 or int(self.spin_min.get()) > 59:
            popupmsg('Incorrect amount of hours or minutes')
        else:
            strTime = self.get_sec()
            os.system("shutdown -s -t %s" % strTime)
            self.countdown(self.get_sec())


    def reboot_func(self):
        if self.get_sec() == 0:
            popupmsg('Set time')
        if int(self.spin_hour.get()) > 23 or int(self.spin_min.get()) > 59:
            popupmsg('Incorrect amount of hours or minutes')
        else:
            strTime = self.get_sec()
            os.system("shutdown -r -t %s" % strTime)
            self.countdown(self.get_sec())


            
    def cancel_func(self):
        os.system("shutdown -a")
        self.remaining = -1
        self.buttonShut['state'] = tk.NORMAL
        self.buttonReboot['state'] = tk.NORMAL
        self.countdown
        

    def callback(self):
        self.buttonShut['state'] = tk.DISABLED
        self.buttonReboot['state'] = tk.DISABLED
        
   
        
root = tk.Tk()
root.title("CLSC v.1.0.8")
root.geometry("240x250")
root.resizable(False, False)
app = Application(master=root)
app.mainloop()
