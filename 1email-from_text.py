#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: jhhalls
"""

import re
text = "Please contact us at contact@tutorialspoint.com for further information."+\
        " You can also give feedbacl at feedback@tp.com"


emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)
