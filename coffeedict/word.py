#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import requests
from dicts.collins_learners import CollinsLeaners


class SearchWord:
    def __init__(self, dict_name, search_word):
        self.dict_name = dict_name
        self.search_word = search_word
        self.search_dict = None

    def _load_dict(self):
        if self.dict_name == 'collins_learners':
            self.search_dict = CollinsLeaners(self.search_word)
        return None

    def _get_result_page(self):
        url = self.search_dict.search_url()
        r = requests.get(url)
        page_html = r.text
        return page_html

    def visit_dict(self):
        self._load_dict()
        page_html = self._get_result_page()
        result_word = self.search_dict.get_result_word(page_html)
        return result_word


