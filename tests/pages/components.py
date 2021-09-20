class Record():

    def __init__(self, element):
        self.element = element

    def select(self):
        self.element.click()
        return

    def get_text(self):
        return self.element.get_attribute('innerText')




    