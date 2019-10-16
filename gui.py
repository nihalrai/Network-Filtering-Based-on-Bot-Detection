import os
import sys
import traceback

from time import sleep
from tkinter.messagebox import showinfo
from tkinter import Tk, Button, Label, Entry, Text
from tkinter import Toplevel, Checkbutton, BooleanVar, Scale, IntVar, Spinbox, messagebox

from app import DDOS

class App:
    def __init__(self):
        self.root = None
        self.out_count = 0
        self.connected = False
        self.die = False
        self.s = None
        self.con_color = "#00FF00"
        self.child = None

    def output(self, text):
        self.output_box.insert("end", str(self.out_count) + "| " + text + "\n")
        self.output_box.see("end")
        self.out_count += 1

    def popup(self, text):
        messagebox.showinfo(text)

    def display(self):
        pass
    
    def on_closing(self):
        try:
            self.connected = True
            self.start_connection(None, None, None, None, None, None)
        except Exception:
            pass
        
        self.root.destroy()
        
    def label(self):
        self.comm_label = Label(self.root, text="Network Filtering Based on Bot Detection", fg="#FF00FF", background="black", justify="center")
        self.comm_label.grid(row="0", column=0, columnspan=5)
        self.comm_label.config(font=("System", 20))
        
        self.ip_label = Label(self.root, text="Target Ip", background="black", fg="red")
        self.ip = Entry(self.root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
        self.ip_label.grid(row=1, column=0)
        self.ip.grid(row=1, column=1)

        self.msg_size_label = Label(self.root, text="Message Size", background="black", fg="red")
        self.msg_size = Entry(self.root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
        self.msg_size_label.grid(row=2, column=0)
        self.msg_size.grid(row=2, column=1)
        
        self.n_ips_label = Label(self.root, text="No. of Ips", background="black", fg="red")
        self.n_ips = Entry(self.root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
        self.n_ips_label.grid(row=3, column=0)
        self.n_ips.grid(row=3, column=1)

        self.interface_label = Label(self.root, text="Network Interface", background="black", fg="red")
        self.interface = Entry(self.root, bd=1, relief="flat", justify="center", background="#333333", fg="white")
        self.interface_label.grid(row=4, column=0)
        self.interface.grid(row=4, column=1)
        
        self.ip.insert(0, "127.0.0.1")
        self.msg_size.insert(0, "100")
        self.n_ips.insert(0, "10")
        self.interface.insert(0, "eth0")

    def send_command(self, mode):
        
        self.command = mode
        self.commands = ["Flood", "Tear Drop", "Black Nurse"]
        
        self.output("Preparing to send command '" + self.commands[self.command] + "'")
        
        self.child = Toplevel(self.root)

        verbose = BooleanVar()
        verbose_label = Label(self.child, text="Verbose")
        verbose_box = Checkbutton(self.child, variable=verbose)

        if self.command is 0:
            verbose_label.grid(row=1, column=0)
            verbose_box.grid(row=1, column=1)
            submit = Button(self.child, width=35, text="Begin", command=lambda:self.output(self.ddos.run(self.command)))
            submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
        
        elif self.command is 1:
            verbose_label.grid(row=0, column=0)
            verbose_box.grid(row=0, column=1)
            submit = Button(self.child, width=35, text="Begin", command=lambda:self.output(self.ddos.run(self.command)))
            submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
        
        elif self.command is 2:
            verbose_label.grid(row=0, column=0)
            verbose_box.grid(row=0, column=1)
            submit = Button(self.child, width=35, text="Begin", command=lambda:self.output(self.ddos.run(self.command)))
            submit.grid(row=2, column=0, columnspan=2, sticky="NESW")
    

    def run(self, root):
        self.root = root

        # Object of bot environment
        obj = DDOS("", 0, 0 , "")
        self.ddos = obj

        self.root.wm_title("Botnet Control Panel")
        self.root.configure(background="black")
        self.output_box = Text(self.root, width=75, height=20, background="black", fg="#00FF00")
        self.output_box.grid(row=1, column=4, rowspan=6)

        self.label()
        
        # Fill data
        try:
            self.connect_button = Button(self.root, width=15, height=2, background="green", text="Bot Detection", font=("System", 15), fg="black", bd=0, activebackground=self.con_color, command= lambda arg="Click": self.popup(arg))
            self.connect_button.grid(row=7, column=0, columnspan=2, sticky="NESW")
            
            self.flood_button = Button(self.root, text="Flood", state="disabled", command=lambda arg=0 :self.send_command(arg))
            self.flood_button.grid(row=1, column=2, sticky="NESW")
            
            self.tear_drop_button = Button(self.root, text="Tear Drop", state="disabled", command=lambda arg=1 :self.send_command(arg))
            self.tear_drop_button.grid(row=2, column=2, sticky="NESW")
            
            self.black_button = Button(self.root, text="Black Nurse", state="disabled", command=lambda arg=2 :self.send_command(arg))
            self.black_button.grid(row=3, column=2, sticky="NESW")
            
            stats_label = Label(self.root, text="Bots: 0    |    Windows: 0    |    Unix: 0    |    Latency: 0ms", font=("System", 10))
            stats_label.grid(row=7, column=2)

            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()

        except:
            self.popup("Error")
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()


if __name__ == '__main__':
    try:
        obj = App()
        root = Tk()
        obj.run(root)

    except KeyboardInterrupt:
        print("Keyboard Interrupt Occured")
        sys.exit()
    except:
        traceback.print_exc()
        sys.exit()