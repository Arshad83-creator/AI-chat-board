from tkinter import*
from PIL import Image ,ImageTk
import speech_to_text
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")

root.resizable(False,False)
root.config(bg="#6F8FAF")


# ask fun

def ask():
    
    user_val= speech_to_text.speech_to_text()
    if user_val is None:
       user_val="Could not understand"
    bot_val= action.Action(user_val)
    # if bot_val is None:
    #     bot_val ="I am not able to understand."
    text.insert(END,'User:<--'+str(user_val)+"\n")
    text.insert(END,"BOT <---"+str(bot_val)+"\n")
    if bot_val.lower()=="ok Sir":
        root.destroy()    


def send():
    send =entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->'+ send+"\n")
    if bot != None:
        text.insert(END,"BOT <---"+str(bot)+"\n")
    if bot=="ok Sir":
        root.destroy() 


def del_text():
    text.delete('1.0',"end")

# frame

frame =LabelFrame(root, padx=100, pady=7, borderwidth=3 , relief= "raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=1,padx=75,pady=10)

# text lable

text_label=Label(frame , text="AI Assistant", font=("conic Sans ms",14,"bold"),bg="#356696")
text_label.grid(row =0, column=0,padx=20,pady=10)

# image

image=ImageTk.PhotoImage(Image.open("robot_200x200.png"))
image_label=Label(frame ,image=image)
image_label.grid(row=1, column=0,pady=10)

# adding a text

text = Text(root, font=('courier 10 bold'), bg="#356696")
text.grid(row=2,column=0)
text.place(x=93, y=375, width=375,height=100)


# entry visit

entry=Entry(root, justify=CENTER)
entry.place(x=105,y=500,width=350,height=30)


# buton1

Button1 =Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
Button1.place(x=70,y=575)

# button2
Button2 =Button(root,text="SEND",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
Button2.place(x=365,y=575)

# button3
Button3 =Button(root,text="DELETE",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
Button3.place(x=210,y=575)


root.mainloop()
