# Завдання 3
#  Створіть метаклас, який автоматично додає певні
# атрибути до всіх класів, що використовують його.

class AutoAttributeMeta(type):
    def __init__(cls, name, bases, attrs):
        cls.new_attribute = "This is a new attribute added automatically"
        super().__init__(name, bases, attrs)
class MyClass(metaclass=AutoAttributeMeta):
    pass
print(MyClass.new_attribute)  # Виведе: This is a new attribute added automatically



