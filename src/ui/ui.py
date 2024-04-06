
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class UI:
    def __init__(self, window,algorithm_service):
        self.window = window
        self.create_widgets()
        self.algorithm_service = algorithm_service

    def start(self):
        self.create_widgets()

    def update_text(self, new_text):
        self.txt_edit.delete("1.0", tk.END)  # Clear previous text
        self.txt_edit.insert(tk.END, new_text)  # Insert new text

    def create_widgets(self):
        self.window.title("Simple Text Editor")
        self.window.rowconfigure(0, minsize=800, weight=1)
        self.window.columnconfigure(1, minsize=800, weight=1)

        self.txt_edit = tk.Text(self.window, font=("Consolas", 16))
        self.frm_buttons = tk.Frame(self.window, relief=tk.FLAT, bd=2)
        self.btn_open = tk.Button(self.frm_buttons, text="Choose map", command=self.open_file)
        self.btn_dijkstra = tk.Button(self.frm_buttons, text="Run Dijkstra", command=self.run_dijkstra)
        self.btn_jps = tk.Button(self.frm_buttons, text="Run JPS", command=self.run_jps)

        self.lbl_start_coordinates = tk.Label(self.frm_buttons, text="Start Coordinates:")
        self.lbl_goal_coordinates = tk.Label(self.frm_buttons, text="Goal Coordinates:")

        self.start_coordinates_entry = tk.Entry(self.frm_buttons)
        self.start_coordinates_entry.insert(0, "E.g. 1,1")
        self.start_coordinates_entry.bind("<FocusIn>", self.clear_start_coordinates)

        self.goal_coordinates_entry = tk.Entry(self.frm_buttons)
        self.goal_coordinates_entry.insert(0, "E.g. 4,7")
        self.goal_coordinates_entry.bind("<FocusIn>", self.clear_goal_coordinates)

        self.btn_open.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.btn_dijkstra.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.lbl_start_coordinates.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.start_coordinates_entry.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.lbl_goal_coordinates.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.goal_coordinates_entry.grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        self.btn_jps.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.frm_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=1, sticky="nsew")
        self.filepath = ""

    def open_file(self):
        self.filepath = askopenfilename(
            initialdir="maps",
            filetypes=[("Text Files", "*.map"), ("All Files", "*.*")]
        )
        if not self.filepath:
            return
        self.txt_edit.delete("1.0", tk.END)
        with open(self.filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
            
        self.window.title(f"Simple Text Editor - {self.filepath}")

    def run_dijkstra(self):
        self.run_algorithm(dijkstra=True)

    def run_jps(self):
        self.run_algorithm(jps=True)

    def run_algorithm(self,dijkstra=False,jps=False):
        start = self.start_coordinates_entry.get()
        goal = self.goal_coordinates_entry.get()
        map = self.filepath
        start = self.coordinates_ok(start)
        goal = self.coordinates_ok(goal)
        if start == False or goal == False:
            return
        print("coordinates ok")
        callback = lambda new_text: self.update_text(new_text)
        slides = []
        self.algorithm_service.run_algorithm(start, goal, map, slides, dijkstra=dijkstra, jps=jps, visualization=False)
        for idx, slide in enumerate(slides):
            self.window.after(idx * 400, lambda s=slide: self.update_text(s))
       
    def coordinates_ok(self, input_text):
        try:
            coordinates = input_text.split(',')
            if len(coordinates) != 2:
                raise ValueError("Invalid input format")
            x = int(coordinates[0])
            y = int(coordinates[1])
            if not (isinstance(x, int) and isinstance(y, int)):
                raise ValueError("Both coordinates must be integers")
            return (x,y) 
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return False

    def clear_start_coordinates(self, event):
        if self.start_coordinates_entry.get() == "E.g. 1,1":
            self.start_coordinates_entry.delete(0, tk.END)

    def clear_goal_coordinates(self, event):
        if self.goal_coordinates_entry.get() == "E.g. 4,7":
            self.goal_coordinates_entry.delete(0, tk.END)

def main():
    window = tk.Tk()
    ui = UI(window)
    window.mainloop()

if __name__ == "__main__":
    main()

