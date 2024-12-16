import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CGP calculation")
        self.marks = []
        self.marks.append(("Python", 80, "A"))
        self.marks.append(("Ist", 70, "B"))
        self.marks.append(("English", 50, "C"))

        full_window_frame = ttk.Frame(self)
        full_window_frame.grid(row=0, column=0, padx=0, pady=10)

        self.student_label1 = ttk.Label(full_window_frame, text="OOP")
        self.student_label1.grid(row=0, column=0, padx=10, pady=10)
        self.student_var1 = tk.StringVar()
        self.student_entry1 = ttk.Entry(full_window_frame, width=50)
        self.student_entry1.grid(row=0, column=1, padx=10, pady=10)
        self.student_entry1["textvariable"] = self.student_var1

        
        self.student_label2 = ttk.Label(full_window_frame, text="ICT")
        self.student_label2.grid(row=3, column=0, padx=10, pady=10)
        self.student_var2 = tk.StringVar()
        self.student_entry2 = ttk.Entry(full_window_frame, width=50)
        self.student_entry2.grid(row=3, column=1, padx=10, pady=10)
        self.student_entry2["textvariable"] = self.student_var2

        
        self.student_label3 = ttk.Label(full_window_frame, text="IST")
        self.student_label3.grid(row=6, column=0, padx=10, pady=10)
        self.student_var3 = tk.StringVar()
        self.student_entry3 = ttk.Entry(full_window_frame, width=50)
        self.student_entry3.grid(row=6, column=1, padx=10, pady=10)
        self.student_entry3["textvariable"] = self.student_var3
        
        self.student_label4 = ttk.Label(full_window_frame, text="ENG")
        self.student_label4.grid(row=9, column=0, padx=10, pady=10)
        self.student_var4 = tk.StringVar()
        self.student_entry4 = ttk.Entry(full_window_frame, width=50)
        self.student_entry4.grid(row=9, column=1, padx=10, pady=10)
        self.student_entry4["textvariable"] = self.student_var4

        self.marks_label = ttk.Label(full_window_frame, text="Total Marks")
        self.marks_label.grid(row=12, column=0, padx=10, pady=10)

        self.marks_var = tk.IntVar()
        self.marks_entry = ttk.Entry(full_window_frame, width=50)
        self.marks_entry.grid(row=15, column=1, padx=10, pady=10)
        self.marks_entry["textvariable"] = self.marks_var

        self.cgp_label = ttk.Label(full_window_frame, text="CGPA")
        self.cgp_label.grid(row=18, column=0, padx=10, pady=10)

        self.cgp_var = tk.StringVar()
        self.cgp_entry = ttk.Entry(full_window_frame, justify="right", width=20)
        self.cgp_entry.grid(row=20, column=1, padx=10, pady=10, sticky="w")
        self.cgp_entry["textvariable"] = self.cgp_var

        self.student_save_button = ttk.Button(full_window_frame, text="Save student marks")
        self.student_save_button.grid(row=22, column=0, padx=10, pady=10)
        self.student_save_button.bind('<Button-1>', self.save_student)

        self.student_show_button = ttk.Button(full_window_frame, text="Double click here to show subject by marks")
        self.student_show_button.grid(row=22, column=1, padx=10, pady=10, sticky="w")
        self.student_show_button.bind('<Double-1>', self.show_student)

    def save_student(self, event):
        self.cgp()
        self.sum()
        self.marks.append((self.student_var1.get(),self.student_var2.get(),self.student_var3.get(),self.student_var4.get(), self.marks_var.get(), self.cgp_var.get()))
        messagebox.showinfo(title="Student Save Info", message=f"Student: {self.student_var.get()}, {self.marks_var.get()}, {self.cgp_var.get()} saved")

    def show_student(self, event):
        available = False
        for b in self.marks:
            if b[0] == self.student_var.get():
                self.marks_var.set(b[1])
                self.cgp_var.set(b[2])
                available = True
        if not available:
            messagebox.askokcancel(title="Student Availability", message="Not available")
    def sum(self):
        
    def cgp(self):
        m = self.marks_var.get()
        if m > 80:
            self.cgp_var.set('A   4 points')
        elif 70 < m <= 80:
            self.cgp_var.set('B   3 points')
        elif 60 <= m <= 70:
            self.cgp_var.set('C   1 points')
        else:
            self.cgp_var.set('F   0 points')


def main():
    App().mainloop()

main()
