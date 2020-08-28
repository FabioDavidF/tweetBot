from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys
from datetime import datetime
def leiaInt(txt):
    """Lê um input baseado no texto fornecido e valida se o mesmo é inteiro.
     Enquanto não for continuará pedindo input
     Retorna o valor n, inteiro"""
    while True:
        n = input(txt)
        try:
            n = int(n)
        except:
            print('\033[01;31mERROR!Please type in an integer*\033[m')
        else:
            break
    return n

tweet = str(input('Type here what you want the bot to tweet: '))

class TwitterBot():
    def __init__(self,username,password):
        self.browser = Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.twitter.com/login")
        sleep(5)
        usernameInput = self.browser.find_element_by_name("session[username_or_email]")
        passwordInput = self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(5)

    def Tweetar(self):
        ano = datetime.now().year
        mes = datetime.now().month
        dia = datetime.now().day
        hora = datetime.now().hour
        minuto = datetime.now().minute
        segundo = datetime.now().second
        tweet = self.browser.find_element_by_xpath('''//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div
                                                      /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div
                                                      /div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div
                                                      /div/div/div''')
        tweet.send_keys(f'''{tweet}''')
        botao = self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div
        /div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span''')
        botao.click()


if __name__ == "__main__":
    username= input("Twitter login: ")
    password= input("Twitter password: ")
    t = TwitterBot(username,password)
    t.signIn()
    h = leiaInt('For how many hours do you want to tweet?')
    freq = leiaInt('With what frequency?(IN SECONDS)')

    for c in range(0, h):
        t.Tweetar()
        sleep(freq)
