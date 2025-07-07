import pandas as pd
import random
from faker import Faker

fake = Faker()
data = []

for _ in range(100):  # 100 dummy records
    data.append({
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "product": random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "USB Cable"]),
        "quantity": random.randint(1, 5),
        "price_per_unit": random.choice([5000, 1000, 1500, 8000, 200]),
        "order_date": fake.date_between(start_date='-30d', end_date='today')
    })

df = pd.DataFrame(data)
df.to_csv(r"C:\Users\Admin\Desktop\DATA Generator\sales_data.csv", index=False)
