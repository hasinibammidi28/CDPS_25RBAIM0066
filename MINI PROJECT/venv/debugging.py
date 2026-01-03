# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 06:21:25 2025

@author: ramus
"""

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("debugging_log.log"),
        logging.StreamHandler()   # THIS shows logs in terminal
    ]
)

def get_logger(name):
    return logging.getLogger(name)
