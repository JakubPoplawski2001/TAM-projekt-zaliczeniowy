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
      </ul>
    </li>
    <li><a href="#Test-scenario">Test scenario</a>
      <ul>
        <li><a href="#Zakup produktu">Zakup produktu</a></li>
        <li><a href="#2.Test">2.Test</a></li>
      </ul>
    </li>
    <li><a href="#Results">Results</a></li>
  </ol>
</details>

## About project
Kod pozwala przetestować przygotowane scenariusze


### Objective:
Przetestowanie ... na stronie e-commerce "[Luma](https://magento.softwaretestingboard.com/)".


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
    <td></td>
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
    <td></td>
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
      ...
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td></td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td>
      ... dane użytkownika
      Kod promocyjny: "20poff"<br>
    </td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td></td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td></td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td></td>
  </tr>
  <tr>
    <th>Tester</th>
    <td></td>
  </tr>
</table>
</details>


### 2. Test
<details>
  <summary>Contents</summary>

</details>
<table>
  <tr>
    <th>Nazwa</th>
    <td></td>
  </tr>
  <tr>
    <th>Opis czynności</th>
    <td>
Włożenie karty<br>
Podaj PIN<br>
Klawisz 1<br>
Klawisz 2<br>
Klawisz 3<br>
Klawisz 4<br>
Klawisz POTWIERDŹ<br>
Klawisz Prawy 1<br>
Wybierz kwotę<br>
Klawisz Prawy 3<br>
Wypłać 1000<br>
Czy chcesz wydruk?<br>
Klawisz Lewy 1<br>
Wydanie karty<br>
Karta odebrana<br>
Wydanie pieniędzy – 1000<br>
Pieniądze odebrane<br>
Wydruk<br>
    </td>
  </tr>
  <tr>
    <th>Warunki wstępne</th>
    <td></td>
  </tr>
  <tr>
    <th>Dane testowe</th>
    <td></td>
  </tr>
  <tr>
    <th>Priorytet</th>
    <td></td>
  </tr>
  <tr>
    <th>Oczekiwany rezultat</th>
    <td></td>
  </tr>
  <tr>
    <th>Komentarz</th>
    <td></td>
  </tr>
  <tr>
    <th>Tester</th>
    <td></td>
  </tr>
</table>


## Results

