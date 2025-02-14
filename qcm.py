import json
import tkinter as tk
from tkinter import messagebox

class QCMApp:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        self.compteur = 0
        self.current_question = 0
        self.score = 0

        # Configuration de la fenêtre
        self.root.title("CCNA Exam Final")
        self.root.geometry("1900x1060")

        # Widgets
        self.question_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_vars = []
        self.answer_buttons = []
        for i in range(6):  # On suppose qu'il y a au maximum 6 réponses par question
            var = tk.IntVar()
            button = tk.Checkbutton(root, text="", variable=var, wraplength=500, font=("Arial", 12))
            button.pack(anchor="w")
            self.answer_vars.append(var)
            self.answer_buttons.append(button)

        self.next_button = tk.Button(root, text="Suivant", command=self.next_question, font=("Arial", 12), bg="black", fg="white", width=10, height=1, activebackground="white", activeforeground="black")
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(root, text=f"Score: {self.score}/{self.compteur}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Charger la première question
        self.load_question()

    def load_question(self):
        """Charge la question actuelle et les réponses."""
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])

        # Réinitialiser les cases à cocher
        for var in self.answer_vars:
            var.set(0)

        # Afficher les réponses
        for i, answer in enumerate(question_data["answers"]):
            self.answer_buttons[i].config(text=answer)
            self.answer_buttons[i].pack(anchor="w")  # Afficher le bouton

        # Masquer les boutons inutilisés
        for i in range(len(question_data["answers"]), 6):
            self.answer_buttons[i].pack_forget()

    def next_question(self):
        """Passe à la question suivante et vérifie les réponses."""
        # Vérifier les réponses sélectionnées
        selected_answers = [i for i, var in enumerate(self.answer_vars) if var.get() == 1]
        correct_answers = [self.questions[self.current_question]["answers"].index(ans) for ans in self.questions[self.current_question]["correct_answers"]]

        self.compteur += 1
        if set(selected_answers) == set(correct_answers):
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}/{self.compteur}")

        # Passer à la question suivante
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Fin du QCM", f"Vous avez terminé le QCM avec un score de {self.score}/{len(self.compteur)}")
            self.root.quit()

# Charger les questions depuis le fichier JSON
def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Point d'entrée du programme
if __name__ == "__main__":
    questions = load_questions("questions_answers.json")

    # Créer l'interface graphique
    root = tk.Tk()
    app = QCMApp(root, questions)
    root.mainloop()