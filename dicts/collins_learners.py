#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from dicts import Dictionary
from bs4 import BeautifulSoup


class CollinsLeaners(Dictionary):
    def __init__(self, word):
        super().__init__(word)

    def search_url(self):
        url = r'http://www.collinsdictionary.com/dictionary/american-cobuild-learners/%s'
        url = url % self.word
        return url

    def get_result_word(self, page_html):
        soup = BeautifulSoup(page_html)
        soup.prettify()

        # word = soup.find_all('h2', {'class': 'orth'})
        print(soup)