import re
from re import sub
NBSP = '\u00A0'


patterns = [
    # handle quotes
    (r'([\'"])(.*?)(\1)', r'«\2»'),
    # replace hypen with dash such case like : это,вот,Я-
    (r'([а-яА-Яa-zA-Z]{1,3})\-\.*?', r'\1—\2'),
    # replace hyphen with n-dash in numbers example:+7(903)-123-45-67
    (r'(^[\+|0])(\d+)[-|?](\d+)-(\d+)-(\d+)', r'\1\2–\3–\4–\5 '),
    # join words with digit by nbsp
    (r'(\d+)[\s+|*?](\w+)', r'\1{}\2'.format(NBSP)),
    # remove win-like newlines
    (r'\r\n', r'\n'),
    # replace extra newlines
    (r'\n{2,}', r'\n'),
    # remove tabs
    (r'\t', r' '),
    # remove extra spaces
    (r'[ ]{2,}', r' '),
]



def typo(text):
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text