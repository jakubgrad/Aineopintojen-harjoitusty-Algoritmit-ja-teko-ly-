import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        initialdir="../maps",
        filetypes=[("Text Files", "*.map"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def run_dijkstra():
    print(txt_edit.get("1.0", "end-1c"))
    

def clear_start_coordinates(event):
    """Clear the default text when the entry widget is focused."""
    if start_coordinates_entry.get() == "E.g. 1,1":
        start_coordinates_entry.delete(0, tk.END)

def clear_goal_coordinates(event):
    """Clear the default text when the entry widget is focused."""
    if goal_coordinates_entry.get() == "E.g. 4,7":
        goal_coordinates_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.FLAT, bd=2)
btn_open = tk.Button(frm_buttons, text="Choose map", command=open_file)
btn_dijkstra = tk.Button(frm_buttons, text="Run Dijkstra",command=run_dijkstra)
btn_jps = tk.Button(frm_buttons, text="Run JPS",command=open_file)

lbl_start_coordinates = tk.Label(frm_buttons, text="Start Coordinates:")
lbl_goal_coordinates = tk.Label(frm_buttons, text="Goal Coordinates:")

start_coordinates_entry = tk.Entry(frm_buttons)
start_coordinates_entry.insert(0, "E.g. 1,1")  # Set default text
start_coordinates_entry.bind("<FocusIn>", clear_start_coordinates)  # Bind event handler

goal_coordinates_entry = tk.Entry(frm_buttons)
goal_coordinates_entry.insert(0, "E.g. 4,7")  # Set default text
goal_coordinates_entry.bind("<FocusIn>", clear_goal_coordinates)  # Bind event handler

btn_open.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
btn_dijkstra.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

lbl_start_coordinates.grid(row=2, column=0, sticky="w", padx=5, pady=5)
start_coordinates_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

lbl_goal_coordinates.grid(row=4, column=0, sticky="w", padx=5, pady=5)
goal_coordinates_entry.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

btn_jps.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()

