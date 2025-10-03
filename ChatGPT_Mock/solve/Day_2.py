
text = "Python is easy and Python is powerful"

count_dict = {}
# print(f"{text.split()}") => ['Python', 'is', 'easy', 'and', 'Python', 'is', 'powerful']
for word in text.split():
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

print(count_dict) # {'Python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}