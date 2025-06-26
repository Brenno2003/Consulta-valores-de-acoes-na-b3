from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def configuracao_web():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    return chrome_options

def acessar_web():
    configuracao = configuracao_web()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=configuracao)
    return driver

def pegar_perco(driver, acao):
    preco = None
    try:
        driver.get(f"https://br.tradingview.com/symbols/BMFBOVESPA-{acao}/?utm_campaign=hotlists&utm_medium=widget&utm_source=b3.com.br")
        wait = WebDriverWait(driver, 50)
        price_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".js-symbol-last span")))
        preco = price_element.text.strip()
    except Exception as erro:
        print(f"Erro ao acessar o site: {erro}")
    return preco