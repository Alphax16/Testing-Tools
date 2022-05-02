import tkinter as tk
from tkinter import Label, Entry, END
from pywinauto import mouse


class DesktopAppTester:
    def table(self, root, lst, r, c):
        header = ('Test Case Number', 'Test Event', 'Output')
        self.h_num = Label(root, text = header[0], width=20, fg='blue', font=('Arial', 16, 'bold'))
        self.h_event = Label(root, text = header[1], width=20, fg='blue', font=('Arial', 16, 'bold'))
        self.h_op = Label(root, text = header[2], width=20, fg='blue', font=('Arial', 16, 'bold'))
        self.h_num.grid(row=0, column=0)
        self.h_event.grid(row=0, column=1)
        self.h_op.grid(row=0, column=2)
        for i in range(1, r):
            for j in range(0, c):
                self.e = Entry(root, width = 20, fg = 'black', font = ('Arial', 16, 'bold'))
                self.e.grid(row = i, column = j)
                self.e.insert(END, lst[i][j])
    # def addEntry(self, tab, lst):
    #     self.e = Entry(tab, width=20, fg='blue', font=('Arial', 16, 'bold'))
    #     self.e.grid(row=len, column=j)
    #     self.e.insert(END, lst[i][j])
    def restart(self, root):
        root.destroy()
        self.desktopAppTester()

    def record(self, root):
        

    def desktopAppTester(self):
        root = tk.Tk()
        root.title('Desktop App Auto Tester')
        lst = [(1, 'Mumbai', 19), (2, 'Pune', 18), (3, 'Mumbai', 20), (4, 'Mumbai', 21), (5, 'Delhi', 21)]
        r, c = len(lst), len(lst[0])


        # -------------------------------------------------------------------------------------------- #

        # -------------------------------------------------------------------------------------------- #

        tab = self.table(root, lst, r, c)

        # -------------------------------------------------------------------------------------------- #

        record = tk.Button(root, text = 'RECORD', width = 25, command = lambda: self.record())
        pause = tk.Button(root, text = 'PAUSE', width = 25, command = lambda: self.pause())

        run = tk.Button(root, text = 'RUN TEST-CASE', width = 25, command = lambda: self.run())

        restart = tk.Button(root, text = 'RESTART', width = 25, command = lambda: self.restart(root))
        exit = tk.Button(root, text = 'EXIT', width = 25, command = root.destroy)

        # -------------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------------- #

        record.grid(row = r + 1, column = c // 2 - 1)
        pause.grid(row = r + 1, column = c // 2 + 1)

        run.grid(row = r + 2, column = c // 2)

        restart.grid(row = r + 3, column = c // 2 - 1)
        exit.grid(row = r + 3, column = c // 2 + 1)

        tk.mainloop()


def main():
    desk_app = DesktopAppTester()
    desk_app.desktopAppTester()

if __name__ == '__main__':
    main()


