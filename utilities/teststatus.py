"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):    #Hereda de SeleniumDriver class.

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []                        #Creo una lista vacia, la usaremos para trackear los resultados. Al final la vamos a llamar y si falla 1 caso vamos a fallar el test case

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:       #Esto es lo mismo que decir if result is True, solo que no hace falta ponerlo.
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):          #Voy a usar este metodo para TODAS las assertions, es decir, para todos los puntos de verificacion
        """
        Mark the result of the verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):    #Esta la voy a usar para la ULTIMA verificacion
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:                           #Si en mi lista tengo algun FAIL...
            self.log.error(testName +  " ### TEST FAILED")
            self.resultList.clear()
            assert True == False    #Si encuentra un FAIL, luego va a entrar aca donde va a fallar.
        else:
            self.log.info(testName + " ### TEST SUCCESSFUL")
            self.resultList.clear()
            assert True == True