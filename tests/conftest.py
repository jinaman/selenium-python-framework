import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)              #Creo una instancia (objeto)
    driver = wdf.getWebDriverInstance()           #getWebDriverInstance() me devuelve el driver que elijo.
    #lp = LoginPage(driver)                     #Creo el objeto del login y
    #lp.login("test@email.com", "abcabc")      #OJO QUE ESTO SE AGREGO AL FINAL DEL CURSO. SI NO ANDA SACARLO.   #Me logueo aca, en el conftest, porque el login no tiene que ver con el test en si. ESTO SE AGREGO AL FINAL, LINEA 17 Y 18. SINO SACARLO Y LOGUEARME EN LOS TESTS.

    if request.cls is not None:
        request.cls.driver = driver               #Para poder usarlo en alguna clase y se lo mando al metodo classSetup de la clase TestClassDemo
    yield driver                                #retorno el driver para poder usarlo en mi test clases y en mis page clases.
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")