#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from coffeedict.word import SearchWord


def main():
    sw = SearchWord('collins_learners', 'cooperation')
    visit = sw.visit_dict()

if __name__ == '__main__':
    main()