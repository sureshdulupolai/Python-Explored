"""
for-loop + append
map + lambda
list comprehension + function


Reusability & readability chahiye → function use karo
Short, one-off scripts → inline list comprehension ya for-loop better

Performance ke liye:
Use list comprehension over +=
Avoid unnecessary lambda nesting for huge datasets
Function call overhead negligible for most real-life scenarios


| Task                       | Prefer                      | Avoid                 |
| -------------------------- | --------------------------- | --------------------- |
| Append to list             | `append()`                  | `+= [item]`           |
| Transform list             | List comprehension          | Nested map/lambda     |
| Filter list                | `filter()` or comprehension | Manual loops with if  |
| Reusable logic             | Functions                   | Copy-paste code       |
| Search in large collection | dict/set                    | list linear search    |
| Memory efficiency          | Generators                  | temporary large lists |
| Loop with index            | `enumerate()`               | manual counter        |
| Sorting                    | `list.sort()`               | manual sorting        |
| Frequency counting         | `Counter`                   | manual dict counts    |


| Task                           | Prefer (Example)                                | Avoid (Example)                                              |
| ------------------------------ | ----------------------------------------------- | ------------------------------------------------------------ |
| **Append to list**             | `lst = []; lst.append(5)`                       | `lst = []; lst += [5]`                                       |
| **Transform list**             | `squares = [x**2 for x in range(5)]`            | `squares = list(map(lambda x: x**2, [0,1,2,3,4]))`           |
| **Filter list**                | `evens = [x for x in range(10) if x%2==0]`      | `evens = []; for x in range(10): if x%2==0: evens.append(x)` |
| **Reusable logic**             | `def greet(name): return f"Hi {name}"`          | `print("Hi Alice"); print("Hi Bob")`                         |
| **Search in large collection** | `my_set = {1,2,3}; 2 in my_set`                 | `my_list = [1,2,3]; 2 in my_list`                            |
| **Memory efficiency**          | `sum(x*x for x in range(1000))`                 | `sum([x*x for x in range(1000)])`                            |
| **Loop with index**            | `for i, val in enumerate(lst): print(i,val)`    | `i=0; for val in lst: print(i,val); i+=1`                    |
| **Sorting**                    | `lst.sort()`                                    | `# manual bubble sort or insertion sort`                     |
| **Frequency counting**         | `from collections import Counter; Counter(lst)` | `d={}; for x in lst: d[x]=d.get(x,0)+1`                      |

"""

