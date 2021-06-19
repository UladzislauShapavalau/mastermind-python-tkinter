**Shapavalau Uladzslau GL06**

---

# _Mastermind_
Gracz wpisuje "kod"(4 cyfry) składający się z liczb od 1 do 6 włącnie. Jego zadaniem będzie odgadnięcie tego kodu w skończonej liczbie prób (12 prób). Po każdej próbie gracz jest informowany jedynie ile z elementów, które wypróbował w danej kolejce znajduje się w ukrytym kodzie (wypisuje „O”) i ile z nich znajduje się już na swojej pozycji (wypisuje „X”). Zbierając informacje z listy w końcu dochodzi do ostatecznego rozwiązania. Jesli gracz z 12 prób nie odgadł kodu, wyświetla się napis "Przegrana!" i kod króry był zgenerowany. W przypadku zwycięstwa wyświetla się napis "Wygrana!". Także na początku każdej gry program wybiera losowe reguły. Przy niepoprawnych regułach program będzie wypisywać niepoprawne odpowiedzi. Jeśli gracz zauważy, że gra wypisuje dziwne podpowiedzi to on może to spwrawdzić wciskając przecisk "Oszust!". Jesli reguła gry będzie niepoprawna to wyświetla się napis "Złapałeś/łas mnie!". Jesli poprawna to "Tere fere" i kod króry był zgenerowany.

### Okno gry  zawiera:
- przycisk Sprawdż (Enter)
- przycisk Oszust
- przycisk Reset (Esc)
- okno z polem tekstowym (Tab)
- lista odpowiedzi

---

Klasy i funkcje głowne zawarte w projekcie
---
### Klasa 
```
class RulesGame
```
Klasa programu, zawierająca funkcji logiki gry, restarta, sprawdzania reguł oraz rysowania okna.

### Klasa
```
TestProject
```
Klasa programu, zawierająca tesy.

### Funkcji
`main` zawiera inicjalizacje modułu tkinter oraz głownego modułu programu `game`. 

`game` zawiera głowny algorym gry i tworzy okno. 

`functions` zawiera `isTrueInput` króra sprawdza czy prawidłowo podane dane. `generateSample` generuje losowe liczby do odgadnięcia. W funkcjii `whatIsRule` program wybiera reguły gry. `createFakeFeedback` generuje niepoprawne odpowiedzi przy niepoprawnej regułe. 

Testy
---
```test_0_checkIfNotGuessed``` - Wpisuje odpowiedzi z błędymi cyframi.

```test_1_checkIfTwoNumbersAreCorrect``` - Wpisywuje odpowiedzi z dwoma poprawnymi cyframi w złych miejscach.

```test_2_checkIfNumbersAreCorrect``` - Wpisuje odpowiedzi z poprawnymi cyframi w złych miejscach oraz dobrych miejscach.

```test_3_checkIfGuessed``` - Wpisuje poprawne odpowiedzi.

```test_4_checkIfValidInput``` - Wpisuje niepoprawny kod - 1231231.

```test_5_checkIfValidInput``` - Wpisuje niepoprawny kod - 8779.

```test_6_checkIfScammer``` - Wciśnięcie przycisku "Oszust!" pry niepoprawnych zasadach gry.

```test_7_checkIfScammer``` - Wciśnięcie przycisku "Oszust!" pry poprawnych zasadach gry.

```test_8_checkReset``` - Wpisanie 10 odpowiedzi z błędymi cyframi. Wciśnięcie "Reset". Wpisanie 5 odpowiedzi z błędymi cyframi. Sprawdzanie czy licznik tur resetuje po wciścnięciu "Reset".
