# %load q02_create_dataframe/build.py
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import pandas as pd
import re
from collections import Counter
from greyatomlib.episource_python_guided_project.q01_load_data.build import q01_load_data
path = 'data/episource.txt'


def q02_create_dataframe(data):
# write your solution here'
    data = q01_load_data(path)

    regex = re.compile('[^a-zA-Z]')
    regex_data = regex.sub(' ', data[0])
    words = Counter(regex_data.split())

    df = pd.DataFrame(list(words.items()), columns=['words', 'count'])
    
    return df

# q02_create_dataframe(path)


