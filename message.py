import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

from main.profile import Profile


class Message(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.title('Messages')
        self.geometry("600x500")
        self.resizable(False, False)
        self.messages = Profile()
        cols = ('Recipient_Id', 'Receiver', 'Messages')
        self.listbox = ttk.Treeview(self, columns=cols, show="headings")
        for col in cols:
            self.listbox.heading(col, text=col)
        label_0 = tk.Label(self, text='Your Messages', width=20, font=("bold", 20))
        label_0.place(x=90, y=43)
        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.place(x=10, y=133)
        self.listbox.column(cols[0], width=120)
        self.listbox.column(cols[1], width=120)
        self.listbox.column(cols[2], width=320)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.type = tk.StringVar(self)
        self.text = ttk.Entry(self)
        self.master = master
        tk.Button(self, text='Show Messages', command=self.show, width=15, bg='green', fg='white',
                  font=("bold", 10)).place(x=30, y=428)
        tk.Button(self, text='Send', command=self.send_message, width=5, bg='purple', fg='white',
                  font=("bold", 10)).place(x=510, y=425)
        tk.Label(self, text='Message', width=10, font=("bold", 10)).place(x=230, y=430)
        self.text.place(x=345, y=430)

        list1 = ['All', 'Individual', 'All']
        droplist = ttk.OptionMenu(self, self.type, *list1)
        droplist.config(width=5)
        self.type.set('Select type')
        droplist.place(x=490, y=390)

    def show(self):
        messages = self.messages.get_messages()
        for i in self.listbox.get_children():
            self.listbox.delete(i)
        for m in messages:
            self.listbox.insert("", "end", values=(m['recipient_id'], m['receivers'], m['messages']))

    def send_message(self):
        send_type = self.type.get()
        if send_type == 'Individual':
            self.send_individual()
        elif send_type == 'All':
            self.send_all()
        else:
            msgbox.showwarning('Choose', 'Choose one sending type')
            pass

    def send_individual(self):
        selected_item = self.listbox.selection()
        values = list(self.listbox.item(selected_item)['values'])
        text = self.text.get()
        if values == [] or text == "":
            msgbox.showinfo('Empty', 'Please enter the message')

        else:
            recipient_id = values[0]
            self.messages.send_individual(text, recipient_id)
            msgbox.showinfo('Sent', 'Message has been sent successfully')

    def send_all(self):
        text = self.text.get()
        if text == "":
            msgbox.showinfo('Empty', 'Please enter the message')
        else:
            self.messages.post_messages(text)
            msgbox.showinfo('Sent', 'Message has been sent successfully')
