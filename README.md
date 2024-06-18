<h3 align="center">TAM-projekt-zaliczeniowy</h3>
<p align="center">Testy sklepu internetowego z użyciem selenium i pytest</p>


<details>
  <summary>Contents</summary>
  <ol>
    <li><a href="#About-project">About project</a>
      <ul>
        <li><a href="#Objective">Objective</a></li>
        <li><a href="#Used-technology">Used technology</a></li>
        <li><a href="#Requirements">Requirements</a></li>
        <li><a href="#Test-environment">Test environment</a></li>
      </ul>
    </li>
    <li><a href="#Test-scenario">Test scenario</a>
      <ul>
        <li><a href="#Zakup-produktu">Zakup produktu</a></li>
        <li><a href="#Rejestracja-i-logowanie">Rejestracja i logowanie</a></li>
      </ul>
    </li>
  </ol>
</details>

## About project
Kod pozwala przetestować przygotowane scenariusze zakupu produktu oraz logowania do konta.


### Objective:
Przetestowanie funkcji zakupu produktu i logowania na stronie e-commerce "[Luma](https://magento.softwaretestingboard.com/)".


### Used technology:
Python, pytest, Selenium, PyCharm


### Requirements:
<ul>
  <li>Python (v. 3.9) with modules and packages: </li>
  <ul>
    <li>time</li>
    <li>pytest (v. 8.2.2)</li>
    <li>selenium (v. 4.21.0)</li>
  </ul>
</ul>


### Test environment:
<ul>
  <li>
    PyCharm 2024.1.2 (Community Edition) <br>
    Build #PC-241.17011.127, built on May 28, 2024 <br>
    Runtime version: 17.0.11+1-b1207.24 amd64 <br>
    VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o. <br>
    Windows 10.0 <br>
    GC: G1 Young Generation, G1 Old Generation <br>
    Memory: 2048M <br>
    Cores: 12 <br>
  </li>
  <li>
    Chrome
  </li>
  <li>
    <a href="https://magento.softwaretestingboard.com/">Luma</a> - demo sklep, sesje resetowane co niedzielę 
  </li>
</ul>
 


## Test scenario

### Zakup produktu
<details>
  <summary>Wyszukanie produktu</summary>
<table>
  <tr>
    <th>Nazwa</th>
    <td>Wyszukanie produktu</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Wprowadzenie nazwy produktu do paska wyszkiwania <br>
      Zatwierdzenie wyszukiwania <br>
      Kliknięcie w nazwę na karcie produktu <br>
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>Na stronie sklepu: https://magento.softwaretestingboard.com/ </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>Nazwa produktu: "Rival Field Messenger"</td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>Strona produktu z nazwą produktu w tytule</td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>Test zakończony pomyślnie.</td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
</table>
</details>


<details>
  <summary>Zakup produktu</summary>
<table>
  <tr>
    <th>Nazwa</th>
    <td>Zakup produktu</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Kiknięcie w przycisk "Add to Cart" <br>
      Kliknięcie w ikonę koszyka <br>
      Klinięcie w przycisk "Proceed to Checkout" <br>
      Uzupełnienie pól: email, first name, last name, telephone poprawnymi danymi <br>
      Wybranie z listy country: Poland <br>
      Wybranie z listy region pierwszej poprawnej opcji <br>
      Uzupełnienie pól: city, postcode, street poprawnymi danymi <br>
      Kliknięcie w przycisk "Next" <br>
      Kliknięcie w przycisk "Place Order"
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>Na stronie produktu: https://magento.softwaretestingboard.com/rival-field-messenger.html </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      email = "user@email.not" <br>
      f_name = "User" <br>
      l_name = "Name" <br>
      street = "Street" <br>
      city = "City" <br>
      zip_code = "12-345" <br>
      country = "PL" <br>
      phone = "123456789"
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>Pojawi się informacja o zakupie produktu oraz numer zamówienia</td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>Test zakończony pomyślnie. Czas oczekiwania na załadowanie się pewnych elementów może się zmieniać.</td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
</table>
</details>


<details>
  <summary>Zakup produktu ze zniżką</summary>
