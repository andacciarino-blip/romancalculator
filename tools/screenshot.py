import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from PIL import ImageGrab
from calcolatrice import Calcolatrice

app = Calcolatrice()
for t in "XII":
    app.premi(t, "cifra")
app.premi("+", "op")
for t in "XXX":
    app.premi(t, "cifra")
app.premi("=", "uguale")

def scatta():
    app.update()
    x, y = app.winfo_rootx(), app.winfo_rooty()
    w, h = app.winfo_width(), app.winfo_height()
    ImageGrab.grab((x, y, x + w, y + h)).save("anteprima.png")
    app.destroy()

app.lift(); app.attributes("-topmost", True)
app.after(1500, scatta)
app.mainloop()
