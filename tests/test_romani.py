import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import pytest
from romani import a_romano, da_romano, calcola, ErroreRomano

def test_andata_e_ritorno():
    for n in range(1, 4000):
        assert da_romano(a_romano(n)) == n

@pytest.mark.parametrize("n,r", [(4,"IV"),(9,"IX"),(14,"XIV"),(1994,"MCMXCIV"),(2026,"MMXXVI"),(3999,"MMMCMXCIX")])
def test_noti(n, r):
    assert a_romano(n) == r

@pytest.mark.parametrize("s", ["IIII","VV","IC","XM","MMMM","","ABC","IL"])
def test_non_validi(s):
    with pytest.raises(ErroreRomano):
        da_romano(s)

def test_operazioni():
    assert calcola("XII", "+", "XXX") == "XLII"
    assert calcola("L", "−", "VIII") == "XLII"
    assert calcola("VI", "×", "VII") == "XLII"
    assert calcola("LXXXIV", "÷", "II") == "XLII"
    assert calcola("X", "÷", "III") == "III resto I"
    assert calcola("V", "−", "V") == "NVLLA"

def test_limiti():
    with pytest.raises(ErroreRomano):
        calcola("V", "−", "X")
    with pytest.raises(ErroreRomano):
        calcola("MM", "×", "II")
