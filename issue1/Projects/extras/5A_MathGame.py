import tkinter as tk
from tkinter import messagebox



class EquationGame:
    def __init__(self, master):
        
        self.master = master
        self.master.title("Equation Game")

        self.equations = [
            ("2 + 2 =", 4),
            ("3 * 5 =", 15),
            ("10 / 2 =", 5),
            ("8 - 3 =", 5)
        ]
        self.current_eq_index = 0
        self.numCorrect = 0
        self.numIncorrect = 0
        self.create_widgets()

    def create_widgets(self):
        
        self.equation_label = tk.Label(self.master, text="")
        self.equation_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack(pady=5)

        self.check_button = tk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=5)

        self.next_button = tk.Button(self.master, text ="Next Equation", command = self.next_equation)
        self.next_button.pack(pady=5)

        self.numIncorrect_label = tk.Label(self.master, text=f"Number Incorrect: {self.numIncorrect}")
        self.numIncorrect_label.pack(pady=5)

        self.update_equation()

    def update_equation(self):
        equation_text, _ = self.equations[self.current_eq_index]
        self.equation_label.config(text=equation_text)

    def check_answer(self):
        _, correct_answer = self.equations[self.current_eq_index]
        user_answer = self.answer_entry.get()
        try:
            user_answer = float(user_answer)
            if user_answer == correct_answer:
                messagebox.showinfo("Correct", "Congratulations! Your answer is correct.")
            else:
                messagebox.showerror("Incorrect", "Sorry, that's the wrong answer. Please try again.")
                self.update_incorrect_label()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def update_incorrect_label(self):
        self.numIncorrect += 1
        self.numIncorrect_label.config(text=f"Number Incorrect: {self.numIncorrect}")

    def next_equation(self):
        self.current_eq_index = (self.current_eq_index + 1) % len(self.equations)
        self.update_equation()
        self.answer_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.geometry('300x200')
    app = EquationGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()