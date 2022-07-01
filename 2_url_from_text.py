#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jhalls
"""

import re
 
with open("path\url_example.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print (urls)
