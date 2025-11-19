from faker import Faker

fake = Faker()


def fake_data():
    first_name = fake.first_name()
    last_name = fake.last_name()
    zip_code = fake.zipcode()
    return first_name, last_name, zip_code

