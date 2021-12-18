import time
import urllib.request
import requests
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import re
import pandas as pd


def get_url(codigo):
    return f"https://www.dlkmodas.com.br/produto/{codigo}"


def get_modelo(codigo):
    url = f"https://www.dlkmodas.com.br/produto/{codigo}"
    page_raw = urllib.request.urlopen(url)
    soup = bs(page_raw, "html.parser")
    modelo_raw = soup.body.findAll("h1")
    t = re.split(r'(?s)(?<=>)(.+?)(?=</h1>)', str(modelo_raw))
    modelo = t[1]
    return modelo.title()


def get_valor(codigo):
    url = f"https://www.dlkmodas.com.br/produto/{codigo}"
    page_raw = urllib.request.urlopen(url)
    soup = bs(page_raw, "html.parser")
    valor_raw = soup.find_all("span", {"class": "fbits-boleto-preco"})
    t = re.split(r'(?s)(?<=>)(.+?)(?=</span>)', str(valor_raw))
    # remove 'R$ ' do valor
    valor = t[1][3:]
    # substitui vígula por ponto
    valor = valor.replace(',', '.')
    return valor


def get_disponivel(codigo):
    pass

