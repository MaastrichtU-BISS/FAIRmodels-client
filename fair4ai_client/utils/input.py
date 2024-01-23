from typing import List
import re

def read_choice_input(prefix="# ", valid: List[str] = [], case_upper=True):
    value = input(prefix)
    if case_upper: value = value.upper()
    while not value in map(str, valid):
        value = input(prefix)
        if case_upper: value = value.upper()
    return value

def read_pattern_input(prefix="> ", pattern: re.Pattern = r'.+', flags: re.RegexFlag = 0):
    value = input(prefix)
    while not re.match(pattern, value, flags):
        value = input(prefix)
    return value