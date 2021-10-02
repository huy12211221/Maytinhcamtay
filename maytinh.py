from tkinter import *
from tkinter.font import BOLD

input_cal=""
input_show =""
input_show2 =""
caled = False
def clicked(data):
    global input_cal
    global input_show
    global caled
    if input_show == "Lỗi cú pháp!":
        input_show = ""
    if caled == True and data in ("0","1","2","3","4","5","6","7","8","9","000"):
        input_show = ""
        input_cal =""
        caled = False
    input_cal += data
    if data == "*":
        input_show += "X"
    elif data == "/100":
        input_show += "%"
    elif data == "**2":
        input_show += "^2"
    else:
        input_show += data
    text.set(input_show)

def AC():
    global input_cal
    global input_show
    input_cal = ""
    input_show = ""
    text.set(input_show)

def Del():
    global input_cal
    global input_show
    if input_show == "Lỗi cú pháp!":
        input_show = ""
    input_cal = input_cal[0:len(input_cal)-1]
    input_show = input_show[0:len(input_cal)-1]
    text.set(input_show)

def cal():
    global input_cal
    global input_show
    global caled
    try:
        equal = eval(input_cal)
        input_cal = str(equal)
        input_show = str(equal)
        input_show2 = "= "+input_show
        caled = True
        text.set(input_show2)
    except SyntaxError:
        input_cal = ""
        input_show = "Lỗi cú pháp!"
        text.set(input_show)

window = Tk()
window.title("Caculator")
window.resizable(0,0)

frame1 = Frame(window,bg="#474849",width=100,height=100)
frame1.grid(column=0,row=0,columnspan=4,sticky=E+S+W+N)
frame2 = Frame(window,bg="#474849",width=100,height=100)
frame2.grid(column=0,row=1,columnspan=4,sticky=E+S+W+N)
#window.geometry("350x500")
text = StringVar()
text.set("0")
lb1 = Label(frame1,textvariable=text,font="Arial",bg="#474849",fg="white",padx=0,pady=20,width=48,height=5,anchor=SE)
lb1.grid(column=0,row=0)
""" lb_e = Label(frame1,text=text2,font="Arial",bg="#474849",fg="white")
lb_e.grid(column=0,row=0) """
""" lb2 = Label(frame1,textvariable=text,font="Arial",bg="#474849",fg="white",padx=0,pady=10,width=37,height=5,anchor=SE)
lb2.grid(column=0,row=0) """

b_ac = Button(frame2,text="AC",font="UTM",bg="#595a5b",fg="white",width=9,height=3,bd=1,command=AC)
b_ac.grid(column=0,row=1)
b_del = Button(frame2,text="Del",font="UTM",bg="#595a5b",fg="white",width=9,height=3,bd=1,command=Del)
b_del.grid(column=1,row=1,sticky=W)
b_persent = Button(frame2,text="%",font="UTM",bg="#595a5b",fg="white",width=9,height=3,bd=1,command=lambda:clicked("/100"))
b_persent.grid(column=2,row=1,sticky=W)
b_div = Button(frame2,text="/",font="UTM",bg="#fe9f0a",fg="white",width=9,height=3,bd=1,command=lambda:clicked("/"))
b_div.grid(column=3,row=1,sticky=W)

b_7 = Button(frame2,text="7",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("7"))
b_7.grid(column=0,row=2,sticky=W)
b_8 = Button(frame2,text="8",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("8"))
b_8.grid(column=1,row=2,sticky=W)
b_9 = Button(frame2,text="9",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("9"))
b_9.grid(column=2,row=2,sticky=W)
b_multi = Button(frame2,text="X",font="UTM",bg="#fe9f0a",fg="white",width=9,height=3,bd=1,command=lambda:clicked("*"))
b_multi.grid(column=3,row=2,sticky=W)

b_4 = Button(frame2,text="4",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("4"))
b_4.grid(column=0,row=3)
b_5 = Button(frame2,text="5",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("5"))
b_5.grid(column=1,row=3,sticky=W)
b_6 = Button(frame2,text="6",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("6"))
b_6.grid(column=2,row=3)
b_sub = Button(frame2,text="-",font="UTM",bg="#fe9f0a",fg="white",width=9,height=3,bd=1,command=lambda:clicked("-"))
b_sub.grid(column=3,row=3)

b_1 = Button(frame2,text="1",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("1"))
b_1.grid(column=0,row=4,sticky=W)
b_2 = Button(frame2,text="2",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("2"))
b_2.grid(column=1,row=4,sticky=W)
b_3 = Button(frame2,text="3",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("3"))
b_3.grid(column=2,row=4,sticky=W)
b_sum = Button(frame2,text="+",font="UTM",bg="#fe9f0a",fg="white",width=9,height=3,bd=1,command=lambda:clicked("+"))
b_sum.grid(column=3,row=4,sticky=W)

b_zero = Button(frame2,text = "0",font = "UTM",bg="#747576",fg="white",padx=95,pady=24,bd=1,command=lambda:clicked("0"))
b_zero.grid(column=0,row=5,columnspan=2,sticky=W)
b_comma = Button(frame2,text=",",font="UTM",bg="#747576",fg="white",width=9,height=3,bd=1,command=lambda:clicked("."))
b_comma.grid(column=2,row=5,sticky=W)
b_equal = Button(frame2,text="=",font="UTM",bg="#fe9f0a",fg="white",padx=94,pady=24,bd=1,command=cal)
b_equal.grid(column=3,row=5,columnspan=2,sticky=W)

b_m2 = Button(frame2,text="▊²",font="UTM",bg="#939393",fg="white",width=9,height=3,bd=1,command=lambda:clicked("**2"))
b_m2.grid(column=4,row=1,sticky=W)
b_bk1 = Button(frame2,text=")",font="UTM",bg="#939393",fg="white",width=9,height=3,bd=1,command=lambda:clicked(")"))
b_bk1.grid(column=4,row=2,sticky=W)
b_bk2 = Button(frame2,text="(",font="UTM",bg="#939393",fg="white",width=9,height=3,bd=1,command=lambda:clicked("("))
b_bk2.grid(column=4,row=3,sticky=W)
b_pi = Button(frame2,text="000",font="UTM",bg="#939393",fg="white",width=9,height=3,bd=1,command=lambda:clicked("000"))
b_pi.grid(column=4,row=4,sticky=W)

""" window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1) """

#window.rowconfigure(2, weight=1)

window.mainloop()