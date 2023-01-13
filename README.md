# conso-score-back-office

Ce répertoire contient le code du backend de l'application conso_score

## Requirements

Python 3.10.5 ou ultérieur
Docker

## Option 1 : Setup le serveur seul

1. Installer les dépendances du projet :
   Se placer à la racine du répertoire

```bash
    pip install -r requirements.txt
```

2. Lancer le projet avec la commande :

```bash
    python conso_score_back.py
```

3. Le serveur Flask est lancé sur le port 5000 par défaut

## Option 2 : Lancer le backend via un contener Docker

Le projet a été dockerisé.
Une fois docker installé, voici la liste des actions à effectuer afin de déployer le backend :

1. Créer un répertoire parent appelé conso-score
2. Se placer dans ce répertoire et effectuer les commandes suivantes (le backend est constitué de deux webservices) :

```bash
git clone https://github.com/FloRichard/conso-score-back-office
git clone https://github.com/FloRichard/conso-score-user-manager
```

3. Descendre dans le répertoire conso-score-back-office avec la commande :

```bash
cd conso-score-back-office
```

4. Lancer le contener Docker avec la commande :

```bash
docker compose up --build --force-recreate
```

5. Le backend est maintenant accessible sur le port 9092

Vous pouvez tester son bon fonctionnement en allant consulter l'url :

http://**[votre ip]**:9092/datas/transport

## Documentation

Toutes les routes sont documentées via un swagger qui se trouve ici : `/doc/conso-score-back-office.yaml`

Ouvrez [swagger editor](https://editor.swagger.io/) et copiez-collez le contenu du fichier.
