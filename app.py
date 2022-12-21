from tkinter import *
from add_window import AddWindow
from view_window import ViewWindow


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x500')
        self.config(pady=30, padx=30)
        self.title('Employee Database')
        window_label = Label(text='Employee Database', font=('Comic Sans', 24))
        window_label.place(x=35, y=125)

        # Open Add Window Button
        add_win_button = Button(text='Add Employee', command=self.open_add_window)
        add_win_button.place(x=10, y=200)

        # Open View Window Button
        view_win_button = Button(text='View Employee', command=self.open_view_window)
        view_win_button.place(x=115, y=200)

        # Open Remove Window Button
        remove_win_button = Button(text='Remove Employee')
        remove_win_button.place(x=220, y=200)

        # Close Button
        Button(self, text='Close', command=self.destroy).place(x=155, y=400)

    def open_add_window(self):
        window = AddWindow(self)
        window.grab_set()

    def open_view_window(self):
        window = ViewWindow(self)
        window.grab_set()


app = App()
app.mainloop()