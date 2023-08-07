# Projet_6

Projet : Classification d'Images de Chiens par Races Utilisant le Deep Learning

Dans ma quête pour donner en retour à l'association de protection des animaux de mon quartier, où j'ai trouvé mon fidèle compagnon, Snooky, j'ai abordé un défi majeur en intelligence artificielle : classer les images de chiens selon leur race. Voici les principaux éléments du projet :

Contexte et Problème : L'association possède une collection croissante d'images de chiens, et le référencement manuel de ces images par race est devenu une tâche ardue. J'ai pris l'engagement de développer un algorithme capable d'automatiser ce processus.

Préparation des Données : Le Stanford Dogs Dataset a servi de base pour l'entraînement. J'ai prétraité les images en utilisant diverses techniques, comme le whitening, l'equalization, et la modification de taille, et j'ai enrichi le jeu de données avec la data augmentation.

Approche de Modélisation : Deux approches ont été explorées :

Réseau CNN Propre : J'ai conçu un réseau de neurones convolutionnels (CNN) en m'inspirant de modèles existants, avec une optimisation approfondie des hyperparamètres.
Transfer Learning : J'ai également adapté un modèle pré-entraîné, en réentrainant les dernières couches et en modifiant la structure pour répondre à mon problème spécifique.
Comparaison : Ces deux approches ont été comparées en termes de temps de traitement et de performances, apportant une compréhension profonde des mérites et des défis de chaque méthode.

Ressources de Calcul : Étant conscient de la demande élevée en ressources pour l'entraînement de CNN, j'ai exploré des solutions comme l'utilisation de GPU ou le cloud computing (comme AWS) pour surmonter les limitations de l'ordinateur de l'association.

Livrables : J'ai fourni un notebook Python illustrant ma démarche, un programme capable de prédire la race d'un chien à partir d'une image, et un support de présentation pour le déploiement en production.

Compétences Évaluées et Acquises :

Évaluation et optimisation des performances des modèles de Deep Learning.
Sélection et mise en place de modèles de CNN adaptés à une problématique réelle.
Adaptation des paramètres et transformation des variables pour l'amélioration du modèle.
Gestion des ressources de calcul pour le Deep Learning.
Réflexion : Ce projet était plus qu'un simple exercice technique ; c'était une opportunité de contribuer à une cause qui me tient à cœur. Les compétences et l'expertise acquises dans la classification d'images par Deep Learning ont des applications larges et m'ont fourni une base solide pour de futurs projets en intelligence artificielle.

Ce projet illustre comment la technologie de pointe peut être utilisée pour résoudre des problèmes réels dans un contexte communautaire, en combinant la passion pour les animaux avec l'expertise en Deep Learning. Cela a été une expérience d'apprentissage enrichissante et gratifiante.
