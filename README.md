# Calcolatrice Romana 🏛️

Una calcolatrice che lavora **solo con i numeri romani**: niente 0–9, solo I, V, X, L, C, D, M.

```
XII + XXX = XLII
LXXXIV ÷ II = XLII
X ÷ III = III resto I
```

## Scaricare l'eseguibile

Vai su **Releases** (colonna a destra del repository) e scarica il file per il tuo sistema:

| Sistema | File |
|---|---|
| Windows | `CalcolatriceRomana-Windows.exe` |
| macOS | `CalcolatriceRomana-macOS.zip` (estrai e apri l'app; al primo avvio: tasto destro → Apri) |
| Linux | `CalcolatriceRomana-Linux` (`chmod +x` e avvia) |

Windows potrebbe mostrare l'avviso SmartScreen perché l'eseguibile non è firmato: *Ulteriori informazioni → Esegui comunque*.

## Come si usa

- Componi i numeri con i tasti I V X L C D M (o con la tastiera).
- Operazioni: `+` `−` `×` `÷`, poi `=` o Invio.
- `⌫` cancella l'ultima cifra, `AC` (o Esc) azzera tutto.
- Si può continuare a calcolare partendo dal risultato.

### Regole romane
- Intervallo valido: da **I** (1) a **MMMCMXCIX** (3999).
- Solo numeri scritti correttamente: `IV` sì, `IIII` no.
- Lo zero non esisteva: un risultato nullo appare come **NVLLA**.
- Niente negativi né decimali: la divisione dà quoziente e resto.

## Eseguire dal codice

Serve Python 3 con Tkinter (incluso nelle installazioni standard):

```bash
python calcolatrice.py
```

Test: `pip install pytest && pytest`

## Come vengono creati gli eseguibili

Il workflow `.github/workflows/build.yml` compila automaticamente l'app con PyInstaller per Windows, macOS e Linux a ogni push su `main` e pubblica una nuova Release con gli eseguibili. Si può anche avviare a mano da *Actions → Compila eseguibili → Run workflow*.

```bash
git tag v1.0.0
git push origin v1.0.0
```
