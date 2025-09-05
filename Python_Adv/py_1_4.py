import re
# re.match(pattern, string) -> Syntax

result = re.match(r"Hello", "Hello World")
print(result)  # Match object milega => <re.Match object; span=(0, 5), match='Hello'>


result = re.search(r"World", "Hello World")
print(result.group())  # 👉 "World"

result = re.findall(r"\d", "My number is 12345")
print(result)  # 👉 ['1', '2', '3', '4', '5']

for m in re.finditer(r"\d", "A1B2C3"):
    print(m.group(), "at", m.start())

text = "apple 123 banana 456"
new_text = re.sub(r"\d+", "#", text)
print(new_text)  # 👉 "apple # banana #"

"""

Common Regex Patterns:

| Pattern  | Meaning                                   |
| -------- | ----------------------------------------- |
| `.`      | koi bhi ek character (except newline)     |
| `\d`     | digit (0-9)                               |
| `\D`     | non-digit                                 |
| `\w`     | word character (a-z, A-Z, 0-9, \_)        |
| `\W`     | non-word character                        |
| `\s`     | whitespace (space, tab, newline)          |
| `\S`     | non-whitespace                            |
| `^`      | string ki shuruaat                        |
| `$`      | string ka end                             |
| `[...]`  | character set (e.g. `[abc]` → a, b, ya c) |
| `[^...]` | not in set                                |
| `*`      | 0 ya zyada repetitions                    |
| `+`      | 1 ya zyada repetitions                    |
| `?`      | 0 ya 1 occurrence                         |
| `{m,n}`  | m se n tak occurrences                    |


"""

text = "Order numbers: 123, 456, 789"
nums = re.findall(r"\d+", text)
print(nums)  # 👉 ['123', '456', '789']


email = "test@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(pattern, email)))  # 👉 True

text = "Call me at 9876543210 or 123-456-7890"
phones = re.findall(r"\d{10}|\d{3}-\d{3}-\d{4}", text)
print(phones)  # 👉 ['9876543210', '123-456-7890']

text = "apple123banana!grape"
words = re.split(r"[^a-zA-Z]+", text)
print(words)  # 👉 ['apple', 'banana', 'grape']

"""

re.match → shuruaat se match
re.search → kahin bhi ek match
re.findall → saare matches
re.sub → replace karna

"""