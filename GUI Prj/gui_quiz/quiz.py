from tkinter import *

def fileOpen() :
    file = open('GUI Prj\gui_quiz\mynote.txt', 'r', encoding='utf-8')
    data = file.read()
    txt.insert(END, data)

def fileSave() :
    pass

def exit() :
    root.quit()
    root.destroy()

root = Tk()
root.title("제목 없음 - window 메모장")
root.geometry("800x600")

# 메뉴 바
mainMenu = Menu(root)
root.config(menu = mainMenu)

fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label = "열기", command = fileOpen)
fileMenu.add_command(label = "저장", command = fileSave)
fileMenu.add_command(label = "끝내기", command = exit)

mainMenu.add_cascade(label = "파일", menu=fileMenu)
mainMenu.add_cascade(label = "편집")
mainMenu.add_cascade(label = "서식")
mainMenu.add_cascade(label = "보기")
mainMenu.add_cascade(label = "도움말")

# frame
frame = Frame(root)
frame.pack(fill = "both", expand = True)

scroll = Scrollbar(frame)
scroll.pack(side = "right", fill = "y")

txt = Text(frame, yscrollcommand = scroll.set)
txt.pack(side = "left", fill = "both", expand = True)

scroll.config(command = txt.yview)

root.mainloop()