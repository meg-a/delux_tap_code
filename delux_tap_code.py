import tkinter as tk
import time
import os

root = tk.Tk()
root.title("Super Delux Tap Type")
root.geometry("1000x1000")
root.configure(bg = "LightBlue1")

row_or_column = "column"
row = 0
column = 0
letters = ""


tap_code = { 11:"a",12:"b", 13:"c", 14:"d", 15:"e",21:"f",22:"g",23:"h",24:"i",25:"j",31:"k",32:"l",33:"m",34:"n",35:"o",41:"p",42:"q",43:"r",44:"s",45:"t",51:"u",52:"v",53:"w",54:"x",55:"y",61:"z",62:" ",63:"",64:"!",65:"?"}


        

def space_or_new_letter(time):
    global letters
    global row_or_column
    global row
    global column
    global tap_code
    if time < 0.5:
        if row_or_column == "column":
            column += 1
        elif row_or_column == "row":
            row += 1
        
        if row > 5:
            row = 1
            
        elif column > 6:
            column = 1
                
        letter_num = column*10 + row
        if letter_num in tap_code:
            if letter_num == 63:
                lbl_letter["text"] = "delete"
                lbl_letter_num["text"]= letter_num
            else:
                lbl_letter["text"] = tap_code[letter_num]
                lbl_letter_num["text"]= letter_num
        elif letter_num+1 in tap_code:
            lbl_letter["text"] = tap_code[letter_num+1]
            lbl_letter_num["text"]= letter_num + 1
            
        
        

    elif time >= 0.5:
        if row_or_column == "row":
            letter_num = column*10 + row
            if letter_num in tap_code:
                if letter_num != 63:
                    letters += tap_code[letter_num]
                    print(letters)
                else:
                    if len(letters) > 1:
                        letters = letters[:-1]
                    elif len(letters) == 1:
                        letters = ""
                    lbl_letter["text"] = tap_code[letter_num]
                lbl_words["text"] = letters
                lbl_letter["text"] = tap_code[letter_num]
                os.system(f"say {letters}")
                row=0
                column=0
                row_or_column = "column"
        else:
            row_or_column = "row"
    
        
        
            
            

        
            
end = 0    
start = 0  
  
def user_input(key):
    global start
    global end
    #mesure the time
    start = time.time()
    #print(key.keysym)

    

   
def key_release(key):
    global start
    global end
    print("key release")
    end = time.time()
    user_press_time = end - start
    space_or_new_letter(user_press_time)
    
    

root.bind("<Key>", user_input)
root.bind("<KeyRelease-Shift_L>", key_release)



lbl_words = tk.Label(root, text = " ", font=("Georgia", 70))
lbl_words.configure(bg = "LightBlue1")
lbl_words.grid(row=0, column=1)

lbl_letter_num = tk.Label(root, text = "0", font=("Georgia", 70))
lbl_letter_num.configure(bg = "LightBlue1")
lbl_letter_num.grid(row=1, column=0)

lbl_letter = tk.Label(root, text = " ", font=("Georgia", 70))
lbl_letter.configure(bg = "LightBlue1")
lbl_letter.grid(row=1, column=2)

table = tk.PhotoImage(file = "tap_delux.gif")
lbl_gif = tk.Label(root, image = table)
lbl_gif.configure(bg = "LightBlue1")
lbl_gif.grid(row=5, column=0, columnspan=3)



root.mainloop()
