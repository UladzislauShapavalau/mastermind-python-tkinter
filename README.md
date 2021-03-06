**Shapavalau Uladzslau GL06**
https://github.com/UladzislauShapavalau/mastermind-python-tkinter

---
### Projekt z Języków Symbolicznych

###### Dokumentacja

# _Mastermind_
Gracz wpisuje "kod"(4 cyfry) składający się z liczb od 1 do 6 włącnie. Jego zadaniem będzie odgadnięcie tego kodu w skończonej liczbie prób (12 prób). Po każdej próbie gracz jest informowany jedynie ile z elementów, które wypróbował w danej kolejce znajduje się w ukrytym kodzie (wypisuje „O”) i ile z nich znajduje się już na swojej pozycji (wypisuje „X”). Zbierając informacje z listy w końcu dochodzi do ostatecznego rozwiązania. Jesli gracz z 12 prób nie odgadł kodu, wyświetla się napis "Przegrana!" i kod króry był zgenerowany. W przypadku zwycięstwa wyświetla się napis "Wygrana!". Także na początku każdej gry program wybiera losowe reguły. Przy niepoprawnych regułach program będzie wypisywać niepoprawne odpowiedzi. Jeśli gracz zauważy, że gra wypisuje dziwne podpowiedzi to on może to spwrawdzić wciskając przecisk "Oszust!". Jesli reguła gry będzie niepoprawna to wyświetla się napis "Złapałeś/łas mnie!". Jesli poprawna to "Tere fere" i kod króry był zgenerowany.

### Okno gry  zawiera:
- przycisk Sprawdż (Enter)
- przycisk Oszust
- przycisk Reset (Esc)
- okno z polem tekstowym (Tab)
- lista odpowiedzi

---

Klasy i funkcje zawarte w projekcie
---
### Klasa 
```
class RulesGame
```
Klasa programu, zawierająca funkcji logiki gry, restarta, sprawdzania reguł oraz rysowania okna.
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/game.py#L5)
### Klasa
```
TestProject
```
Klasa programu, zawierająca tesy. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L7)

### Funkcji
`main.py` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/main/main.py)

- Zawiera inicjalizacje modułu tkinter oraz głownego modułu programu `game`. 


`game.py` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/main/game.py)
zawiera
- `class RulesGame` [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/game.py#L5)
- `__init__` inicjalizacja zmiennych. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/8fc13622fe200e0a978b6a9360331b24f391898d/game.py#L7)
- `resetBtn` funkcja restartuje nową grę. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/8fc13622fe200e0a978b6a9360331b24f391898d/game.py#L23)
- `isScammer` sprawdzanie czy reguły gry są prawidłowe. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/8fc13622fe200e0a978b6a9360331b24f391898d/game.py#L34)
- `mainLogic` główna logika gry. Liczy i daje odpowiedzi czy gracz poprawnie podał liczby. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/8fc13622fe200e0a978b6a9360331b24f391898d/game.py#L45)
- `drawField` funkcja rysuje okno. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/8fc13622fe200e0a978b6a9360331b24f391898d/game.py#L81)

`functions.py` [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/functions.py) zawiera 
- `isTrueInput` sprawdza czy prawidłowo podane dane [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/functions.py#L5)
- `generateSample` generuje losowe liczby do odgadnięcia. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/functions.py#L21)
- `whatIsRule` program wybiera reguły gry. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/functions.py#L25)
- `createFakeFeedback` generuje niepoprawne odpowiedzi przy niepoprawnych regułach. [link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/functions.py#L29)

Testy
---
```test_0_checkIfNotGuessed``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L12)


Wpisuje odpowiedzi z błędymi cyframi.

```test_1_checkIfTwoNumbersAreCorrect``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L25)

Wpisywuje odpowiedzi z dwoma poprawnymi cyframi w złych miejscach.

```test_2_checkIfNumbersAreCorrect```
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L38)

Wpisuje odpowiedzi z poprawnymi cyframi w złych miejscach oraz dobrych miejscach.

```test_3_checkIfGuessed```
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L53)

Wpisuje poprawne odpowiedzi.

```test_4_checkIfValidInput``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L66)

Wpisuje niepoprawny kod - 1231231.

```test_5_checkIfValidInput``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L74)

Wpisuje niepoprawny kod - 8779.

```test_6_checkIfScammer``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L83)

Wciśnięcie przycisku "Oszust!" pry niepoprawnych zasadach gry.

```test_7_checkIfScammer```
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L94)

Wciśnięcie przycisku "Oszust!" pry poprawnych zasadach gry.

```test_8_checkReset``` 
[link](https://github.com/UladzislauShapavalau/mastermind-python-tkinter/blob/642f94584504ab2207eee4bf8f3404c3ed656404/test.py#L105)

Wpisanie 10 odpowiedzi z błędymi cyframi. Wciśnięcie "Reset". Wpisanie 5 odpowiedzi z błędymi cyframi. Sprawdzanie czy licznik tur resetuje po wciścnięciu "Reset".
