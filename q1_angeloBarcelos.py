accountList = [
    {"name": "Angelo", "balance": 1000, "account": "1111", "password": "1234"},
    {"name": "Vithor", "balance": 2000, "account": "2222", "password": "1234"},
    {"name": "Julio", "balance": 3000, "account": "3333", "password": "1234"},
    {"name": "Ana Clara", "balance": 4000, "account": "4444", "password": "1234"},
    {"name": "Iury", "balance": 5000, "account": "5555", "password": "1234"}
]

cash = lambda: "Cash"
fund = lambda: "Found"
credit = lambda: "Credit"

validate_user = lambda name, password: next((user for user in accountList if user["name"] == name and user["password"] == password), None)
create_transaction_menu = lambda: (lambda username, password: (lambda logged_user: (lambda: print("Welcome,", logged_user["name"]) or create_transaction(logged_user) if logged_user else print("Invalid username or password.") or None)())(validate_user(username, password)))(input("Enter your username: "), input("Enter your password: "))
create_transaction = lambda user: (lambda choice: (lambda: cash() if choice == "0" else (lambda: fund() if choice == "1" else (lambda: credit() if choice == "2" else print("Invalid transaction choice, please enter 0, 1, or 2."))))() if choice.isdigit() and 0 <= int(choice) <= 2 else print("Invalid transaction choice, please enter a number."))(input("Choose a transaction: \n0 - Cash \n1 - Fund \n2 - Credit\n"))

print(create_transaction_menu())