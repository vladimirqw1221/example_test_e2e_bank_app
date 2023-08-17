from faker import Faker
from data.data_person import DataPerson

fake_data = Faker(locale='en_US')


def generate_data():
    yield DataPerson(
        first_name=fake_data.first_name(),
        last_name=fake_data.last_name(),
        post_code=fake_data.postcode()
    )
