# Завдання 1
#  Метаклас, який вносить додаткові перевірки/логіку
# до певних методів у всіх класах.
class ExtraChecksMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if attr_name == "some_method":
                attrs[attr_name] = cls.modify_method(attr_value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def modify_method(method):
        def wrapper(*args, **kwargs):
            print("Додаткова перевірка або логіка перед викликом методу")
            result = method(*args, **kwargs)
            return result
        return wrapper

class MyClass(metaclass=ExtraChecksMeta):
    def some_method(self):
        print("Оригінальний метод")
obj = MyClass()
obj.some_method()
