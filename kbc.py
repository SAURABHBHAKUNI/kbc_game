import tkinter as tk
from tkinter import messagebox
from questions import QUESTIONS

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.current_question = 0
        self.money = 0
        self.lifeline_used = False
        self.setup_gui()
        self.load_question()

    def setup_gui(self):
        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=600, justify="center")
        self.question_label.pack(pady=20)

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", font=("Arial", 14), width=20, command=lambda i=i: self.check_answer(i + 1))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Lifeline and Quit Buttons
        self.lifeline_button = tk.Button(self.root, text="Lifeline", font=("Arial", 14), command=self.use_lifeline)
        self.lifeline_button.pack(side="left", padx=20)

        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 14), command=self.quit_game)
        self.quit_button.pack(side="right", padx=20)

        # Money Label
        self.money_label = tk.Label(self.root, text="Money: 0", font=("Arial", 14))
        self.money_label.pack(pady=20)

    def load_question(self):
        if self.current_question >= len(QUESTIONS):
            self.game_over("Congrats!! You answered all the questions correctly!!\nTotal Money Won: {}".format(self.money))
            return

        question = QUESTIONS[self.current_question]
        self.question_label.config(text=f"Question {self.current_question + 1}: {question['name']}")
        self.money_label.config(text=f"Money: {self.money}")

        for i in range(4):
            self.option_buttons[i].config(text=f"Option {i + 1}: {question['option' + str(i + 1)]}", state="normal")

    def check_answer(self, selected_option):
        question = QUESTIONS[self.current_question]
        correct_answer = question["answer"]

        if selected_option == correct_answer:
            messagebox.showinfo("Correct!", "You answered correctly!")
            self.money += question["money"]
            self.current_question += 1
            self.load_question()
        else:
            self.game_over(f"Incorrect! The correct answer was Option {correct_answer}.\nMoney Won: {self.money}")

    def use_lifeline(self):
        if self.lifeline_used:
            messagebox.showwarning("Lifeline Used", "You have already used the lifeline!")
            return

        self.lifeline_used = True
        question = QUESTIONS[self.current_question]
        correct_answer = question["answer"]
        incorrect_options = [1, 2, 3, 4]
        incorrect_options.remove(correct_answer)

        # Hide two incorrect options
        hide_options = incorrect_options[:2]
        for i in hide_options:
            self.option_buttons[i - 1].config(text="", state="disabled")

    def quit_game(self):
        self.game_over(f"You chose to quit!\nTotal Money Won: {self.money}")

    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()