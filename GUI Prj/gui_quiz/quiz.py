from tkinter import *
import os

root = Tk()
root.title("제목 없음 - window 메모장")
root.geometry("800x600")

filename = "mynote.txt"

def fileOpen() :
    if os.path.isfile(filename) : # 파일이 있으면 true, 없으면 false
        with open(filename, 'r', encoding = "utf-8") as file :
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용을 본문에 입력

def fileSave() :
     with open(filename, 'w', encoding = "utf-8") as file :
            file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장

# 메뉴 바
mainMenu = Menu(root)

fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label = "열기", command = fileOpen)
fileMenu.add_command(label = "저장", command = fileSave)
fileMenu.add_separator()
fileMenu.add_command(label = "끝내기", command = root.quit)
mainMenu.add_cascade(label = "파일", menu=fileMenu)

# 편집, 서식, 보기, 도움말
mainMenu.add_cascade(label = "편집")
mainMenu.add_cascade(label = "서식")
mainMenu.add_cascade(label = "보기")
mainMenu.add_cascade(label = "도움말")

root.config(menu = mainMenu)

# 스크롤 바
scroll = Scrollbar(root)
scroll.pack(side = "right", fill = "y")

# 본문 영역
txt = Text(root, yscrollcommand = scroll.set)
txt.pack(side = "left", fill = "both", expand = True)

scroll.config(command = txt.yview)

root.mainloop()