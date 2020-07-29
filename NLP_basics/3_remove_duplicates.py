#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: trendydice
"""

import nltk

x = "hello world says system and system says hello world"
print(x.split())
print(list(set(x.split())))