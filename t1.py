# import pandas as pd
# # import lxml

# df = pd.read_html('https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D', header = 0)[0] 

# print(df.head())

import pandas as pd
dict_data = {'a': 1, 'b': 2, 'c': 3}
sr = pd.Series(dict_data)

print(sr)