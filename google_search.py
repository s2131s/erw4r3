#!/usr/bin/env python3
"""
Google Search Automation Script
Otomatik olarak Google'da arama yapar
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def google_search(search_term="selam"):
    """
    Google'da arama yapar

    Args:
        search_term (str): Aranacak kelime (varsayılan: "selam")
    """
    print(f"Google'da '{search_term}' aranıyor...")

    # Chrome seçeneklerini ayarla
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Tarayıcıyı görünür yapmak için aşağıdaki satırı kaldır
    # chrome_options.add_argument("--headless")

    driver = None
    try:
        # WebDriver'ı başlat
        driver = webdriver.Chrome(options=chrome_options)

        # Google'a git
        print("Google açılıyor...")
        driver.get("https://www.google.com")

        # Arama kutusunu bul (Google'ın arama kutusu)
        wait = WebDriverWait(driver, 10)

        # Google'ın arama kutusunu farklı yöntemlerle bul
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
        except:
            search_box = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")

        print(f"Arama kutusu bulundu, '{search_term}' yazılıyor...")

        # Arama terimini yaz
        search_box.clear()
        search_box.send_keys(search_term)

        # Enter'a bas
        print("Enter tuşuna basılıyor...")
        search_box.send_keys(Keys.RETURN)

        # Sonuçların yüklenmesini bekle
        print("Arama sonuçları bekleniyor...")
        time.sleep(3)

        # Sayfa başlığını yazdır
        print(f"Sayfa başlığı: {driver.title}")
        print("Arama başarıyla tamamlandı!")

        # Kullanıcının sonuçları görmesi için biraz bekle
        print("\n5 saniye sonra tarayıcı kapanacak...")
        time.sleep(5)

    except Exception as e:
        print(f"Hata oluştu: {str(e)}")

    finally:
        # Tarayıcıyı kapat
        if driver:
            print("Tarayıcı kapatılıyor...")
            driver.quit()
        print("İşlem tamamlandı!")


if __name__ == "__main__":
    # Varsayılan olarak "selam" ara
    google_search("selam")

    # Farklı bir kelime aramak için:
    # google_search("Python programlama")
