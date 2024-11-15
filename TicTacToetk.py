import tkinter as tk
from tkinter import messagebox

# Spielfeld initialisieren
spielfeld = [[' ' for _ in range(3)] for _ in range(3)]

# Funktion zum Zeichnen des Spielfelds
def zeichne_spielfeld():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=spielfeld[i][j])

# Funktion zur Überprüfung, ob das Spielfeld voll ist
def spielfeld_voll():
    for reihe in spielfeld:
        if ' ' in reihe:
            return False
    return True

# Funktion zur Überprüfung, ob ein Spieler gewonnen hat
def gewinner(spieler):
    # Überprüfen der Reihen
    for reihe in spielfeld:
        if reihe == [spieler, spieler, spieler]:
            return True
    
    # Überprüfen der Spalten
    for spalte in range(3):
        if [spielfeld[0][spalte], spielfeld[1][spalte], spielfeld[2][spalte]] == [spieler, spieler, spieler]:
            return True

    # Überprüfen der Diagonalen
    if [spielfeld[0][0], spielfeld[1][1], spielfeld[2][2]] == [spieler, spieler, spieler]:
        return True
    
    if [spielfeld[0][2], spielfeld[1][1], spielfeld[2][0]] == [spieler, spieler, spieler]:
        return True

    return False

# Funktion, die aufgerufen wird, wenn ein Spieler ein Feld auswählt
def feld_geklickt(i, j):
    global aktueller_spieler

    # Überprüfen, ob das Feld bereits belegt ist
    if spielfeld[i][j] == ' ':
        spielfeld[i][j] = aktueller_spieler
        zeichne_spielfeld()

        # Überprüfen, ob der aktuelle Spieler gewonnen hat
        if gewinner(aktueller_spieler):
            messagebox.showinfo("Spielende", f"Spieler {aktueller_spieler} GEWINNT!!!")
            fenster.quit()

        # Überprüfen, ob das Spielfeld voll ist
        elif spielfeld_voll():
            messagebox.showinfo("Spielende", "Das Spielfeld ist voll. Untenschieden!!!")
            fenster.quit()

        # Spieler wechseln
        aktueller_spieler = 'O' if aktueller_spieler == 'X' else 'X'

# Hauptspielfunktion
def starte_spiel():
    global aktueller_spieler
    aktueller_spieler = 'X'
    zeichne_spielfeld()

# Fenster erstellen
fenster = tk.Tk()
fenster.title("Tic-Tac-Toe")

# Buttons für das Spielfeld erstellen
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(fenster, text=" ", font=('Arial', 40), width=5, height=2, 
                                  command=lambda i=i, j=j: feld_geklickt(i, j))
        buttons[i][j].grid(row=i, column=j)

# Spiel starten
starte_spiel()

# Fenster anzeigen
fenster.mainloop()
