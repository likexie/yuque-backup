from tkinter import *
from tkinter.dialog import DIALOG_ICON,Dialog
from tkinter.simpledialog import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.ttk import *

class TkRoot(Tk):
    def __init__(self, title='YQbak-1.0', width=500,height=500):
        super().__init__()
        # 设置主窗体大小
        winWidth = width
        winHeight = height
        # 获取屏幕分辨率
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        # 计算主窗口在屏幕上的坐标
        x = int((screenWidth - winWidth)/ 2)
        y = int((screenHeight - winHeight) / 3)
        # 设置主窗口标题
        self.title(title)
        # 设置主窗口大小
        self.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        self.resizable(0,0)


# label

root = TkRoot('YQbackup-1.0')

root.mainloop()