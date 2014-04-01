# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re

def clean_float(v):
    v = v.replace(',','.')
    v = v.replace('?','')
    v = v.replace("π",'3.14')

    non_decimal = re.compile(r'[a-z]')
    v = non_decimal.sub('', v)

    try :
        v = float(v)
    except :
        return np.nan

    return v

def clean_int(v):
    v = v.replace(',','.')
    v = v.replace('?','')
    non_decimal = re.compile(r'[a-z]|[A-Z]|\'|\.')
    v = non_decimal.sub('', v)
    try :
        return int(v)
    except :
        return np.nan

def clean_string(v):
    return str(v).upper()

def clean_bool(v):
    v = v.upper()
    if re.match('YES|YEP',v):
        return True
    if re.match('NO',v):
        return False
    return np.nan
