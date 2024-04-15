import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from config import default_jps, default_dijkstra


class UI:
    def __init__(self, window, algorithm_service):
        self.window = window
        self.font = ("Consolas", 18)
        self.algorithm_service = algorithm_service
        self.slides = []
        self.counter = 0
        self.max_counter = 0
        self.job_ids = []
        self.create_widgets()

    def start(self):
        self.create_widgets()

    def update_text(self, new_text):
        self.txt_edit.delete("1.0", tk.END)
        self.txt_edit.insert(tk.END, new_text)

    def update_counter(self, number):
        if type(number) == str:
            number = int(number)
        if 0 <= number <= self.max_counter:
            self.counter = number
            self.update_text(self.slides[number])
            self.lbl_update_counter.config(
                text=f"Browse slides from 0 to {self.max_counter}, current is {self.counter}")
            return True
        return False

    def update_font_size(self, size):
        old_font_name = self.font[0]
        self.font = (old_font_name, size)
        self.txt_edit.config(font=self.font)

    def create_widgets(self):
        self.window.title("JPS vs Dijkstra")
        self.window.rowconfigure(0, minsize=800, weight=1)
        self.window.columnconfigure(1, minsize=800, weight=1)

        self.txt_edit = tk.Text(self.window, font=self.font)
        self.frm_buttons = tk.Frame(self.window, relief=tk.FLAT, bd=2)

        self.btn_open = tk.Button(
            self.frm_buttons, text="Choose map", bg="#000080", fg="#ffffff", command=self.open_file)

        self.btn_dijkstra = tk.Button(
            self.frm_buttons, text="Run Dijkstra", bg="#000080", fg="#ffffff", command=self.run_dijkstra)

        self.btn_jps = tk.Button(
            self.frm_buttons, text="Run JPS", bg="#000080", fg="#ffffff", command=self.run_jps)

        self.btn_def_dijkstra = tk.Button(
            self.frm_buttons, text="Run Default Dijkstra", bg="#808000", fg="#ffffff", command=self.run_default_dijkstra)

        self.btn_def_jps = tk.Button(
            self.frm_buttons, text="Run Default JPS", bg="#808000", fg="#ffffff", command=self.run_default_jps)

        self.lbl_start_coordinates = tk.Label(
            self.frm_buttons, bg="#000080", fg="#ffffff", padx=5, pady=5, text="Start Coordinates")

        self.lbl_goal_coordinates = tk.Label(
            self.frm_buttons, bg="#000080", fg="#ffffff", font=("Consolas", 10), padx=5, pady=5, text="Goal Coordinates")

        self.start_coordinates_entry = tk.Entry(self.frm_buttons)
        self.start_coordinates_entry.insert(0, "1,1")
        self.start_coordinates_entry.bind(
            "<FocusIn>", self.clear_start_coordinates)

        self.goal_coordinates_entry = tk.Entry(self.frm_buttons)
        self.goal_coordinates_entry.insert(0, "4,7")
        self.goal_coordinates_entry.bind(
            "<FocusIn>", self.clear_goal_coordinates)

        self.btn_decrease_counter = tk.Button(
            self.frm_buttons, text="←", bg="#ff8c00", fg="#ffffff", command=lambda: self.update_counter(self.counter-1))

        self.btn_increase_counter = tk.Button(
            self.frm_buttons, text="→", bg="#ff8c00", fg="#ffffff", command=lambda: self.update_counter(self.counter+1))

        self.lbl_font = tk.Label(
            self.frm_buttons, text="Change font size")

        self.btn_decrease_font = tk.Button(
            self.frm_buttons, text="-", bg="#9400D3", fg="#ffffff", command=lambda: self.update_font_size(self.font[1]-1))
        self.btn_increase_font = tk.Button(
            self.frm_buttons, text="+", bg="#9400D3", fg="#ffffff", command=lambda: self.update_font_size(self.font[1]+1))

        self.counter_entry = tk.Entry(self.frm_buttons)
        self.counter_entry.bind(
            "<Return>", lambda event: self.update_counter(self.counter_entry.get()))
        self.counter_entry.insert(0, "E.g. 4,7")
        self.counter_entry.bind(
            "<FocusIn>", self.clear_counter_entry)

        self.btn_update_counter = tk.Button(
            self.frm_buttons, text="Update counter", bg="#ff8c00", fg="#ffffff", command=lambda: self.update_counter(self.counter_entry.get()))

        self.lbl_update_counter = tk.Label(
            self.frm_buttons, text="Browse slides")

        self.btn_animate = tk.Button(
            self.frm_buttons, text="Animate!", bg="#208B83", fg="#ffffff", command=lambda: self.animate(self.counter))

        self.btn_animate_start = tk.Button(
            self.frm_buttons, text="Animate from start!", bg="#2AC6B9", fg="#ffffff", command=lambda: self.animate(0))

        self.btn_stop_animation = tk.Button(
            self.frm_buttons, text="Stop animation", bg="#FF0000", fg="#ffffff", command=lambda: self.stop_animation())

        self.lbl_log = tk.Label(
            self.frm_buttons, text="Log")

        self.txt_log = tk.Text(
            self.frm_buttons, font=("Consolas", 11), wrap="word", height=30, width=60)

        self.txt_log.config(state=tk.DISABLED)

        self.btn_open.grid(row=0, column=0, columnspan=2,
                           sticky="ew", padx=5, pady=5)

        self.btn_dijkstra.grid(
            row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.btn_jps.grid(row=4, column=0, columnspan=2,
                          sticky="ew", padx=5, pady=5)

        self.lbl_start_coordinates.grid(
            row=1, column=0, columnspan=1, sticky="w", padx=5, pady=5)

        self.lbl_goal_coordinates.grid(
            row=1, column=1, columnspan=1, sticky="w", padx=5, pady=5)

        self.start_coordinates_entry.grid(
            row=2, column=0, columnspan=1, sticky="ew", padx=5, pady=5)

        self.goal_coordinates_entry.grid(
            row=2, column=1, columnspan=1, sticky="ew", padx=5, pady=5)

        self.btn_def_jps.grid(row=7, column=0, columnspan=2,
                              sticky="ew", padx=5, pady=5)

        self.btn_def_dijkstra.grid(row=8, column=0, columnspan=2,
                                   sticky="ew", padx=5, pady=5)

        self.btn_decrease_counter.grid(row=9, column=0, columnspan=1,
                                       sticky="ew", padx=0, pady=5)

        self.btn_increase_counter.grid(row=9, column=1, columnspan=1,
                                       sticky="ew", padx=0, pady=5)

        self.counter_entry.grid(row=10, column=0, columnspan=1,
                                sticky="ew", padx=0, pady=5)

        self.btn_update_counter.grid(row=10, column=1, columnspan=1,
                                     sticky="ew", padx=0, pady=5)

        self.lbl_update_counter.grid(row=11, column=0, columnspan=2,
                                     sticky="ew", padx=5, pady=1)

        self.btn_animate.grid(row=12, column=0, columnspan=1,
                              sticky="ew", padx=0, pady=5)

        self.btn_animate_start.grid(row=12, column=1, columnspan=1,
                                    sticky="ew", padx=0, pady=5)

        self.btn_stop_animation.grid(row=13, column=0, columnspan=2,
                                     sticky="ew", padx=5, pady=5)

        self.lbl_font.grid(row=14, column=0, columnspan=2,
                           sticky="ew", padx=5, pady=1)

        self.btn_decrease_font.grid(row=15, column=0, columnspan=1,
                                    sticky="ew", padx=0, pady=5)

        self.btn_increase_font.grid(row=15, column=1, columnspan=1,
                                    sticky="ew", padx=0, pady=5)

        self.lbl_log.grid(
            row=16, column=0, sticky="w", padx=5, pady=5)

        self.txt_log.grid(
            row=17, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

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

    def run_default_dijkstra(self):
        self.run_algorithm(dijkstra=True, jps=False,
                           start="4,4", goal="7,7", map=default_dijkstra)

    def update_log(self, message):
        self.txt_log.config(state=tk.NORMAL)
        self.txt_log.insert("1.0", message + "\n")
        self.txt_log.config(state=tk.DISABLED)

    def run_default_jps(self):
        self.run_algorithm(dijkstra=False, jps=True,
                           start="1,1", goal="4,7", map=default_jps)

    def run_dijkstra(self):
        self.run_algorithm(dijkstra=True)

    def run_jps(self):
        self.run_algorithm(jps=True)

    def run_algorithm(self, dijkstra=False, jps=False, start=False, goal=False, map=False):
        start = start if start else self.start_coordinates_entry.get()
        goal = goal if goal else self.goal_coordinates_entry.get()
        map = map if map else self.filepath

        self.slides = []

        if not self.algorithm_service.coordinates_ok(start, goal):
            return

        distance = self.algorithm_service.run_algorithm(
            start, goal, map, self.slides, dijkstra=dijkstra, jps=jps, visualization=False)
        self.clear_log()
        self.update_log(f"Distance is {distance}")
        self.max_counter = len(self.slides)-1
        self.counter = self.max_counter
        self.update_text(self.slides[self.counter])
        self.lbl_update_counter.config(
            text=f"Browse slides from 0 to {self.max_counter}")

    def clear_start_coordinates(self, event):
        if self.start_coordinates_entry.get() == "E.g. 1,1":
            self.start_coordinates_entry.delete(0, tk.END)

    def clear_goal_coordinates(self, event):
        if self.goal_coordinates_entry.get() == "E.g. 4,7":
            self.goal_coordinates_entry.delete(0, tk.END)

    def clear_counter_entry(self, event):
        self.counter_entry.delete(0, tk.END)

    def clear_log(self):
        self.txt_log.config(state=tk.NORMAL)
        self.txt_log.delete("1.0", tk.END)
        self.txt_log.config(state=tk.DISABLED)

    def animate(self, start=0):
        self.stop_animation()  # Stop any ongoing animation
        self.job_ids = []  # Reset job IDs list
        for idx, slide in enumerate(self.slides[start:], start=start):
            job_id = self.window.after(
                (idx - start) * 400, lambda s=slide, c=idx: self.update_text_and_counter(s, c))
            self.update_counter(self.counter+1)
            # print(f"self.counter{self.counter}")
            self.lbl_update_counter.config(
                text=f"Browse slides from 0 to {self.max_counter}, current is {self.counter}")
            self.job_ids.append(job_id)  # Store the job ID

    def update_text_and_counter(self, slide, counter):
        self.update_text(slide)
        self.update_counter(counter)
        self.lbl_update_counter.config(
            text=f"Browse slides from 0 to {self.max_counter}, current is {counter}")
        self.counter_entry.delete(0, tk.END)
        self.counter_entry.insert(0, f"{self.counter}")

    def stop_animation(self):
        for job_id in self.job_ids:
            self.window.after_cancel(job_id)


def main():
    window = tk.Tk()
    ui = UI(window)
    window.mainloop()


if __name__ == "__main__":
    main()
