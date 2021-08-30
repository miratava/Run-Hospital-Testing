class Record():

    def __init__(self, element):
        self.element = element

    def select(self):
        self.element.click()

    def get_text(self):
        return self.element.get_attribute('innerText')




    