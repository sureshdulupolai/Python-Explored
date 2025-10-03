# ========================== Imports ==========================
import csv
import json
from functools import reduce
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any, Union, Optional

# ========================== History Class ==========================
class History:
    """
    Manage search history with navigation utilities.
    Supports next/previous/first/last/middle navigation.
    """

    def __init__(self, history_list: List[str]):
        self._history: List[str] = history_list
        self._index: int = -1  # Start before first element

        # Aliases for navigation methods
        self._aliases = {
            "all": self.all_items,
            "next": self.next_item,
            "previous": self.previous_item,
            "first": self.first_item,
            "last": self.last_item,
            "middle": self.middle_item,
        }

    def __getattr__(self, name: str):
        if name in self._aliases:
            return self._aliases[name]
        raise AttributeError(f"'History' object has no attribute '{name}'")

    # ---------------- Methods ----------------
    def all_items(self) -> List[str]:
        """Return all items in reverse order (most recent first)."""
        return self._history[::-1]

    def next_item(self) -> Optional[str]:
        """Return next item in history or None if end reached."""
        if self._index + 1 < len(self._history):
            self._index += 1
            return self._history[::-1][self._index]
        return None

    def previous_item(self) -> Optional[str]:
        """Return previous item in history or None if start reached."""
        if self._index > 0:
            self._index -= 1
            return self._history[::-1][self._index]
        return None

    def first_item(self) -> Optional[str]:
        """Return the first item (oldest) in history."""
        return self._history[-1] if self._history else None

    def last_item(self) -> Optional[str]:
        """Return the last item (latest) in history."""
        return self._history[0] if self._history else None

    def middle_item(self) -> Optional[str]:
        """Return the middle item in history."""
        if not self._history:
            return None
        mid = len(self._history) // 2
        return self._history[::-1][mid]


