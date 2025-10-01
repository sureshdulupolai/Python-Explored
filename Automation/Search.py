from concurrent.futures import ThreadPoolExecutor

class Search:
    def __init__(self, MainList=None, Lw=True, ProjectName="my_project", Key=None):
        self.project = ProjectName
        self.Check = None
        self.History = []
        self.Lw = Lw

        result = self._process_mainlist(MainList, Lw, Key)

        if result["status"] == "success":
            self.list = result["list"]
            self.init_error = {"status": True, "details": "All items processed successfully"}
        else:
            self.list = []
            self.init_error = {"status": False, "details": result["details"]}

    def _process_mainlist(self, MainList, Lw=True, Key=None):
        if MainList is None:
            MainList = []

        if not isinstance(MainList, (list, tuple, set)):
            return {"status": "error", "details": "MainList must be list, tuple, or set"}

        MainList = list(MainList)

        if not MainList:
            return {"status": "success", "list": []}

        first_type = type(MainList[0])
        if first_type not in [str, dict]:
            return {"status": "error", "details": "First element must be string or dict"}

        processed_list = []
 
        for item in MainList:
            if not isinstance(item, first_type):
                return {"status": "error", "details": "All elements must be of same type as first element"}

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
    
    def __single__(self, InputValue):

        def ShortOperation():
            return [i for i in self.list if InputValue in i]
        
        def FindOperation():
            return any(InputValue == i for i in self.list)

        if len(self.list) <= 0:
            return None
        
        self.History.append(InputValue)
        InputValue = InputValue.lower() if self.Lw else InputValue

        # run parallel
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_search = executor.submit(ShortOperation)
            future_find   = executor.submit(FindOperation)
            search_result = future_search.result()
            find_result   = future_find.result()

        SearchingIn = {
            "search": search_result,
            "find": find_result
        }
        self.Check = len(SearchingIn['search'])
        return SearchingIn

    def __CheckList__(self):
        return self.list
    
    def __his__(self):
        return self.History[::-1]


def MainFunction():

    def Printing(data):
        for i in data:
            print(i)
    
    my_filter = Search(MainList=[
        'Sakinaka', 'Marol Naka', 'Ghatkopar', 
        'Airport Road', 'Andheri', 'Versova', 
        'Santacruz', 'Aaroli', 'Asalpha'
    ])

    while True:
        UserSearch = input("Search For Location: ")

        if UserSearch.lower() in ['exit']:
            break

        elif UserSearch.lower() in ['history']:
            Printing(data=my_filter.__his__())
            continue

        data = my_filter.__single__(UserSearch)

        if not data or len(data['search']) == 0:
            print(f"No Location Found For {UserSearch}")
        elif data['find'] == True:
            break
        else:
            Printing(data=data['search'])
        
    return None

MainFunction()
