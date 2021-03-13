#import
import tkinter as tk
import time
import os

#root window settings 
root = tk.Tk()
root.title("Super Delux Tap Type")
root.geometry("1000x600")
root.configure(bg = "LightBlue1")



#global variables 
row_or_column = "row"
row = 0
column = 0
letters = ""

#global variables for time 
end = 0    
start = 0 

#tap code dictionary 
tap_code = { 11:"a",12:"b", 13:"c", 14:"d", 15:"e",21:"f",22:"g",23:"h",24:"i",25:"j",31:"k",32:"l",33:"m",34:"n",35:"o",41:"p",42:"q",43:"r",44:"s",45:"t",51:"u",52:"v",53:"w",54:"x",55:"y",61:"z",62:" ",63:"",64:"!",65:"?"}

#functions
#functions for timing 
#when user presses the shift key 
def user_input(key):
    #global variables
    global start
    global end
    #when user presses shift key, time is recorded
    start = time.time()

#when user releases the shift key    
def key_release(key):
    #global variables 
    global start
    global end
    #when user releases the shift key, time is recorded
    end = time.time()
    #released time - pressed time = how many seconds user pressed the shift key 
    user_press_time = end - start
    #send the time to the tap code function 
    space_or_new_letter(user_press_time)
    


#when shift is pressed and released
def space_or_new_letter(time):
    #global variables 
    global letters
    global row_or_column
    global row
    global column
    global tap_code
    #if the pressed time is less than 0.5 seconds  
    if time < 0.5:
        if row_or_column == "row":
            column += 1
        elif row_or_column == "column":
            row += 1
        
        if row > 5:
            row = 1
            
        elif column > 6:
            column = 1
        #formula for letter number (for dictionary, tap_code)        
        letter_num = column*10 + row
        #only for letters in dictionary, tap_code
        if letter_num in tap_code:
            #for the delete only 
            if letter_num == 63:
                lbl_letter["text"] = "delete"
                lbl_letter_num["text"]= letter_num
            #for other numbers that are in tap_code 
            else:
                lbl_letter["text"] = tap_code[letter_num]
                lbl_letter_num["text"]= letter_num
        #10, 20, 30, 40, 50, and 60 are not in dictionry so add one 
        elif letter_num+1 in tap_code:
            lbl_letter["text"] = tap_code[letter_num+1]
            lbl_letter_num["text"]= letter_num + 1
    #if the press time is longer than 0.5 seconds 
    elif time >= 0.5:
        #if it is classified row then alphabet is printed and the sound function reads the word
        if row_or_column == "column":
            letter_num = column*10 + row
            if letter_num in tap_code:
                #for general letter numbers in tap code (63 is exception)
                if letter_num != 63:
                    letters += tap_code[letter_num]
                else:
                    #only if letter number is 63, the last letter of the string in variable 'letters' is deleted
                    if len(letters) > 1:
                        letters = letters[:-1]
                    elif len(letters) == 1:
                        letters = " "
                lbl_words["text"] = letters
                lbl_letter["text"] = tap_code[letter_num]
                os.system(f"say {letters}")
                row=0
                column=0
                row_or_column = "row"
        #if it is classified column then you will input row next 
        else:
            row_or_column = "column"
            
#connecting root to keys  
root.bind("<Key>", user_input)
root.bind("<KeyRelease-Shift_L>", key_release)

#tkinter widgets 
#label for typed words 
lbl_words = tk.Label(root, text = " ", font=("Georgia", 70))
lbl_words.configure(bg = "LightBlue1")
lbl_words.grid(row=0, column=1)

#label for showing typing/typed letter number 
lbl_letter_num = tk.Label(root, text = "0", font=("Georgia", 70))
lbl_letter_num.configure(bg = "LightBlue1")
lbl_letter_num.grid(row=1, column=0)

#label for showing typing/typed alphabet
lbl_letter = tk.Label(root, text = " ", font=("Georgia", 70))
lbl_letter.configure(bg = "LightBlue1")
lbl_letter.grid(row=1, column=2)

#the tap code table 
table = tk.PhotoImage(file = "tap_delux.gif")
lbl_gif = tk.Label(root, image = table)
lbl_gif.configure(bg = "LightBlue1")
lbl_gif.grid(row=3, column=0, columnspan=3)


root.mainloop()
