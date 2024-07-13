import tkinter as tk

root = tk.Tk()

# Define the options for the dropdown
options = ["Apple", "Banana", "Orange", "Grape"]

# Create a StringVar to store the selected value
selected_value = tk.StringVar(root)
selected_value.set(options[0])  # Set the initial value

# Create a Listbox hidden by default
listbox = tk.Listbox(root, listvariable=selected_value, height=len(options), exportselection=False)
listbox.pack(pady=10)

# Hide the Listbox initially
listbox.pack_forget()

# Create a button to toggle the Listbox
def toggle_listbox():
    if listbox.winfo_ismapped():
        listbox.pack_forget()
    else:
        listbox.pack(pady=10)

button = tk.Button(root, text="Select Fruit", command=toggle_listbox)
button.pack()

# Create a label to display the selected value
label = tk.Label(root, textvariable=selected_value)
label.pack()

root.mainloop()