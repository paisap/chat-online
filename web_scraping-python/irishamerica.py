#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import json

def get_images(obj_soup):
    """ obtener todas las imagenes """
    images = [img['src'] for img in obj_soup.find_all('img')]
    return images


def get_articles(obj_soup):
    """ Obtiene todos los links de los articulos """
    articles = []
    for link in obj_soup.find_all('a'):
        if 'y=' in link['href']:
            articles.append(link['href'])
    return articles


def get_title(obj_soup, id_title):
    """ Obitiene el titulo con el id especifico """
    title = obj_soup.find('h2', id=id_title).text
    return title

def get_pie_imagen(obj_soup):
    """ Obtiene todos los pie de las imagenes en orden """
    texto = [pie.text for pie in obj_soup('div', {'class': 'ccfic'})]
    return texto


def get_intro_noticia(obj_soup):
    """ Obtiene todas las noticias que se ven """
    list_news = [pie.find('p').text for pie in obj_soup('div', {'class': 'blog-entry'})]
    return list_news

def tags_with_links(obj_soup):
    """ obtiene los nombes y links y los devuelve en un json"""
    all_tags = {}
    count = 0
    for obj in obj_soup('div', {'class': 'post-tags'}):
        tags = {}
        for i in obj.find_all('a'):
            tags[i.text ] = i['href']
        all_tags[count] = tags
        count += 1
    return all_tags

def links_to_news(obj_soup):
    """ obtiene todos los links a las noticias """
    articles = []
    for link in obj_soup('div', {'class': 'blog-entry'}):
        for i in link.find_all('a'):
            articles.append(i['href'])
            break
    return articles


req = Request('https://irishamerica.com/category/blog/', headers={'User-Agent': 'Mozilla/5.0'})
irish = urlopen(req).read().decode("utf-8")
soup = BeautifulSoup(irish, "html.parser")
start_body = irish.find('<body ')
end_body = irish.find('</body>')
images = get_images(soup)
articles = get_articles(soup)
title = get_title(soup, "post-51484")
pies_imagen = get_pie_imagen(soup)
news = get_intro_noticia(soup)
t = tags_with_links(soup)
links_news = links_to_news(soup)



jsonOBJ = {
    "Noticia 1": {
        "title":  title,
        "imagen": images[1],
        "pie de imagen": pies_imagen[0],
        "intro noticia": news[0],
        "tags con link": t[0],
        "link noticia": links_news[0]
    },
    "Noticia 2": {
        "title": get_title(soup, "post-51423"),
        "imagen": images[2],
        "pie de imagen": pies_imagen[1],
        "intro noticia": news[1],
        "tags con link": t[1],
        "link noticia": links_news[1]
    },
    "links todos los articulos": articles
}
print(json.dumps(jsonOBJ, indent = 4))