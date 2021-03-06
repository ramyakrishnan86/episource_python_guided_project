# %load q04_create_newframe/build.py
import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from greyatomlib.episource_python_guided_project.q03_remove_wordcount.build import q03_remove_wordcount
path = 'data/episource.txt'


def q04_create_newframe(path):

    df = q03_remove_wordcount(path)
    condition = (df['words'].str.len() > 5) & (df['count'] > 10)

    conditional_df = df.loc[condition]
    return conditional_df

# q04_create_newframe(path)


