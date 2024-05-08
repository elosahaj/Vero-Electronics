import random as random
import datetime
import mysql.connector

# Connecting to the database

db_config = {
    'user': 'root',
    'password': '**********',
    'host': 'localhost',
    'database': 'vero_electronics',
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Lists and dictionaries to create random orders

gender_list = ['M', 'F']

male_names = [
    "James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Charles", "Thomas",
    "Christopher", "Daniel", "Matthew", "Anthony", "Donald", "Mark", "Paul", "Steven", "Andrew", "Kenneth",
    "Joshua", "Kevin", "Brian", "George", "Edward", "Ronald", "Timothy", "Jason", "Jeffrey", "Ryan",
    "Jacob", "Gary", "Nicholas", "Eric", "Jonathan", "Stephen", "Larry", "Justin", "Scott", "Brandon",
    "Benjamin", "Samuel", "Gregory", "Frank", "Alexander", "Raymond", "Patrick", "Jack", "Dennis",
    "Jerry", "Tyler", "Aaron", "Jose", "Henry", "Adam", "Douglas", "Nathan", "Peter", "Zachary",
    "Kyle", "Walter", "Harold", "Jeremy", "Ethan", "Carl", "Keith", "Roger", "Gerald", "Christian",
    "Terry", "Sean", "Arthur", "Austin", "Noah", "Lawrence", "Jesse", "Joe", "Bryan", "Billy",
    "Jordan", "Albert", "Dylan", "Bruce", "Willie", "Gabriel", "Alan", "Juan", "Logan", "Wayne",
    "Ralph", "Roy", "Eugene", "Randy", "Vincent", "Russell", "Louis", "Philip", "Bobby", "Johnny"
]

female_names = [
    "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Margaret", "Lisa", "Betty", "Dorothy", "Sandra", "Ashley", "Kimberly", "Donna", "Emily",
    "Michelle", "Carol", "Amanda", "Melissa", "Deborah", "Stephanie", "Rebecca", "Laura", "Sharon",
    "Cynthia", "Kathleen", "Amy", "Shirley", "Angela", "Helen", "Anna", "Brenda", "Pamela", "Nicole",
    "Emma", "Samantha", "Katherine", "Christine", "Debra", "Rachel", "Catherine", "Carolyn", "Janet",
    "Ruth", "Maria", "Heather", "Diane", "Virginia", "Julie", "Joyce", "Victoria", "Olivia", "Kelly",
    "Christina", "Lauren", "Joan", "Evelyn", "Judith", "Megan", "Cheryl", "Andrea", "Hannah", "Martha",
    "Jacqueline", "Frances", "Gloria", "Ann", "Teresa", "Kathryn", "Sara", "Janice", "Jean", "Alice",
    "Madison", "Doris", "Abigail", "Julia", "Judy", "Grace", "Denise", "Amber", "Marilyn", "Beverly",
    "Danielle", "Theresa", "Sophia", "Marie", "Diana", "Brittany", "Natalie", "Isabella", "Charlotte"
]

surnames = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez",
    "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez",
    "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson",
    "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans",
    "Edwards", "Collins", "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell",
    "Murphy", "Bailey", "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson",
    "Gray", "Ramirez", "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood",
    "Barnes", "Ross", "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson",
    "Hughes", "Flores", "Washington", "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander",
    "Russell", "Griffin", "Diaz", "Hayes"]

producer_list = {
    "Apple": {"id": 1},
    "Samsung": {"id": 2},
    "Sony": {"id": 3},
    "Microsoft": {"id": 4},
    "LG": {"id": 5},
    "Panasonic": {"id": 6},
    "Lenovo": {"id": 7},
    "HP": {"id": 8},
    "Dell": {"id": 9},
    "Huawei": {"id": 10}
}

product_list = {
    "Smartphone": {"id": 1, "price": [800, 1500]},
    "Laptop": {"id": 2, "price": [2000, 3000]},
    "Tablet": {"id": 3, "price": [400, 800]},
    "Smartwatch": {"id": 4, "price": [250, 500]},
    "Television": {"id": 5, "price": [2000, 5000]},
    "Headphones": {"id": 6, "price": [100, 300]},
    "Digital Camera": {"id": 7, "price": [900, 1500]},
    "Printer": {"id": 8, "price": [300, 500]},
    "Router": {"id": 9, "price": [150, 300]},
    "External Hard Drive": {"id": 10, "price": [150, 500]}
}

product_colour = {
    "white": {"id": 1},
    "black": {"id": 2},
    "silver": {"id": 3}
}

# Functions

def generate_buyer():
    """Generates a random buyer data"""
    gender = random.choice(gender_list)
    if gender == 'F':
        first_name = random.choice(female_names)
    else:
        first_name = random.choice(male_names)
    last_name = random.choice(surnames)
    email = (first_name+last_name+"@email.com").lower()
    buyer = [first_name, last_name, email]
    return buyer

def generate_order_items(product_list, producer_list, product_colour):
    """Generates a random order list of items with different properties, quantities and price ranges"""
    quantities = [1, 2, 3]
    probabilities = [0.6, 0.3, 0.1]
    quantity = random.choices(quantities, probabilities)[0]
    items = []
    for _ in range(quantity):
        product = random.choice(list(product_list.keys()))
        producer = random.choice(list(producer_list.keys()))
        colour = random.choice(list(product_colour.keys()))
        price_range = product_list[product]["price"]
        price = random.randint(price_range[0], price_range[1])
        items.append({
            'product_id': product_list[product]['id'],
            'producer_id': producer_list[producer]['id'],
            'colour_id': product_colour[colour]['id'],
            'price': price
        })
    return items


def generate_purchase_time():
    """Sets and formats the current time as purchase time"""
    current_time = datetime.datetime.now()
    purchase_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return purchase_time

def populate_tables(num_orders):
    """Inserts data generated via other functions to the tables in a local database"""
    for _ in range(num_orders):
        buyer = generate_buyer()
        cursor.execute("INSERT INTO customers (first_name, last_name, email) VALUES (%s, %s, %s)", buyer)
        customer_id = cursor.lastrowid

        order_items = generate_order_items(product_list, producer_list, product_colour)
        total_amount = sum(item['price'] for item in order_items)

        purchase_time = generate_purchase_time()

        cursor.execute("INSERT INTO orders (customer_id, amount, purchase_time) VALUES (%s, %s, %s)", (customer_id, total_amount, purchase_time))
        order_id = cursor.lastrowid

        for item in order_items:
            cursor.execute("INSERT INTO items (order_id, product_id, producer_id, colour_id, price) VALUES (%s, %s, %s, %s, %s)",
                           (order_id, item['product_id'], item['producer_id'], item['colour_id'], item['price']))

    conn.commit()
    cursor.close()
    conn.close()



populate_tables(1)
