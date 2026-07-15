
import live_detect as l
import recognise_human_activity as m
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Object detection using ELM")
window.geometry("1000x800")
window.configure(bg="#FFFFFF")

# Create the navbar frame
navbar = tk.Frame(window, bg="#1E90FF", height=50)
navbar.pack(side="top", fill="x")

# Add the navbar title
title = tk.Label(navbar, text="Action detection using ELM", font=("Arial Bold", 20), bg="#1E90FF", fg="#FFFFFF")
title.place(relx=0.5, rely=0.5, anchor="center")

# Create the content frame
content = tk.Frame(window, bg="#FFFFFF")
content.pack(side="top", fill="both", expand=True)

# Add the input box
input_frame = tk.Frame(content, bg="#FFFFFF")
input_frame.pack(side="top", pady=50)

input_label = tk.Label(input_frame, text="Upload a video file:", font=("Arial", 14), bg="#FFFFFF")
input_label.pack(side="top", pady=10)

input_box = tk.Entry(input_frame, width=56, font=("Arial", 14), bd=1, relief="solid")
input_box.pack(padx=10, pady=20, ipady=5)



# Add the upload and clear buttons
button_frame = tk.Frame(input_frame, bg="#FFFFFF")
button_frame.pack()

def browse_video():
    # Open a file dialog to browse for a video file
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.gif")])
    
    # Update the input box with the selected file path
    input_box.delete(0, tk.END)
    input_box.insert(0, file_path)
    m.video_path = input_box.get()

upload_button = tk.Button(button_frame, text="Upload", font=("Arial", 14), bg="#1E90FF", fg="#FFFFFF", width=12, cursor="hand2", bd=0, activebackground="#0080FF", command=browse_video)
upload_button.pack(side="left", padx=10)

def clear_input():
    # Clear the input box
    input_box.delete(0, tk.END)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 14), bg="#DC143C", fg="#FFFFFF", width=12, cursor="hand2", bd=0, activebackground="#FF4040", command=clear_input)
clear_button.pack(side="left", padx=10, pady=10)

def my_function():
    # Do something when the submit button is clicked

    m.my_function()
# Add the submit button
submit_button = tk.Button(button_frame, text="Submit", font=("Arial", 14), bg="#E0FFFF", fg="#000000", width=12, cursor="hand2", bd=0, activebackground="#B0E0E6", command=my_function)
submit_button.pack(side="left", padx=10)

def detect_live():
    l.live()
    

detect_live_button = tk.Button(button_frame, text="Detect Live", font=("Arial", 14), bg="#32CD32", width=12, cursor='hand2', bd=0, activebackground="#006400", command=detect_live)
detect_live_button.pack(side="left", padx=10)

# Create the footer frame
footer = tk.Frame(window, bg="#CCCCCC", height=30)
footer.pack(side="bottom", fill="x")

# Add the footer text
footer_label = tk.Label(footer, text="© 2023 My Company. All rights reserved.", font=("Arial", 10), bg="#CCCCCC")
footer_label.place(relx=0.5, rely=0.5, anchor="center")



#code for using backend
param = m.Parameters()
#m.video_path = input_box.get()



# Start the main loop
window.mainloop()
