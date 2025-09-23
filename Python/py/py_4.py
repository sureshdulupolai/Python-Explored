from collections import Counter

# Sample data
companies = [
    {
        "name": "TechSoft",
        "employees": [
            {"name": "Amit"},
            {"name": "Riya"},
            {"name": "Sohan"}
        ]
    },
    {
        "name": "DataCorp",
        "employees": [
            {"name": "Anita"},
            {"name": "Karan"},
            {"name": "Neha"}
        ]
    },
    {
        "name": "FinSolve",
        "employees": [
            {"name": "Vikas"},
            {"name": "Priya"},
            {"name": "Arjun"}
        ]
    }
]

# Function: get employees per company
def get_company_employees(companies):
    return [(c['name'], [e['name'] for e in c['employees']]) for c in companies]

# Function: all employees across companies
def get_all_employees(companies):
    return [e['name'] for c in companies for e in c['employees']]

# Function: employee frequency (example for duplicates)
def employee_frequency(companies):
    all_emps = get_all_employees(companies)
    return Counter(all_emps)

# Main execution
company_employees = get_company_employees(companies)
print("Employees per company:", company_employees)

all_employees = get_all_employees(companies)
print("All employees:", all_employees)

freq = employee_frequency(companies)
print("Employee frequency:", freq)

# Example: Filter companies with more than 2 employees
large_companies = [
    (
        c['name'], [e['name'] for e in c['employees']]
    ) 
    for c in companies if len(c['employees']) > 2
]
print("Companies with >2 employees:", large_companies)
