# -*- coding: utf-8 -*-
"""
Created on 2019-5-20

@author: cheng.li
"""

import re

CHINESE_WORDS_MAPPING = [
    {"P2 Lite": ["pr light", "p2 light", "皮尔，light", "p2 let", "pr lie", "pr let", "皮尔莱特", "p2赖"]},
    {"T2 Lite": ["Tr，light", "T2 light", "提尔莱特", "提尔赖特"]},
    {"T2 Mini": ["T2迷你", "提尔迷你"]},
    {"P2 Pro": ["p up o", "皮尔pro", "皮尔普洱", "皮尔普尔", "皮尔普二"]},
    {"V2 Pro": ["Vr pro", "vrpro", "vrpo", "V up"]},
    {"电子价签": ["电子价钱", "垫子价钱", "垫子价签", "ESL", "价签"]},
    {"L2K": ["L，二，k", "L2 k", "LRK", "12k"]},
    {"V1S": ["V 1s", "ves"]},
    {"码利奥": ["马里奥", "玛丽奥"]},
    {"D2": ["第二"]},
    {"H1": ["he"]},
    {"K1": ["k，依", "k，一", "ke"]},
    {"L2": ["L，二"]},
    {"M2": ["M，二"]},
    {"P1": ["P，一", "皮衣", "pe"]},
    {"S2": ["S，二"]},
    {"T2": ["T，二", "题，二", "T，2", "提尔"]},
    {"V2": ["V，二", "V，2", "V二", "威尔", "vr", "威尔"]},
    {"W1": ["W 一", "W，一", "We", "W一"]},
    {"小闪": ["小山", "小衫", "小散", "小伞", "小三", "小产"]},
    {"你": ["您"]}
]


ENGLISH_WORDS_MAPPING = [
    {"you": ["your"]}
]


def calibrate_products(q, language):

    if language == 'cn' or language == 'chinese':
        words_mapping = CHINESE_WORDS_MAPPING
    else:
        words_mapping = ENGLISH_WORDS_MAPPING

    match_products = None
    for w_dict in words_mapping:
        w_words = list(w_dict.values())[0]
        w_key = list(w_dict.keys())[0].lower()
        match_products = [m.lower() for m in re.findall('|'.join(w_words), q, re.IGNORECASE)]
        if match_products:
            break

    if match_products:
        word = match_products[0]
        q = re.sub(word, w_key.lower(), q, flags=re.IGNORECASE)
    return q