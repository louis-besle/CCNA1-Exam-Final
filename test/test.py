import json
from bs4 import BeautifulSoup

# Charger le contenu HTML
with open('test.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parser le HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver toutes les questions et réponses
questions = []
for strong_tag in soup.find_all('strong'):
    question_text = strong_tag.get_text(strip=True)
    if "?" in question_text:  # S'assurer que c'est une question
        # Trouver la liste des réponses suivante
        ul_tag = strong_tag.find_next('ul')
        if ul_tag:
            answers = [li.get_text(strip=True) for li in ul_tag.find_all('li')]
            # Identifier les réponses correctes
            correct_answers = [li.get_text(strip=True) for li in ul_tag.find_all('li', class_='correct_answer')]
            questions.append({
                "question": question_text,
                "answers": answers,
                "correct_answers": correct_answers
            })

# Enregistrer les questions et réponses dans un fichier JSON
with open('questions_answers.json', 'w', encoding='utf-8') as json_file:
    json.dump(questions, json_file, ensure_ascii=False, indent=4)

print("Les questions et réponses ont été extraites et enregistrées dans 'questions_answers.json'.")