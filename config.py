#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) TRTECHGUIDE

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION","BQA4pXQqbaMgB4fVWoqa0OHV_rHQug3pxe8zYdqrVTEfZDzNDb-7V1dyAc2ZwM0D9eANPRmEmbHqDW0R12z6FyxDvN_MeaMtVE7hVLjj4smaMIjDBZBMf0mbhvXKb6SGm3BdK49OO8JF5VNcB0JGDgu_Ve_XYnnrwon1An_mbRfzZtqMIcIKNxAnlepcKBQcSpq0-xGdOtPaRrLiQBYjYfjx7WDiYq_1bDdzEPZaH72kg3KqixCHk9NY1f-dO8_6Ee0yz_c4RYqohYeugZvw7VFoakEbeJaUSNetnyeleSqyzbsNk24hTaD7mILo6bS7Nt6DBP2GIuIp5_VXvifb3fOHAAAAAU4qzAsA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
