from concurrent.futures import ThreadPoolExecutor
from functools import reduce

class History:
    def __init__(self, history_list):
        self._history = history_list
        self._index = -1  # Start before first element

        # Aliases for both normal & magic methods
        self._aliases = {
            "all": self.__all_,
            "__all_": self.__all_,
            "next": self.__next_,
            "__next_": self.__next_,
            "previous": self.__previous_,
            "__previous_": self.__previous_,
            "first": self.__first_,
            "__first_": self.__first_,
            "last": self.__last_,
            "__last_": self.__last_,
            "middle": self.__middle_,
            "__middle_": self.__middle_,
        }

    # Dynamic attribute resolution
    def __getattr__(self, name):
        if name in self._aliases:
            return self._aliases[name]
        raise AttributeError(f"'History' object has no attribute '{name}'")

    # ---------------- Methods ----------------
    def __all_(self):
        return self._history[::-1]

    def __next_(self):
        if self._index + 1 < len(self._history):
            self._index += 1
            return self._history[::-1][self._index]
        return None

    def __previous_(self):
        if self._index > 0:
            self._index -= 1
            return self._history[::-1][self._index]
        return None

    def __first_(self):
        return self._history[-1] if self._history else None

    def __last_(self):
        return self._history[0] if self._history else None

    def __middle_(self):
        if not self._history:
            return None
        mid = len(self._history) // 2
        return self._history[::-1][mid]

# ------------------ Integrate with Search class ------------------

