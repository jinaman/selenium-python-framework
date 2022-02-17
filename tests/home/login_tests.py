from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)  #creo un objeto llamado ts (lo instancio)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("namanjuanignacio@gmail.com", "abcabc")
        result1 = self.lp.verifyLoginTitle()                           #ES EL NOMBRE DE LA PESTAÑA
        self.ts.mark(result1, "Title verified")  #Mark no hace ningun assert, solo lleva el tracking de los resultados
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was verified")                 #Markfinal si hace el assert final, solo la uso para el ultimo test case del metodo, y si alguno falla, me fallara el test.

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("namanjuanignacio@gmail.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True