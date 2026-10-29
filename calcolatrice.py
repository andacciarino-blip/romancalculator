"""Calcolatrice Romana — una calcolatrice che usa solo i numeri romani."""

import tkinter as tk

from romani import ErroreRomano, calcola, da_romano

SFONDO = "#2b1d14"
PIETRA = "#e8dcc4"
ORO = "#c9a227"
PORPORA = "#7a1f3d"
INCHIOSTRO = "#2b1d14"
FONT = ("Times New Roman", 20, "bold")

OPERATORI = ["+", "−", "×", "÷"]


class Calcolatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calcolatrice Romana")
        self.configure(bg=SFONDO, padx=14, pady=14)
        self.resizable(False, False)

        self.primo = ""      # primo operando
        self.operatore = ""  # operatore scelto
        self.corrente = ""   # numero in digitazione
        self.finito = False  # True subito dopo "="

        self.storia = tk.StringVar()
        self.schermo = tk.StringVar(value="")

        tk.Label(self, textvariable=self.storia, bg=PIETRA, fg="#6b5a45",
                 font=("Times New Roman", 13), anchor="e", padx=10
                 ).grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Label(self, textvariable=self.schermo, bg=PIETRA, fg=INCHIOSTRO,
                 font=("Times New Roman", 28, "bold"), anchor="e", padx=10,
                 width=16, height=1
                 ).grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(0, 12))

        layout = [
            [("M", "cifra"), ("D", "cifra"), ("C", "cifra"), ("÷", "op")],
            [("L", "cifra"), ("X", "cifra"), ("V", "cifra"), ("×", "op")],
            [("I", "cifra"), ("⌫", "canc"), ("AC", "azzera"), ("−", "op")],
            [("=", "uguale", 3), ("+", "op")],
        ]
        for r, riga in enumerate(layout, start=2):
            c = 0
            for voce in riga:
                testo, tipo = voce[0], voce[1]
                span = voce[2] if len(voce) > 2 else 1
                colore = {"cifra": PIETRA, "op": ORO, "uguale": PORPORA}.get(tipo, "#b8a888")
                testo_col = "white" if tipo == "uguale" else INCHIOSTRO
                b = tk.Button(self, text=testo, font=FONT, bg=colore, fg=testo_col,
                              activebackground=ORO, relief="flat", bd=0,
                              width=4, height=1, cursor="hand2",
                              command=lambda t=testo, k=tipo: self.premi(t, k))
                b.grid(row=r, column=c, columnspan=span, sticky="nsew", padx=3, pady=3)
                c += span

        self.bind("<Key>", self.tastiera)
        self.aggiorna()

    # --- logica dei tasti -------------------------------------------------
    def premi(self, testo, tipo):
        if tipo == "cifra":
            if self.finito:
                self.primo, self.operatore, self.finito = "", "", False
                self.storia.set("")
            if len(self.corrente) < 15:
                self.corrente += testo
        elif tipo == "op":
            self.scegli_operatore(testo)
        elif tipo == "uguale":
            self.uguale()
        elif tipo == "canc":
            self.corrente = self.corrente[:-1]
        elif tipo == "azzera":
            self.primo = self.operatore = self.corrente = ""
            self.finito = False
            self.storia.set("")
        self.aggiorna()

    def scegli_operatore(self, op):
        if self.finito:
            # si continua dal risultato, se è un numero vero
            risultato = self.schermo.get()
            self.finito = False
            try:
                da_romano(risultato)
            except ErroreRomano:
                return
            self.primo, self.corrente = risultato, ""
        elif self.corrente:
            if self.primo and self.operatore:
                if not self.esegui():
                    return
                self.primo, self.corrente = self.schermo.get(), ""
            else:
                try:
                    da_romano(self.corrente)
                except ErroreRomano as e:
                    self.errore(str(e))
                    return
                self.primo, self.corrente = self.corrente, ""
        elif not self.primo:
            return
        self.operatore = op
        self.storia.set(f"{self.primo} {op}")

    def uguale(self):
        if self.primo and self.operatore and self.corrente:
            self.storia.set(f"{self.primo} {self.operatore} {self.corrente} =")
            if self.esegui():
                self.finito = True

    def esegui(self):
        try:
            risultato = calcola(self.primo, self.operatore, self.corrente)
        except ErroreRomano as e:
            self.errore(str(e))
            return False
        except ZeroDivisionError:
            self.errore("Divisione impossibile")
            return False
        self.primo = self.operatore = ""
        self.corrente = ""
        self.schermo.set(risultato)
        return True

    def errore(self, messaggio):
        self.storia.set(messaggio)
        self.corrente = ""
        self.primo = self.operatore = ""
        self.finito = True
        self.schermo.set("ERRATVM")

    def aggiorna(self):
        if self.finito:
            return  # lo schermo mostra il risultato o l'errore
        if self.corrente:
            self.schermo.set(self.corrente)
        elif self.primo:
            self.schermo.set(self.primo)
        else:
            self.schermo.set("")

    def tastiera(self, evento):
        tasto = evento.char.upper()
        if tasto in "IVXLCDM" and tasto:
            self.premi(tasto, "cifra")
        elif tasto in ("+", "-", "*", "/") and tasto:
            self.premi({"-": "−", "*": "×", "/": "÷"}.get(tasto, tasto), "op")
        elif evento.keysym in ("Return", "KP_Enter") or tasto == "=":
            self.premi("=", "uguale")
        elif evento.keysym == "BackSpace":
            self.premi("⌫", "canc")
        elif evento.keysym == "Escape":
            self.premi("AC", "azzera")


if __name__ == "__main__":
    Calcolatrice().mainloop()