<table>
  <tr>
    <th>Nazwa</th>
    <td>Zakup produktu ze zniżką</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Kiknięcie w przycisk "Add to Cart" <br>
      Kliknięcie w ikonę koszyka <br>
      Klinięcie w przycisk "Proceed to Checkout" <br>
      Uzupełnienie pól: email, first name, last name, telephone poprawnymi danymi <br>
      Wybranie z listy country: Poland <br>
      Wybranie z listy region pierwszej poprawnej opcji <br>
      Uzupełnienie pól: city, postcode, street poprawnymi danymi <br>
      Kliknięcie w przycisk "Next" <br>
      Rozwinięcie opcji dodania rabatu <br>
      Wpisanie rabatu <br>
      Kliknięcię przycisku "Apply Discount" <br>
      Kliknięcie w przycisk "Place Order" <br>
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>
      Na stronie produktu: https://magento.softwaretestingboard.com/rival-field-messenger.html <br>
      Włączony kod promocyjny
    </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      email = "user@email.not" <br>
      f_name = "User" <br>
      l_name = "Name" <br>
      street = "Street" <br>
      city = "City" <br>
      zip_code = "12-345" <br>
      country = "PL" <br>
      phone = "123456789" <br>
      discount_code = "20poff"
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>
      Po zatwierdzeniu kodu promocyjnego, koszt powinnien zostać obniżony o 20% ceny produktu <br>
      Pojawi się informacja o zakupie produktu oraz numer zamówienia
    </td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>
      Test zakończony pomyślnie. 
      Czas oczekiwania na załadowanie się pewnych elementów może się zmieniać.
    </td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
</table>
</details>


### Rejestracja i logowanie
<details>
  <summary>Rejestracja istniejącego konta</summary>
  <table>
  <tr>
    <th>Nazwa</th>
    <td>Rejestracja isniejącego konta użytkownika</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Kliknięcie przycisku "Create an Account" <br>
      Uzupełnienie pól: first name, last name, email, password, password confirmation <br>
      Kliknięcie w przycisk "Create Account" 
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>
      Na stronie produktu: https://magento.softwaretestingboard.com/rival-field-messenger.html <br>
      Utworzone konto na dane testowe
    </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      email = "user@email.not" <br>
      f_name = "User" <br>
      l_name = "Name" <br>
      password = "Password1234"
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>
      Po próbie stworzenia konta na zarejestowane już dane, 
      powinien pojawić się komunikat o istniejącym już koncie
    </td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>
      Test zakończony pomyślnie. <br>
      Przez charakter środowiska demo, pierwsze uruchomienie testu po resecie strony (co niedzielę), 
      może zakończyć się niepowodzeniem. W takim wypadku należy ponownie uruchomić test.
    </td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
  </table>
</details>



<details>
  <summary>Logowanie</summary>
  <table>
  <tr>
    <th>Nazwa</th>
    <td>Logowanie do konta użytkownika</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Kliknięcie przycisku "Sign In" <br>
      Uzupełnienie pól: email, password <br>
      Kliknięcie w przycisk "Sign In" 
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>
      Na stronie produktu: https://magento.softwaretestingboard.com/rival-field-messenger.html <br>
      Utworzone konto na dane testowe
    </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      email = "user@email.not" <br>
      password = "Password1234"
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>
      Po zalogowaniu powinno pokazać się menu użytkownika, 
      które pozwala przejść na konto użytkownika lub wylogować się.
    </td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>
      Test zakończony pomyślnie.
    </td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
  </table>
</details>


<details>
  <summary>Logowanie z błędnym hasłem</summary>
  <table>
  <tr>
    <th>Nazwa</th>
    <td>Logowanie do konta użytkownika z nieprawidłowym hasłem</td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
      Kliknięcie przycisku "Sign In" <br>
      Uzupełnienie pól: email, password <br>
      Kliknięcie w przycisk "Sign In" 
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td>
      Na stronie produktu: https://magento.softwaretestingboard.com/rival-field-messenger.html <br>
      Utworzone konto na poprawne dane testowe
    </td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      email = "user@email.not" <br>
      invalid_password = "InvalidPassword"
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td>Ważny</td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td>
      Po próbie zalogowania się powinien pokazać się alert informujący o błędnych danych logowania.
    </td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td>
      Test zakończony pomyślnie.
    </td>
  </tr>
  <tr>
    <th>Tester</th>
    <td>Jakub</td>
  </tr>
  </table>
</details>
