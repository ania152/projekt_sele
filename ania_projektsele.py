import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email = "seletest2020@op.pl"
name = "Anna"
surname = "Marchewka"
login = "seletest"
password = "Testowanie1?"
siedziba_poza_Polska = "Nie"
regon = "787824013"
nip = "085193224"
nazwa_podmiotu = "Podmiot testowy"
pkd = "5229C"
pkd_nazwa = "DZIAŁALNOŚĆ POZOSTAŁYCH AGENCJI TRANSPORTOWYCH"
city = "Katowice"
budynek = "12"
budynek = "1"
postcode = "40-006"
telefon = "0327573333"
fax = "0327573333"
data_rozp = "2019-01-01"


class LsiRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(' https://lsi-dev.slaskie.pl/#/login')
        self.driver.maximize_window()
        # Czekaj max 5 sekund na elementy
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_NIP(self):
        driver = self.driver
        login = driver.find_element_by_name("username").send_keys(login)
        password = driver.find_element_by_name("password").send_keys(password)
        signin = driver.find_element_by_id("btn-submit")
        signin.click()
        siedziba_poza_Polska = driver.find_element_by_id("nie_poza_pl").click()
        driver.find_element_by_id("regon").send_keys(regon)
        driver.find_element_by_id("nip").send_keys(nip)
        driver.find_element_by_id("nazwa").send_keys(nazwa_podmiotu)
        driver.find_element_by_id("pkd_kod").send_keys(pkd)
        driver.find_element_by_id("pkd").send_keys(pkd_nazwa)
        driver.find_element_by_id("button_lupa").click()
        sleep(5)
        select_city = driver.find_element_by_id("search.nazwa").send_keys(city)
        driver.FindElement(By.XPath("//div/button[@type='submit']")
        driver.FindElement(By.XPath("//div/button[@title="wybierz: Katowice [pow. Katowice / gmi. Katowice]"])
        driver.find_element_by_id("adr_budynek").send_keys(budynek)
        driver.find_element_by_id("adr_lokal").send_keys(lokal)
        driver.find_element_by_id("adr_kod").send_keys(postcode)
        driver.find_element_by_id("telefon").send_keys(telefon)
        driver.find_element_by_id("fax").send_keys(fax)
        driver.find_element_by_id("email").send_keys(email)
        data_rozp_select = driver.find_element_by_id("data_rozp"). send_keys(data_rozp)
        data_rozp_select.select_by_visible_text("12")
        forma_prawna_select = Select(driver.find_element_by_id("forma_prawna_id"))
        forma_prawna_select.select_by_visible_text("spółki z ograniczoną odpowiedzialnością - mikroprzedsiębiorstwo")
        forma_wlasnosci_select = Select(driver.find_element_by_id("forma_wlasnosci_id"))
        forma_wlasnosci_select.select_by_visible_text("Pozostałe krajowe jednostki prywatne")
        driver.find_element_by_id("osw_reprezentacja_podm").click()
        driver.FindElement(By.XPath("//button[contains(text(),'Zapisz i wyjdź')]”)
        errors = driver.find_elements_by_xpath('//div[@class=" alert alert-dismissible msg-animate ng-scope alert-danger"]/ol/li')
        assert len(errors) == 1
        error_text = errors[0].get_attribute('innerText')
        assert errors[0].is_displayed()
        assert "NIP jest niepoprawny. Skoryguj dane." in error_text
