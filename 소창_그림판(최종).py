from tkinter import*
from tkinter.colorchooser import*
from tkinter.simpledialog import*

def mouseClick(event):
    global x1,y1,x2,y2
    x1=event.x
    y1=event.y

def mouseDrop(event):
    global x1,y1,x2,y2,penWidth,penColor
    x2=event.x
    y2=event.y
    canvas.create_line(x1,y1,x2,y2,width=penWidth,fill=penColor)
def straight():
    global t
    t="straight"
    canvas.bind("<ButtonRelease-1>",mouseDrop)
def curveLine(event):
    if t=="curve":
        global x1,y1,penWidth,penColor
        canvas.create_line(x1,y1,event.x,event.y,width=penWidth,fill=penColor)
        x1=event.x
        y1=event.y
def curve():
    global t
    t="curve"
    canvas.bind("<B1-Motion>",curveLine)
def starLine(event): 
    global x1,y1,penWidth,penColor
    canvas.create_text(x1,y1,text="*",font=("나눔고딕코딩",penWidth+15),fill=penColor)
    x1=event.x
    y1=event.y
def star():
    canvas.bind("<B1-Motion>",starLine)
def heartLine(event): 
    global x1,y1,penWidth,penColor
    canvas.create_text(x1,y1,text="♡",font=("나눔고딕코딩",penWidth+15),fill=penColor)
    x1=event.x
    y1=event.y
def heart():
    canvas.bind("<B1-Motion>",heartLine)
 
def getColor():
    global penColor
    color=askcolor()
    penColor=color[1]

def getWidth():
    global penWidth
    penWidth=askinteger("선 두께","선 두께(1~10)을 입력하세요",minvalue=1,maxvalue=10)
    

def eraser():
    global penColor
    penColor="#f1f1f1"
    curve()
def eraserWidth():
    global penWidth
    penWidth=askinteger("지우개 두께","지우개 두께(1~10)을 입력하세요",minvalue=1,maxvalue=10)
def eraserEnd():
    global penColor
    penColor="black"
    
def allClear():
    canvas.delete("all")
def getShape(shape):
    if shape=='c':
        canvas.create_circle(x1,y1,x2,y2,width=penWidth,fill=penColor) 
window=None
canvas=None

x1,y1,x2,y2=None,None,None,None
penColor='black'
penWidth=5


if __name__=="__main__":
    window=Tk()
    window.title("밥 아저씨-이서윤")
    canvas=Canvas(window,height=300,width=300)
    
    canvas.bind("<Button-1>",mouseClick)
    canvas.bind("<ButtonRelease-1>",mouseDrop)
    canvas.pack()


    mainMenu=Menu(window)
    window.config(menu=mainMenu)
    fileMenu1=Menu(mainMenu)
    
    mainMenu.add_cascade(label='설정',menu=fileMenu1)
    fileMenu1.add_command(label="선 색상 선택",command=getColor)
    fileMenu1.add_command(label="선 두께 결정",command=getWidth)
    fileMenu1.add_command(label="초기화",command=allClear)

    fileMenu2=Menu(mainMenu)
    mainMenu.add_cascade(label="지우개",menu=fileMenu2)
    fileMenu2.add_command(label="지우개 사용",command=eraser)
    fileMenu2.add_command(label="지우개  두께 결정",command=eraserWidth)
    fileMenu2.add_command(label="지우개 사용 종료",command=eraserEnd)

    fileMenu3=Menu(mainMenu)
    mainMenu.add_cascade(label="선 모양 바꾸기",menu=fileMenu3)
    fileMenu3.add_command(label="직선",command=straight)
    fileMenu3.add_command(label="곡선",command=curve)
    fileMenu3.add_command(label="별선",command=star)
    fileMenu3.add_command(label="하트선",command=heart)
    
    window.mainloop()
