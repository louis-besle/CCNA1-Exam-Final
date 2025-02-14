# CCNA1-Exam-Final

# Documentation pour le programme `qcm.py`

## Prérequis

1. **Python** : Assurez-vous d'avoir Python installé sur votre machine. Vous pouvez télécharger Python depuis [python.org](https://www.python.org/downloads/).

2. **Fichiers nécessaires** :
   - `qcm.py` : Le fichier principal contenant le code du programme.
   - `questions_answers.json` : Un fichier JSON contenant les questions et les réponses pour le quiz.

## Étapes pour exécuter le programme

1. **Installer Python** :
   - Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/).
   - Assurez-vous de cocher l'option pour ajouter Python au PATH lors de l'installation.

2. **Préparer les fichiers** :
   - Placez `qcm.py` et `questions_answers.json` dans le même répertoire.

3. **Contenu du fichier `questions_answers.json`** :
   - Créez un fichier `questions_answers.json` dans le même répertoire que `qcm.py`.
   - Ajoutez-y les questions et réponses au format suivant :

    ```json
    [
        {
            "question": "Question 1?",
            "answers": ["Réponse 1", "Réponse 2", "Réponse 3", "Réponse 4"],
            "correct_answers": ["Réponse 1", "Réponse 3"]
        },
        {
            "question": "Question 2?",
            "answers": ["Réponse 1", "Réponse 2", "Réponse 3"],
            "correct_answers": ["Réponse 2"]
        }
    ]
    ```

## Exécuter le programme

1. **Ouvrir une fenêtre de terminal** :
   - Sur Windows : Appuyez sur `Win + R`, tapez `cmd` et appuyez sur Entrée.
   - Sur macOS : Ouvrez `Terminal` depuis les Applications.
   - Sur Linux : Ouvrez votre terminal préféré.

2. **Naviguer vers le répertoire contenant les fichiers** :
   - Utilisez la commande `cd` pour changer de répertoire.

    ```sh
    cd chemin/vers/repertoire
    ```

3. **Exécuter le programme** :

    ```sh
    python qcm.py
    ```

## Utiliser l'application

1. **Interface graphique** :
   - Une fenêtre s'ouvrira avec la première question du quiz.
   - Lisez la question affichée en haut de la fenêtre.
   - Sélectionnez les réponses en cochant les cases correspondantes.
   - Cliquez sur le bouton "Suivant" pour valider vos réponses et passer à la question suivante.

2. **Fin du quiz** :
   - À la fin du quiz, une boîte de dialogue affichera votre score final.
   - Cliquez sur "OK" pour fermer l'application.

## Dépannage

- Si vous rencontrez des erreurs, assurez-vous que :
  - Le fichier `questions_answers.json` est bien formé (vérifiez la syntaxe JSON).
  - Vous avez Python installé et configuré correctement.
  - Les fichiers `qcm.py` et `questions_answers.json` sont dans le même répertoire.

## Conclusion

Cette documentation vous guide à travers l'installation et l'exécution du programme `qcm.py`. Assurez-vous de suivre chaque étape attentivement pour garantir le bon fonctionnement de l'application.