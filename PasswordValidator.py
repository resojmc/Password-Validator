import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Password Validator")

def valid_pass(p):
    #Function that checks if a given password(p) meets all of the requirements
    valid_lower = False
    valid_upper = False
    valid_digits = False
    valid_length = False
    is_valid = False
    if len(p) >= 6 and len(p) <= 16:
        valid_length = True
    
    for char in p:
        if char.isalpha():
            valid_lower = True
    
    for char in p:
        if ord(char) < 96:
            valid_upper = True

    for char in p:
          if char.isdigit():
            valid_digits = True
              
    if valid_length and valid_lower and valid_upper and valid_digits == True:
        is_valid = True
    
    if is_valid != True:
        error = "Invalid Password."
        return(error)
    
    if is_valid == True:
        valid_msg = f"{p} is a valid password!"
        return valid_msg

def update_pass():
    #Function that runs valid_pass() and outputs results for a given password
    pw = entry_box.get()
    data = pw
    data = valid_pass(data)
    result_label.config(text=f"""Results:
    {data}
    """)

#Tkinter gui elements
entry_label = tk.Label(root, text="Enter Password")
entry_box = tk.Entry(root,)
button = tk.Button(root, text="Go", command=update_pass)
info_label = tk.Label(root, text="""
Password Requirements:
Minimum length 6 characters.
Maximum length 16 characters.
At least 1 Uppercase letter.
At least 1 Lowercase letter.
At least 1 number between [0-9].
""")
result_label = tk.Label(root, text="Result: ")

#tkinter structure
info_label.pack()
entry_label.pack()
entry_box.pack()
button.pack()
result_label.pack()

#executes main loop
root.mainloop()