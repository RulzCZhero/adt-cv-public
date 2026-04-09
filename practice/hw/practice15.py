from collections import defaultdict

def report_city_spending(transactions :list[set]):
    totalSpent = defaultdict(float)
    uniqueCustomers = defaultdict(set)
    for city, customer, cash in transactions:
        totalSpent[city]+=cash
        uniqueCustomers[city].add(customer)
    for key,value in totalSpent.items():
        print(f"{key}: {value} CZK ({len(uniqueCustomers[key])} unique customers)")

def main():
    data = [
    ("Plzeň", "S1", 500.0),
    ("Praha", "S2", 1000.0),
    ("Plzeň", "S1", 250.0), # Same customer, different purchase
    ("Plzeň", "S3", 300.0),
    ("Praha", "S4", 100.0)
]
    report_city_spending(data)
    

if __name__=='__main__':
    main()