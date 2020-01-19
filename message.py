import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from main.profile import Profile


class Message(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.show_widget()

    def show_widget(self):
        self.geometry("600x500")
        self.resizable(False, False)
        self.title('Messages')
        tk.Button(self, text='Show Messages', command=self.show, width=15, bg='green', fg='white',
                  font=("bold", 10)).place(x=30, y=630)

    def show(self):
        label_0 = tk.Label(self, text='Your Messages', width=20, font=("bold", 20))
        label_0.place(x=90, y=43)
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        cols = ('Senders', 'Receiver', 'Messages')
        listbox = ttk.Treeview(self, columns=cols, show="headings")

        for col in cols:
            listbox.heading(col, text=col)

        listbox.place(x=10, y=133)
        listbox.column(cols[0], width=120)
        listbox.column(cols[1], width=120)
        listbox.column(cols[2], width=320)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        messages = Profile()
        messages = messages.get_messages()
        for m in messages:
            listbox.insert("", "end", values=(m['senders'], m['receivers'], m['messages']))



