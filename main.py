from tkinter import *
from tkinter import ttk

colorone = "#070807"  #black
colortwo = "#feffff"    #white
colorthree = "#38576b"  #blue
colorfour = "#ECEFF1"   #grey
colorfive = "#FFAB40"  #orange

window = Tk()
window.title("Calculadora")
window.geometry("235x310")
window.config(bg=colorone)

#frames
frame_screen = Frame(window, width=235, height=50, bg=colorthree)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268)
frame_body.grid(row=1, column=0)


all_values = ''
value_text = StringVar()
#
def enter_Values(event):
    global all_values
    all_values = all_values + str(event)
    value_text.set(all_values)

def calculate():
    global all_values
    r = eval(all_values)
    value_text.set(str(r))
    all_values = str(r)

def clear_screen():
    global all_values
    all_values = ''
    value_text.set('')

#label
app_label = Label(frame_screen, textvariable=value_text, width=16, height=2, padx=7, relief=FLAT,
                  anchor="e", justify=RIGHT, font=('Ivy 18'), bg=colorthree, fg=colortwo)
app_label.place(x=0, y=0)

#butons
b_one = Button(frame_body, command=clear_screen, text="C", width=11, height=2, bg=colorfour,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_one.place(x=0, y=0)
b_two = Button(frame_body, command=lambda: enter_Values('%'), text="%", width=5, height=2, bg=colorfour,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_two.place(x=118, y=0)
b_three = Button(frame_body, command=lambda: enter_Values('/'), text="/", width=5, height=2, bg=colorfive, fg=colortwo,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_three.place(x=177, y=0)

b_four = Button(frame_body, command=lambda: enter_Values('7'), text="7", width=5, height=2, bg=colorfour,
                font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_four.place(x=0, y=52)
b_five = Button(frame_body, command=lambda: enter_Values('8'), text="8", width=5, height=2, bg=colorfour,
                font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_five .place(x=59, y=52)
b_six = Button(frame_body, command=lambda: enter_Values('9'), text="9", width=5, height=2, bg=colorfour,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_six.place(x=118, y=52)
b_seven = Button(frame_body, command=lambda: enter_Values('*'), text="*", width=5, height=2, bg=colorfive, fg=colortwo,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seven.place(x=177, y=52)

b_eight = Button(frame_body, command=lambda: enter_Values('4'), text="4", width=5, height=2, bg=colorfour,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eight.place(x=0, y=104)
b_nine = Button(frame_body, command=lambda: enter_Values('5'), text="5", width=5, height=2, bg=colorfour,
                font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_nine.place(x=59, y=104)
b_ten = Button(frame_body, command=lambda: enter_Values('6'), text="6", width=5, height=2, bg=colorfour,
               font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ten.place(x=118, y=104)
b_eleven = Button(frame_body, command=lambda: enter_Values('-'), text="-", width=5, height=2, bg=colorfive, fg=colortwo,
                  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eleven.place(x=177, y=104)

b_twelve = Button(frame_body, command=lambda: enter_Values('1'), text="1", width=5, height=2, bg=colorfour,
                  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_twelve.place(x=0, y=156)
b_thirteen = Button(frame_body, command=lambda: enter_Values('2'), text="2", width=5, height=2, bg=colorfour,
                    font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_thirteen.place(x=59, y=156)
b_fourteen = Button(frame_body, command=lambda: enter_Values('3'), text="3", width=5, height=2, bg=colorfour,
                    font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_fourteen.place(x=118, y=156)
b_fiveteen = Button(frame_body, command=lambda: enter_Values('+'), text="+", width=5, height=2, bg=colorfive, fg=colortwo,
                    font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_fiveteen.place(x=177, y=156)

b_sixteen = Button(frame_body, command=lambda: enter_Values('0'), text="0", width=11, height=2, bg=colorfour,
                   font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sixteen.place(x=0, y=208)
b_seventeen = Button(frame_body, command=lambda: enter_Values('.'), text=".", width=5, height=2, bg=colorfour,
                     font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_seventeen.place(x=118, y=208)
b_eighteen = Button(frame_body, command=calculate, text="=", width=5, height=2, bg=colorfive, fg=colortwo,
                    font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_eighteen.place(x=177, y=208)








window.mainloop()