# from selenium import webdriver  ##importujemy webdrivera z selenium
# import pytest  ##importujemy bibliotekę pytest
# from selenium.webdriver.common.by import By  ##importujemy By do lokalizowania elementów
#
#
# @pytest.fixture()  # tworzymy fiksturę z pytest, która pomaga nam wyciągnąć do ustawień początkowych i końcowych powtarzajace się kroki/czynnosci
# def setup_and_teardown():  # definiujemy kroki poczatkowe (setup) przed testem oraz te, które mają się wykonywac po kazdym tescie (teardown)
#     global driver  # ustawiamy driver globalnie
#     driver = webdriver.Chrome()  # definiujemy przeglądarkę za pomocą selenium
#     driver.maximize_window()  # maksymalizujemy okno
#     driver.get("https://tutorialsninja.com/demo/")  # wchodzimy w link konkretnej strony
#     yield  # oddzielamy ustawienia początkowe od koncowych - jest to miejsce gdzie bedzie wykonywany test
#     driver.quit()  # zamykamy karty
#
#
# def test_search_for_product(setup_and_teardown):  # definiujemy pierwszy test
#
#     driver.find_element(By.NAME, "search").send_keys(
#         "hp")  # szukamy na otwartej stronie do której dostalismy sie z setup elementu wyszukanego po nazwie i wpisujemy tam slowo HP
#     driver.find_element(By.XPATH,
#                         "//button[contains(@class,'btn-default')]").click()  # wyszukujemy tym razem po xpath lupke i klikamy w nią
#     assert driver.find_element(By.LINK_TEXT,
#                                'HP LP3065').is_displayed()  # sprawdzamy czy wyswietyla nam sie pozycja, ktorą wyszukalismy po Link_text
#     driver.quit()  # zamykamy
#
#
# def test_search_for_invalid_product(setup_and_teardown):  # definiujemy test 2
#
#     driver.find_element(By.NAME, "search").send_keys(
#         'Mercedes')  # wyszukujemy to samo pole co w tescie 1 tylko wpisujemy haslo Mercedes
#     driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()  # wyszukujemy i klikamy w lupke
#     # poniewaz jak zrobimy to na rzeczywistej stronie to wyswietli nam sie kounikat ponizszy tekst, chcemy zbadac czy rzeczywiscie ten tekst jest wyswietlany
#     expected_text = "There is no product that matches the search criteria."  # ustalamy sobie zmienną tekstu jaki oczekujemy po napisaniu Mercedes w polu search box
#     assert driver.find_element(By.XPATH, "//input[@ID='button-search']/following-sibling::p").text.__eq__(
#         expected_text)  # sprawdzamy  czy tekst, ktory wyswietlił sie po wpisaniu słowa Mercedes jest taki sam jak zdefiniowany przez nas wyżej expected_text
#     driver.quit()
