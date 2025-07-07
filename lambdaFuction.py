# add = lambda a, b: a + b
# print(add(10, 5))  # Output: 15
import pandas as pd

# is_even = lambda x: x % 2 == 0
# print(is_even(4))

# data = [(1, 'b'), (2, 'c'), (3, 'a')]
# sort = sorted(data, key=lambda x:x[0] )
# print(sort)

# df = pd.DataFrame({'amount': [100, 200, 300]})
# df['tax'] = df['amount'].apply(lambda x : x*0.18)
# print(df)


# squares = list(map(lambda x: x**2, nums))
# print(squares)

# sorting = list(filter(lambda x : x% 2 == 0, nums))
# print(sorting)

# from functools import reduce
# nums = [1, 2, 3, 4]
# total = reduce(lambda x , y : x + y , nums)
# print(total)

# words = ['apple', 'banana', 'kiwi']
# sorted_word = sorted(words, key =lambda x:len(x))
# print(words)

# df['bonus'] = df.apply(lambda row: row['salary'] * 0.10 if row['performance'] == 'High' else 0, axis=1)
# df.apply(lambda row :row[''] * 10 if row ['']== 'High' else 0, axis = 1)

# high_paid = ('salary', lambda x: sum(x > 50000))



