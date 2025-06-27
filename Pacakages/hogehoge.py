
class A:

    def __init__(self):
        self.value = 42

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def increment_value(self):
        self.value += 1

    def reset_value(self):
        self.value = 0

class B():

    def __init__(self):
        self.value = 100

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def double_value(self):
        self.value *= 2

    def reset_value(self):
        self.value = 0