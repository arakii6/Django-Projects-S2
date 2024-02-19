# Imports
from faker import Faker
from .models import *
from Purchase.models import *
import random

# Create an instance of Faker Class.
fake = Faker()


# Function 1: To create fake customer data
def create_customer():
    try:
        for _ in range(5):
            Customer.objects.create(
                Name = fake.name(),
                Age = random.randint(18,60)
            )
    except Exception as e:
        print(f'Error: {e}')


# Function 2: To create fake purchase data
def create_purchase():
    try:
        for _ in range(5):
            Purchase.objects.create(
                Amount = round(random.uniform(10,100),2),
                FK = random.choice(Customer.objects.all())
            )
    except Exception as e:
        print(f'Error: {e}')


'''This allows for a more flexible approach, 
where we can run both functions together or seperately depending upon the need.'''
def create_data():
    create_customer()
    create_purchase()