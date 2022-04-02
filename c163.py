from tkinter import *
import tkinter.messagebox as tkmb
root=Tk()
root.title("fever report")
root.geometry("600x600")


question1_label=Label(root,text="Do you have headache and sore throat?")
question1_label.pack()
question1_radiobutton=StringVar(value="0")
question1_r1=Radiobutton(root,text="yes",variable=question1_radiobutton,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="no",variable=question1_radiobutton,value="no")
question1_r2.pack()

question2_label=Label(root,text="Is your body temperature high?")
question2_label.pack()
question2_radiobutton=StringVar(value="0")
question2_r1=Radiobutton(root,text="yes",variable=question2_radiobutton,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="no",variable=question2_radiobutton,value="no")
question2_r2.pack()

question3_label=Label(root,text="are there any symptoms of eye redness?")
question3_label.pack()
question3_radiobutton=StringVar(value="0")
question3_r1=Radiobutton(root,text="yes",variable=question3_radiobutton,value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="no",variable=question3_radiobutton,value="no")
question3_r2.pack()

def fever_report():
    score=0
    if question1_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question2_radiobutton.get()=="yes":
        score=score+20
        print(score)
    if question3_radiobutton.get()=="yes":
        score=score+20
        print(score)
        
    if score<=20:
        tkmb.showinfo("report","you dont need to visit a doctor")
    elif score>20 and score<=40:
        tkmb.showinfo("report","you might perhaps have to visit a doctor")
    else:
        tkmb.showinfo("report","I strongly advise you to visit a doctor")

clickme_btn=Button(root,text="click me",command=fever_report)
clickme_btn.pack()

root.mainloop()
