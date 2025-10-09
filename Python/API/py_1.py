import time
import json
from data import products, users, orders
from concurrent.futures import ThreadPoolExecutor

class APIManager:
    API_Name = ""        # Global API name across all instances
    API_Registry = {}    # Keeps track of all projects per API_Name

    def __init__(self, LogName=None, API=None, ProjectName=None):
        if LogName:
            APIManager.API_Name = LogName

        self.ProjectName = ProjectName
        self.API = API if API else []
        # Initialize registry for this API_Name if not already
        if APIManager.API_Name not in APIManager.API_Registry:
            APIManager.API_Registry[APIManager.API_Name] = []
        self.All_API = APIManager.API_Registry[APIManager.API_Name]

    # ---------------- Validation Helpers ----------------
    def _validate_api_data(self, API):
        if not isinstance(API, list):
            return False, "Data is not a list"
        if not API:
            return True, "Data is empty"
        if not all(isinstance(item, dict) for item in API):
            return False, "All items must be dictionaries"
        base_keys = set(API[0].keys())
        for idx, item in enumerate(API):
            if set(item.keys()) != base_keys:
                return False, f"Dict at index {idx} has mismatched keys"
        return True, "Valid"

    def _project_exists(self, name):
        return any(api['ProjectName'].lower() == name.lower() for api in self.All_API)

    def _find_project(self, name):
        for api in self.All_API:
            if api["ProjectName"].lower() == name.lower():
                return api
        return None

    # ---------------- CRUD Methods ----------------
    def fetch(self, API, APIName=None):
        """Add new API data (prevents duplicate project names)."""
        start_time = time.time()
        ProjectName = APIName or self.ProjectName
        if not ProjectName:
            return {"status": "error", "message": "ProjectName required.", "bool": False}

        is_valid, msg = self._validate_api_data(API)
        if not is_valid:
            return {"status": "error", "message": msg, "bool": False}

        if self._project_exists(ProjectName):
            return {"status": "error", "message": f"Project '{ProjectName}' already exists.", "bool": False}

        self.All_API.append({"ProjectName": ProjectName, "API": API})
        APIManager.API_Registry[APIManager.API_Name] = self.All_API  # Keep global registry updated
        self.API = API
        return {"status": "success","API_Name": APIManager.API_Name,"ProjectName": ProjectName,"API_Count": len(API),"API_List": [proj["ProjectName"] for proj in self.All_API],"time": round(time.time() - start_time, 5),"bool": True,"API" : self.API}

    def get_record(self, Name=""):
        if not self.All_API:
            return {"status": "error", "message": "No APIs stored.", "bool": False}

        if not Name.strip():
            first = self.All_API[0]
            return {"status": "success", "ProjectName": first["ProjectName"], "API": first["API"], "bool": True}

        found = self._find_project(Name)
        if found:
            return {"status": "success", "ProjectName": found["ProjectName"], "API": found["API"], "bool": True}

        return {"status": "error", "message": f"No record found with ProjectName '{Name}'.", "bool": False}

    def search(self, Name):
        """Check if project exists (True/False)."""
        return any(api['ProjectName'].lower() == Name.lower() for api in self.All_API)

    def delete(self, Name):
        """Delete a project by name."""
        found = self._find_project(Name)
        if not found:
            return {"status": "error", "message": f"No project '{Name}' found.", "bool": False}
        self.All_API.remove(found)
        APIManager.API_Registry[APIManager.API_Name] = self.All_API  # Update global registry
        return {"status": "success", "message": f"Project '{Name}' deleted.", "API_List": [proj["ProjectName"] for proj in self.All_API], "bool": True}

    def update(self, Name, new_data, replace=False):
        found = self._find_project(Name)
        if not found:
            return {"status": "error", "message": f"Project '{Name}' not found.", "bool": False}

        if replace:
            found["API"] = new_data
            return {"status": "success", "message": f"Project '{Name}' replaced successfully.", "bool": True}

        # merge mode → add only new unique records
        existing_serialized = [json.dumps(d, sort_keys=True) for d in found["API"]]
        added = 0
        for new_item in new_data:
            serialized = json.dumps(new_item, sort_keys=True)
            if serialized not in existing_serialized:
                found["API"].append(new_item)
                existing_serialized.append(serialized)
                added += 1

        return {"status": "success", "message": f"Added {added} new records to '{Name}'.", "bool": True}

    # 📦 Summary
    def summary(self):
        return {
            "API_Name": APIManager.API_Name,
            "API_List": [proj["ProjectName"] for proj in self.All_API],
            "Total_Projects": len(self.All_API)
        }
    
    def listing_data(self, response=None):
        if not response:
            return None, "Response Not Found"
        return response['API']
    
    def error(self, response=None):
        if not response:
            return None, "Response Not Found"
        return response['bool']
        
    def fetching_value(self, response=None):
        if not response:
            return False, []

        with ThreadPoolExecutor() as executor:
            api_list, error_bool = executor.submit(self.listing_data, response).result(), \
                                executor.submit(self.error, response).result()
        return error_bool, api_list

# ---------------- Example Usage ----------------
if __name__ == "__main__":
    api = APIManager(LogName="Main API Manager")

    res1 = api.fetch(products, "Products API")
    res2 = api.fetch(users, "Users API")
    re3 = []
    error, value = api.fetching_value(res2)
    print(value)

    # print(api.listing_data(res2))

    # res3 = api.fetch(orders, "Orders API")

    # print("Fetch Results:")
    # for r in [res1, res2, res3]:
    #     if r.get("bool"):
    #         print("✅", r)
    #     else:
    #         print("❌", r)
    # print()

    # # ✅ Update
    # extra_data = [{"id": 4, "name": "Mouse", "price": 500}]
    # print(api.update("Products API", extra_data, replace=False)["message"])

    # # ✅ Replace data
    # new_set = [{"id": 1, "name": "Monitor", "price": 8000}]
    # print(api.update("Products API", new_set, replace=True)["message"])

    # # ✅ Delete
    # print(api.delete("Orders API"))

    # # ✅ Check summary
    # print(api.summary())
