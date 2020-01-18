import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

from main.profile import Profile


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tweet Master")
        self.geometry("1100x1050")
        self.resizable(False, False)
        self.label_0 = tk.Label(self, text='!!!!WELCOME TO THE TWEET MASTER!!!!', width=50, font=("bold", 20))
        self.label_0.place(x=100, y=43)

        self.label_1 = tk.Label(self, text='Your Profile', width=50, font=("bold", 20))
        self.label_1.place(x=100, y=103)
        self.profile = Profile()
        self.home()
        self.label_1 = tk.Label(self, text='Followers Details', width=50, font=("bold", 20))
        self.label_1.place(x=-200, y=318)

        self.label_2 = tk.Label(self, text='Following Details', width=50, font=("bold", 20))
        self.label_2.place(x=400, y=318)

        self.scrollbar_1 = ttk.Scrollbar(self)
        self.scrollbar_1.pack(side=LEFT, fill=Y)

        self.scrollbar_2 = ttk.Scrollbar(self)
        self.scrollbar_2.pack(side=RIGHT, fill=Y)
        self.cols = ('Name', 'Follower_Count', 'Friends', 'Verified', 'Profile_Image')
        self.listbox_1 = ttk.Treeview(self, columns=self.cols, show="headings")
        self.listbox_2 = ttk.Treeview(self, columns=self.cols, show="headings")

        for col in self.cols:
            self.listbox_1.heading(col, text=col)
            self.listbox_2.heading(col, text=col)

        self.listbox_1.place(x=30, y=400)
        self.listbox_2.place(x=580, y=400)
        self.listbox_1.column(self.cols[0], width=150)
        self.listbox_1.column(self.cols[1], width=150)
        self.listbox_1.column(self.cols[2], width=60)
        self.listbox_1.column(self.cols[3], width=60)
        self.listbox_1.column(self.cols[4], width=100)

        self.listbox_2.column(self.cols[0], width=150)
        self.listbox_2.column(self.cols[1], width=150)
        self.listbox_2.column(self.cols[2], width=60)
        self.listbox_2.column(self.cols[3], width=60)
        self.listbox_2.column(self.cols[4], width=80)

        self.listbox_1.config(yscrollcommand=self.scrollbar_1.set)
        self.listbox_2.config(yscrollcommand=self.scrollbar_2.set)
        self.scrollbar_1.config(command=self.listbox_1.yview)
        self.scrollbar_2.config(command=self.listbox_2.yview)

        # buttons
        tk.Button(self, text='Show Followers', command=self.show_follower, width=15, bg='green', fg='white',
                  font=("bold", 10)).place(x=30, y=630)
        tk.Button(self, text='Show Following', command=self.show_following, width=15, bg='yellow', fg='white',
                  font=("bold", 10)).place(x=580, y=630)

    def home(self):

        profile = self.profile.profile()
        for p in profile:
            label_0 = tk.Label(self, text='Username:', width=15, font=("bold", 15))
            label_0.place(x=200, y=160)

            data_0 = ttk.Label(self, text=p['name'], width=20, font=("bold", 13))
            data_0.place(x=600, y=160)

            label_1 = tk.Label(self, text='Followers_Count:', width=20, font=("bold", 15))
            label_1.place(x=200, y=200)

            data_1 = ttk.Label(self, text=p['follower_count'], width=20, font=("bold", 13))
            data_1.place(x=600, y=200)

            label_2 = tk.Label(self, text='Following_Count:', width=20, font=("bold", 15))
            label_2.place(x=200, y=240)

            data_2 = ttk.Label(self, text=p['following_count'], width=20, font=("bold", 13))
            data_2.place(x=600, y=240)

    def show_follower(self):
        follower = self.profile.get_followers()
        for i in self.listbox_1.get_children():
            self.listbox_1.delete(i)
        for c in follower:
            self.listbox_1.insert("", "end", values=(c['name'], c['followers_count'], c['friends_count'],
                                                     c['isVerified'], c['profile_image']))

    def show_following(self):
        following = self.profile.get_following()
        for i in self.listbox_2.get_children():
            self.listbox_2.delete(i)
        for c in following:
            self.listbox_2.insert("", "end", values=(c['name'], c['followers_count'],
                                                     c['friends_count'], c['isVerified'], c['profile_image']))

    def on_closing(self):
        if msgbox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.protocol("WM_DELETE_WINDOW", mainwindow.on_closing)
    mainwindow.mainloop()
