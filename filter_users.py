import json

def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)
    
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    
    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)

def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("email", "").lower() == email.lower()]

    for user in filtered_users:
        print(user)

if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name, age or email' are supported): ").strip().lower()

    match filter_option:
        case "name":
            criteria = input("Enter a name to filter users: ").strip()
            filter_users_by_name(criteria)
        case "age":
            criteria = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(criteria)
        case "email":
            criteria = input("Enter an email to filter users: ").strip()
            filter_users_by_email(criteria)
        case _:
            print(f"Filtering by {filter_option} is not yet supported.")
