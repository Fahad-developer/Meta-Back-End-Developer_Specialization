# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp

def to_mod_list(employee_list):
    """ Modifies the employee list of dictionaries into list of employee-department strings """

    mod_list = list(map(mod, employee_list))
    return mod_list

def generate_usernames(mod_list):
    """ Generates a list of usernames """

    username_list = [item.replace(" ", "_") for item in mod_list]
    return username_list

def map_id_to_initial(employee_list):
    """ Maps employee id to first initial """

    id_initial_map = {emp['name'][0]: emp['id'] for emp in employee_list}
    return id_initial_map

def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
    main()
