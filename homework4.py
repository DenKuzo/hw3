class Class1:

    def __init__(self, name):
        self.name = name


class Class2:

    def __init__(self, age):
        self.age = age


class Class3(Class1):

    def display_name(self):
        print(f'{self.name} is name')


class Class4(Class2):

    def display_info(self):
        print(f" Age: {self.age}")


class Class5(Class4, Class3, Class2, Class1):

    def __init__(self, name, age):
        super().__init__(name)

        self.age = age

    def display_all(self):
        self.display_name()

    def display_age(self):
        self.display_age()