# ========================== Search Class ==========================
class Search:
    """
    Search manager for handling lists, dicts, CSV files.
    Supports multiple projects, single/multi search, history tracking.
    """

    _projects: Dict[str, "Search"] = {}

    # ---------------- Object Management ----------------
    def __new__(cls, MainList: Optional[Union[List[Any], tuple, set]] = None, Lw: bool = True, Next: bool = False,
        Key: Optional[str] = None, ProjectName: str = "my_project") -> "Search":

        if ProjectName in cls._projects:
            obj = cls._projects[ProjectName]
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

        obj = super().__new__(cls)
        cls._projects[ProjectName] = obj
        return obj

    def __init__(self, MainList: Optional[Union[List[Any], tuple, set]] = None, Lw: bool = True, Next: bool = False,
        Key: Optional[str] = None, ProjectName: str = "my_project") -> None:

        if hasattr(self, "_initialized") and self._initialized:
            return

        self.project: str = ProjectName
        self.Check: Optional[int] = None
        self.History: List[str] = []
        self.More: List[bool] = [Lw, Next]

        result = self._process_mainlist(MainList, Lw, Key)

        if result["status"] == "success":
            self.list: List[str] = result["list"]
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

        self._initialized = True

    # ---------------- Internal Processing ----------------
    def _process_mainlist(self, MainList: Optional[Union[List[Any], tuple, set]],
                          Lw: bool = True, Key: Optional[str] = None,
                          allow_append: bool = False) -> Dict[str, Any]:

        if MainList is None:
            MainList = []

        if not isinstance(MainList, (list, tuple, set)):
            return {"status": "error", "details": "MainList must be list, tuple, or set"}

        MainList = list(MainList)

        if not MainList:
            return {"status": "success", "list": []}

        first_type = type(MainList[0])
        if allow_append and hasattr(self, "list") and self.list:
            first_type = type(self.list[0])

        if first_type not in [str, dict]:
            return {"status": "error", "details": "Elements must be string or dict"}

        processed_list: List[str] = []

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

    # ---------------- Static Helpers ----------------
    @staticmethod
    def dict_choice(InputDict: Union[List[Dict[str, Any]], Dict[str, Any]],
                    Keys: Optional[List[str]] = None,
                    str_type: bool = True, repeat: bool = False) -> Union[List[str], Dict[str, str]]:

        try:
            dict_list = InputDict if isinstance(InputDict, list) else [InputDict]
            Keys = [Keys] if isinstance(Keys, str) else Keys or [""]

            flatten = lambda v: [
                str(x) if str_type else x if isinstance(x, str)
                else (_ for _ in ()).throw(TypeError(f"Non-string value found: {x}"))
                for y in (v if isinstance(v, (list, tuple, set)) else [v])
                for x in (flatten(y) if isinstance(y, (list, tuple, set)) else [y])
            ]

            out = [
                flatten(
                    reduce(
                        lambda d, k: d[k] if isinstance(d, dict) and k in d
                        else (_ for _ in ()).throw(KeyError(f"Key path '{Key}' not found in dict {item}")),
                        Key.split("."),
                        item
                    )
                )
                for item in dict_list for Key in Keys
            ]

            out = [x for sub in out for x in sub]
            return list(dict.fromkeys(out)) if repeat else out

        except (TypeError, KeyError) as e:
            return {"error": str(e), "status": "fail"}

    @staticmethod
    def from_csv(file_path: str, Keys: Optional[List[str]] = None,
                 str_type: bool = True, repeat: bool = False) -> Union[List[Dict[str, Any]], Dict[str, str]]:

        try:
            with open(file_path, newline='', encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                dict_list: List[Dict[str, Any]] = []

                for row in reader:
                    parsed_row: Dict[str, Any] = {}
                    for k, v in row.items():
                        v = v.strip() if isinstance(v, str) else v
                        try:
                            parsed_row[k] = json.loads(v) if v and v[0] in ['{', '['] else v
                        except Exception:
                            parsed_row[k] = v
                    dict_list.append(parsed_row)

            return Search.dict_choice(dict_list, Keys=Keys, str_type=str_type, repeat=repeat) if Keys else dict_list

        except Exception as e:
            return {"error": str(e), "status": "fail"}

    # ---------------- Utility Methods ----------------
    @classmethod
    def show_all_projects(cls) -> List[Dict[str, Any]]:
        return [
            {"Project-Name": obj.project, "details": obj.list}
            for obj in cls._projects.values()
        ]

    def single_search(self, InputValue: str) -> Optional[Dict[str, Any]]:

        def ShortOperation(self, InputValue: str) -> List[str]:
            if self.More[1]:
                return [i for i in self.list if len(InputValue) <= len(i) and i.startswith(InputValue)]
            return [i for i in self.list if InputValue in i]

        def FindOperation(self, InputValue: str) -> int:
            if self.More[1]:
                return sum(1 for i in self.list if len(InputValue) <= len(i) and i.startswith(InputValue))
            return sum(1 for i in self.list if InputValue == i)

        if not self.list:
            return None

        self.History.append(InputValue)
        InputValue = InputValue.lower() if self.More[0] else InputValue

        with ThreadPoolExecutor(max_workers=2) as executor:
            future_search = executor.submit(ShortOperation, self, InputValue)
            future_find = executor.submit(FindOperation, self, InputValue)
            search_result = future_search.result()
            find_result = future_find.result()

        SearchingIn = {
            "search": search_result,
            "find": find_result,
            "count": len(search_result)
        }
        self.Check = len(SearchingIn['search'])
        return SearchingIn

    def get_list(self) -> List[str]:
        """Return the processed list."""
        return self.list

    def history_iter(self) -> History:
        """Return a History object for iteration."""
        return History(self.History)


# ========================== Example / Testing ==========================
def TestingCSV():
    my_filter = Search()
    path = "employees.csv"

    print(my_filter.from_csv(path, Keys=["name"]))
    print()
    print(my_filter.from_csv(path, Keys=["info.skills"]))
    print()
    print(my_filter.from_csv(path, Keys=["projects"]))
    print()
    print(my_filter.from_csv(path))


# Uncomment to test
# TestingCSV()


def main_function() -> None:
    """
    Interactive search function for locations.
    """
    
    def printing(data: List[str]) -> None:
        for item in data:
            print(item)

    my_filter = Search(MainList=[
        'Sakinaka', 'Marol Naka', 'Ghatkopar',
        'Airport Road', 'Andheri', 'Versova',
        'Santacruz', 'Aaroli', 'Asalpha'
    ])
    
    while True:
        user_search: str = input("Search For Location: ").strip()
        lower_input = user_search.lower()

        if lower_input == 'exit-me':
            break

        elif lower_input == 'history-off':
            printing(data=my_filter.history_iter().all_items())
            continue

        data = my_filter.single_search(user_search)

        if not data or len(data['search']) == 0:
            print(f"No Location Found For {user_search}")
        else:
            printing(data=data['search'])
            print()


# Uncomment below to run
# main_function()