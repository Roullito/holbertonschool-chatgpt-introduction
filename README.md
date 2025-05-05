# ChatGPT - Introduction

> Projet Holberton School : découverte de l’intégration de l’IA dans les pratiques de développement logiciel.

## Table of Contents

- [Description](#description)
- [Technologies](#technologies)
- [Objectifs du projet](#objectifs-du-projet)
- [Fonctionnalités principales](#fonctionnalités-principales)
- [Structure du projet](#structure-du-projet)

---

## Description

Ce projet vise à explorer l’utilisation de **ChatGPT** comme assistant au développement, avec une mise en pratique sur deux axes fondamentaux :
- **Débogage de code (Debugging)**
- **Automatisation de tâches de développement (Automation)**

L’idée est de comprendre comment une IA peut améliorer notre efficacité, clarifier les erreurs, produire du code répétitif, et écrire une documentation plus lisible.

---

## Technologies

- Python 3.8+
- HTML5 / CSS3 / JavaScript
- Git & GitHub
- Visual Studio Code (ou équivalent)
- ChatGPT (comme assistant d’analyse IA)

---

## Objectifs du projet

- Apprendre à utiliser ChatGPT pour :
  - Identifier et corriger des erreurs de code.
  - Générer automatiquement du code simple (boilerplate, tests, documentation).
  - Rédiger une documentation claire et lisible.
- Renforcer la capacité à **vérifier**, **tester** et **critiquer** les réponses fournies par l'IA.
- Se préparer aux enjeux réels de l'automatisation dans le développement logiciel.

---

## Fonctionnalités principales

### 1. Debugging

| Fichier                   | Description |
|--------------------------|-------------|
| `factorial.py`           | Corriger une boucle infinie dans le calcul de factorielle |
| `print_arguments.py`     | Corriger un script pour qu’il ignore le nom du fichier dans `argv` |
| `change_background.html` | Corriger une faute de frappe dans un `id` pour le JS |
| `mines.py`               | Corriger et ajouter une condition de victoire au jeu de démineur |
| `tic.py`                 | Corriger un jeu de morpion avec vérification d'entrée et détection de gagnant |

### 2. Documentation

| Fichier                     | Objectif |
|----------------------------|----------|
| `factorial_recursive.py`   | Ajouter une documentation structurée à la fonction factorielle |

### 3. Error Handling

| Fichier         | Objectif |
|----------------|----------|
| `checkbook.py` | Ajouter la gestion des erreurs utilisateurs (input non numérique) |

---

## Structure du projet

```bash
holbertonschool-chatgpt-introduction/
├── debugging/
│   ├── factorial.py
│   ├── print_arguments.py
│   ├── change_background.html
│   ├── mines.py
│   ├── tic.py
│   ├── factorial_recursive.py
│   └── checkbook.py
└── README.md
