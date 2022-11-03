from bs4 import BeautifulSoup   
import requests


class Scrapper:

    @staticmethod
    def scrap():

        url = "https://ru.ufrj.br/index.php/2014-07-24-00-55-59"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        div = soup.find("div",itemprop="articleBody")
        lista = div.find_all("a")


        url_spreadshet = lista[2]['href']
        html_SS = requests.get(url_spreadshet)
        soup_SS = BeautifulSoup(html_SS.text, 'html.parser')
        alimentos = soup_SS.find_all("td", class_="s3")
        comidinhas = []
        for i in alimentos:
            comidinhas.append(" ".join(i.text.split())) 
        return comidinhas