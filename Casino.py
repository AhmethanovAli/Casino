from tkinter import *
from random import randint
from tkinter import ttk


# root = Tk()
# root.title('Mellbet')
# root.geometry('500x500')

class Main(Tk):
    def __init__(self):  # self = root
        super().__init__()  # Когда мы создаем объект этого класса ( Main() )
        self.win = Label(text='💰💲Jackpot💲💰', font=('Elephant', 24, 'bold'), bg='#FFF8DC')
        self.title('Mellbet')
        self.geometry('652x652')
        self['bg'] = '#FFF8DC'
        self.x = randint(1, 3)
        self.y = randint(1, 3)
        self.z = randint(1, 3)
        self.loop = None
        self.money = 200
        self.flag = True
        self.games = 0
        self.winning = 0
        self.losing = 0
        self.entry = ttk.Entry()
        self.top_up = Button(text='Top Up')

        self.error = Label(text='Top up your balance', bg='#FFF8DC', font=('Elephant', 19), foreground='red')

        self.invalid_input = Label(text='Please input number', bg='#FFF8DC', font=('Elephant', 19), foreground='red')

        self.balance = Label(text=self.money, bg='#FFD300', font=('Elephant', 12), borderwidth=5,
                             relief="ridge")
        self.balance.place(x=20, y=20, width=100, height=45)

        self.numb = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb.place(x=200, y=240, width=60, height=60)

        self.numb1 = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb1.place(x=260, y=240, width=60, height=60)

        self.numb2 = Label(text='0', bg='#FFD300', font=('Elephant', 18, 'bold'), borderwidth=5, relief="sunken")
        self.numb2.place(x=320, y=240, width=60, height=60)

        self.lbl_games = Label(text=f'games:   {self.games}', bg='#F4FF18', font=('Elephant', 16, 'bold'),
                               relief='groove', anchor='w')
        self.lbl_games.place(x=430, y=20, width=220)

        self.lbl_winning = Label(text=f'winning: {self.winning}', bg='#F4FF18', font=('Elephant', 16, 'bold'),
                                 relief='groove', anchor='w')
        self.lbl_winning.place(x=430, y=51, width=220)

        self.lbl_loosing = Label(text=f'loosing: {self.losing}', bg='#F4FF18', font=('Elephant', 16, 'bold'),
                                 relief='groove', anchor='w')
        self.lbl_loosing.place(x=430, y=82, width=220)

        button_start = Button(
            text='Start',
            bg='#ECC85B',
            font=('Elephant', 13, 'bold'),
            activebackground='#B94E48',
            activeforeground='#E8E111',
            command=self.press_start
        )
        button_start.place(x=230, y=150, width=60, height=40)

        button_stop = Button(
            text='Stop',
            bg='#E8E111',
            font=('Elephant', 13, 'bold'),
            activebackground='#B4674D',
            activeforeground='#893F45',
            command=self.press_stop
        )
        button_stop.place(x=290, y=150, width=60, height=40)

    def press_start(self):
        self.x = randint(1, 3)
        self.y = randint(1, 3)
        self.z = randint(1, 3)
        self.numb.configure(text=self.x)
        self.numb1.configure(text=self.y)
        self.numb2.configure(text=self.z)
        self.win.destroy()

        if self.money - 200 < -200:
            self.error.place(x=170, y=20)
            self.entry = ttk.Entry()
            self.entry.place(x=180, y=140, width=220, height=220)
            self.top_up = Button(text='Top Up', command=self.top_up_balance)
            self.top_up.place(x=260, y=365)
            raise ValueError('Is not enough money')
        if self.flag == True:
            self.games += 1
            self.lbl_games.configure(text=f'games:   {self.games}')
            self.flag = False
            self.money -= 200
            self.losing += 200
            self.lbl_loosing.configure(text=f'loosing: {self.losing}')
            self.balance.configure(text=self.money)
        self.loop = self.after(100, self.press_start)  # Метод зацикливания функции

    def top_up_balance(self):
        value = self.entry.get()
        if value.isdigit():
            value = int(value)
            self.money += value
            if self.money - 200 > -200:
                self.balance.configure(text=self.money)
                self.error.destroy()
                self.top_up.destroy()
                self.entry.destroy()
        else:
            self.invalid_input.place(x=170, y=85)

        print(value)

    def press_stop(self):
        self.flag = True
        if self.x == self.y and self.x == self.z:
            cash = randint(1000, 2000)
            self.money += cash
            self.winning += cash
            self.lbl_winning.configure(text=f'winning: {self.winning}')
            self.balance.configure(text=self.money)
            self.win = Label(text='💰💲Jackpot💲💰', font=('Elephant', 23, 'bold'), bg='#FFF8DC')
            self.win.place(x=170, y=80)
        self.after_cancel(self.loop)


if __name__ == '__main__':
    root = Main()
    root.mainloop()
