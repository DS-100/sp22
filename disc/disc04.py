import re

def q3(txt):
    """
    >>> sometext = "I've got 10 eggs, 20 gooses, and 30 giants."
    >>> q3(sometext)
    ['10 eggs', '20 gooses', '30 giants']
    """
    pat = r'\d{2}\s\w+'
    return re.findall(pat,txt)

def q5(txt):
    r"""
    >>> log = "169.237.46.168 - - [26/Jan/2014:10:47:58 -0800]\rGET /stat141/Winter04/ HTTP/1.1 200 2585\rhttp://anson.ucdavis.edu/courses/"
    >>> q5(log)
    26
    Jan
    2014
    """
    pattern = r'\[(\d{2})\/(\w+)\/(\d{4}):'
    matches = re.findall(pattern, txt)
    day, month, year = matches[0]
    print(day)
    print(month)
    print(year) 

def q6(txt):
    """
    >>> text = "a big moon, between us..." 
    >>> q6(text)
    'a.i.oo.e.ee.u.'
    """
    pat = r'[^aeiou]+'
    return re.sub(pat,".",txt)


