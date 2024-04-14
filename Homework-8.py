# Завдання 2
#  Метаклас, що може змінювати ім'я класу залежно
# від певних умов або параметрів.
class DynamicClassNameMeta(type):
    def __new__(cls, name, bases, attrs):
        if "dynamic_name" in attrs:
            new_name = attrs["dynamic_name"]
            del attrs["dynamic_name"]
            return super().__new__(cls, new_name, bases, attrs)
        else:
            return super().__new__(cls, name, bases, attrs)
class MyClass(metaclass=DynamicClassNameMeta):
    dynamic_name = "NewClassName"
print(MyClass.__name__)  # Виведе: NewClassName

