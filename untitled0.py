# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:37:41 2020

@author: paula
"""
import random
banks = ["Banco Mil","Banco Ave","Banco Caxa","Banco Lolo","Banco Wal","Banco Dil"]
companies = ["Company Orro","Company Gato","Company Willano","Company Blumen","Company Caxao","Company Omega","Company Waxin","Company Bim"]

banks_banks = [("Company Orro","Company Willano"),
               ("Company Orro","Company Omega"),
               ("Company Orro","Company Caxao"),
               ("Company Gato","Company Waxin"),
               ("Company Orro","Company Omega"),
               ("Company Bim","Company Orro"),
               ("Company Orro","Company Willano"),
               ("Company Orro","Company Caxao"),
               ("Company Omega","Company Gato"),
               ("Company Omega","Company Gato")]
companies_banks = []
for company in companies:
    companies_banks.append((company, random.choice(banks)))