class Search:
    # Class-level registry of projects
    _projects = {}

    def __new__(cls, MainList=None, Lw=True, Next=False, Key=None, ProjectName="my_project"):
        # Agar project pehle se exist karta hai → wahi return karo
        if ProjectName in cls._projects:
            obj = cls._projects[ProjectName]

            # Agar naye data diye gaye hain toh append kar do
            if MainList:
                result = obj._process_mainlist(MainList, Lw, Key, allow_append=True)
                if result["status"] == "success":
                    obj.list.extend(result["list"])
                else:
                    obj.init_error = {
                        "status": False,
                        "details": result["details"],
                        "Project-Name": obj.project
                    }
            return obj

        # Naya object banega
        obj = super().__new__(cls)
        cls._projects[ProjectName] = obj
        return obj

    def __init__(self, MainList=None, Lw=True, Next=False, Key=None, ProjectName="my_project"):
        # Agar object already initialized hai toh dobara init mat karo
        if hasattr(self, "_initialized") and self._initialized:
            return

        self.project = ProjectName
        self.Check = None
        self.History = []
        self.More = [Lw, Next]

        result = self._process_mainlist(MainList, Lw, Key)

        if result["status"] == "success":
            self.list = result["list"]
            self.init_error = {
                "status": True,
                "details": "All items processed successfully",
                "Project-Name": self.project
            }
        else:
            self.list = []
            self.init_error = {
                "status": False,
                "details": result["details"],
                "Project-Name": self.project
            }

        self._initialized = True  # mark as initialized

    def _process_mainlist(self, MainList, Lw=True, Key=None, allow_append=False):
        if MainList is None:
            MainList = []

        if not isinstance(MainList, (list, tuple, set)):
            return {"status": "error", "details": "MainList must be list, tuple, or set"}

        MainList = list(MainList)

        # agar empty diya aur append karna hai → kuch bhi add nahi hoga
        if not MainList:
            return {"status": "success", "list": []}

        # Check type consistency
        if allow_append and hasattr(self, "list") and self.list:
            first_type = type(self.list[0])  # jo pehle se hai wahi type enforce hoga
        else:
            first_type = type(MainList[0])

        if first_type not in [str, dict]:
            return {"status": "error", "details": "Elements must be string or dict"}

        processed_list = []

        for item in MainList:
            if not isinstance(item, first_type):
                return {"status": "error", "details": f"All elements must be of type {first_type.__name__}"}

            if isinstance(item, str):
                processed_list.append(item.lower() if Lw else item)

            elif isinstance(item, dict):
                if not item:
                    return {"status": "error", "details": "Dict inside MainList cannot be empty"}
                if Key is None:
                    return {"status": "error", "details": "Key parameter required for dicts"}
                if Key not in item:
                    return {"status": "error", "details": f"Key '{Key}' not found in dict {item}"}
                val = item[Key]
                if not isinstance(val, str):
                    return {"status": "error", "details": f"Value of key '{Key}' must be string"}
                processed_list.append(val.lower() if Lw else val)

        return {"status": "success", "list": processed_list}
    
    def __dict_choice__(InputDict, Keys=None, type=True, repeat=False):
        try:
            dict_list = InputDict if isinstance(InputDict, list) else [InputDict]
            Keys = [Keys] if isinstance(Keys, str) else Keys or [""]

            flatten = lambda v: [str(x) if type else x if isinstance(x,str) else (_ for _ in ()).throw(TypeError(f"Non-string value found: {x}"))
                for y in (v if isinstance(v,(list,tuple,set)) else [v])
                for x in (flatten(y) if isinstance(y,(list,tuple,set)) else [y])]

            out = [flatten(reduce(lambda d,k: d[k] if isinstance(d,dict) and k in d else (_ for _ in ()).throw(KeyError(f"Key path '{Key}' not found in dict {item}")), Key.split("."), item))
                for item in dict_list for Key in Keys]

            out = [x for sub in out for x in sub]

            return list(dict.fromkeys(out)) if repeat else out

        except (TypeError, KeyError) as e:
            return {"error": str(e), "status": "fail"}

    # 🔹 New function: Show all projects with details
    @classmethod
    def show_all_projects(cls):
        return [
            {"Project-Name": obj.project, "details": obj.list}
            for obj in cls._projects.values()
        ]
    
    def __single__(self, InputValue):
        
        def ShortOperation(self, InputValue):
            if self.More[1]:
                # Prefix search mode
                return [i for i in self.list if len(InputValue) <= len(i) and i.startswith(InputValue)]
            else:
                # Normal substring search mode
                return [i for i in self.list if InputValue in i]

        def FindOperation(self, InputValue):
            if self.More[1]:
                # Prefix match → count how many start with InputValue
                return sum(1 for i in self.list if len(InputValue) <= len(i) and i.startswith(InputValue))
            else:
                # Exact match → count how many are exactly equal
                return sum(1 for i in self.list if InputValue == i)

        if len(self.list) <= 0:
            return None
        
        self.History.append(InputValue)
        InputValue = InputValue.lower() if self.More[0] else InputValue
        
        # run parallel
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_search = executor.submit(ShortOperation, self, InputValue)
            future_find   = executor.submit(FindOperation, self, InputValue)
            search_result = future_search.result()
            find_result   = future_find.result()
        
        SearchingIn = {
            "search": search_result,
            "find": find_result,
            "count" : len(search_result)
        }
        self.Check = len(SearchingIn['search'])
        return SearchingIn

    def __CheckList__(self):
        return self.list
    
    def __history_iter__(self):
        """Return a HistoryManager object for this instance"""
        return History(self.History)

def MainFunction():

    def Printing(data):
        for i in data:
            print(i)
    
    my_filter = Search(MainList=[
        'Sakinaka', 'Marol Naka', 'Ghatkopar', 
        'Airport Road', 'Andheri', 'Versova', 
        'Santacruz', 'Aaroli', 'Asalpha'
    ])

    print(my_filter.show_all_projects())

    while True:
        UserSearch = input("Search For Location: ")

        if UserSearch.lower() in ['exit']:
            break

        elif UserSearch.lower() in ['history']:
            Printing(data=my_filter.__history_iter__().__all_())
            continue

        data = my_filter.__single__(UserSearch)
    
        if not data or len(data['search']) == 0:
            print(f"No Location Found For {UserSearch}")
        elif data['find'] == True:
            break
        else:
            Printing(data=data['search'])
            print()

    return None

MainFunction()
