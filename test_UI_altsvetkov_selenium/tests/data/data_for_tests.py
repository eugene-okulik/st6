from faker import Faker
fake = Faker()


class CreateAccountData:
    name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = 'qwerty@1#'
