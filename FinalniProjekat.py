import tkinter as tk
from tkinter import messagebox

current_question = 0
score = 0
quiz_file = "quiz_results.txt"

questions = [
    {"question": "Koji je glavni grad Bosne i Hercegovine?", "options": ["Berlin", "Atina", "Sarajevo"], "answer": "Sarajevo"},
    {"question": "Koje je četvrto slovo u grčkoj abecedi?", "options": ["Alfa", "Delta", "Sigma"], "answer": "Delta"},
    {"question": "Na kojem programskom jeziku je napisan ovaj kviz?", "options": ["Python", "C++", "Java"], "answer": "Python"},
    {"question": "Koja je tacka ključanja vode?", "options": ["100°", "20°", "0°"], "answer": "100°"},
    {"question": "Koja je zivotinja poznata kao kralj dzungle?", "options": ["Slon", "Lav", "Zebra"], "answer": "Lav"},
    {"question": "Koliko jedan kosarkaski tim ima igraca na terenu tokom igre?", "options": ["10", "6", "5"], "answer": "5"}
    
]

def next_question():
    global current_question, score
    selected = answer.get()
    if selected == "":
        messagebox.showwarning("No answer", "Please select an option.")
        return

    if selected == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question >= len(questions):
        end_quiz()
    else:
        load_question()

def load_question():
    question_label.config(text=questions[current_question]["question"])
    options = questions[current_question]["options"]
    answer.set("")
    for i in range(3):
        radio_buttons[i].config(text=options[i], value=options[i])

def end_quiz():
    save_score()
    messagebox.showinfo("Quiz Completed", f"You scored {score}/{len(questions)}")
    root.destroy()

def save_score():
    with open(quiz_file, "a") as file:
        file.write(f"Score: {score}/{len(questions)}\n")


root = tk.Tk()
root.title("Simple Quiz")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

answer = tk.StringVar()

radio_buttons = []
for i in range(3): 
    rb = tk.Radiobutton(root, text="", variable=answer, value="", font=("Arial", 12))
    rb.pack(anchor="w", padx=50)
    radio_buttons.append(rb)

next_btn = tk.Button(root, text="Next", command=next_question, font=("Arial", 12))
next_btn.pack(pady=20)

load_question()
