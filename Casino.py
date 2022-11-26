from tkinter import *
from random import randint
from tkinter import ttk


# root = Tk()
# root.title('Mellbet')
# root.geometry('500x500')

class Main(Tk):
    def __init__(self):  # self = root
        super().__init__()  # Когда мы создаем объект этого класса ( Main() )
        self.title('Mellbet')
        self.geometry('600x600')
        self['bg'] = '#FFF8DC'
        self.x = randint(1, 3)
        self.y = randint(1, 3)
        self.z = randint(1, 3)
        self.loop = None
        self.numb = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb.place(x=200, y=240, width=60, height=60)
        self.numb1 = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb1.place(x=260, y=240, width=60, height=60)
        self.numb2 = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb2.place(x=320, y=240, width=60, height=60)
        button_start = Button(text='Start', bg='#ECC85B', font=('Elephant', 13, 'bold'), activebackground='#B94E48',
                              activeforeground='#E8E111', command=self.press_start)
        button_start.place(x=230, y=150, width=60, height=40)
        button_stop = Button(text='Stop', bg='#E8E111', font=('Elephant', 13, 'bold'), activebackground='#B4674D',
                             activeforeground='#893F45', command=self.press_stop)
        button_stop.place(x=290, y=150, width=60, height=40)

    def press_start(self):
        self.x = randint(1, 3)
        self.y = randint(1, 3)
        self.z = randint(1, 3)
        self.numb.configure(text=self.x)
        self.numb1.configure(text=self.y)
        self.numb2.configure(text=self.z)
        self.loop = self.after(100, self.press_start)  # Метод зацикливания функции

    def press_stop(self):
        if self.x == self.y and self.x == self.z:
            win = Label(text='💰💲Jackpot💲💰', font=('Elephant', 24, 'bold'), bg='#FFF8DC')
            win.place(x=180, y=80)
        self.after_cancel(self.loop)


if __name__ == '__main__':
    root = Main()
    root.mainloop()