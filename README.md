# To-Do List CLI App mit Python & SQLite

Dieses Projekt ist eine Kommandozeilen-Anwendung (CLI), die es dem Benutzer ermöglicht, seine täglichen Aufgaben zu verwalten. Die Aufgaben werden in einer SQLite-Datenbank gespeichert.
Das Projekt demonstriert grundlegende Python-Kenntnisse, modulare Programmierung und den Umgang mit Datenbanken.

---

## Funktionen
- Aufgaben hinzufügen, anzeigen, bearbeiten und löschen (CRUD)
- Speicherung der Aufgaben in SQLite
- Modularer Aufbau: separate Dateien für Datenbank (db.py), Aufgabenlogik, (task.py) und CLI
- (cli.py)
- Einfache Bedienung über die Kommandozeile
---

## Projektstruktur

```
.
 
├── main.py     # Einstiegspunkt der Anwendung
├── cli.py      # Kommandozeilen-Interface
├── task.py     # Logik zur Aufgabenverwaltung
├── db.py       # Verwaltung der SQLite-Datenbank
└── README.md   # Project documentation

```

---

## Installation & Ausführung

1. **Repository klonen**

```bash
git clone https://github.com/GhazalNorouzi/todolist-cli-python.git
cd todolist-cli-python
```

2. **Abhängigkeiten installieren**
   
```bash
pip install -r requirements.txt
```

3. **Anwendung starten**
   
```bash
python main.py
```

**Beispielhafte Nutzung:**

```text
> python main.py
1. Aufgabe hinzufügen
2. Aufgaben anzeigen
3. Aufgabe bearbeiten
4. Aufgabe löschen
```


## Fähigkeiten


Python Grundlagen & OOP

SQLite Datenbank & CRUD Operationen

Modularer Codeaufbau

CLI-Anwendungen




## Zukünftige Verbesserungen (optional)

Unit-Tests und Integrationstests hinzufügen

REST API für Web-Zugriff implementieren

Benutzer-Authentifizierung und Multi-User-Funktionalität
