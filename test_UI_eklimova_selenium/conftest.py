


@pytest.fixture()
def create_new_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendlyPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture
def creds():
    with open('creds.json') as f:
        return json.load(f)
