from faker import Faker


fake = Faker()
first_name = 'Name'
last_name = 'Surname'
email = 'test@me.too'
invalid_email = 'testme.too'
password = '159Qwe!textPLM'

first_name_faker = fake.first_name()
last_name_faker = fake.last_name()
email_faker = fake.ascii_free_email()
password_faker = fake.password(length=15, special_chars=True,
                               upper_case=True, lower_case=True)
