# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 06:21:41 2025

@author: ramus
"""

from debugging_log.log import get_logger

logger = get_logger(__name__)

def get_movies():
    logger.info("Fetching movies")
    movies = ["Inception", "Interstellar", "Avatar"]
    return movies
