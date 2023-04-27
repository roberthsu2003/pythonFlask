import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.update_data()

    def update_data(self):
        print("更新資料")
        self.update_threading = self.after(1000,self.update_data)

def on_closing():
    print("視窗關閉")
    window.after_cancel(window.update_threading)
    window.destroy()

def main():
    global window
    window = Window()
    window.title("背景執行")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()

if __name__ == "__main__":    
    main()