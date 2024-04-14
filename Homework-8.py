# Завдання 4
# Метаклас, що додає перевірку та обробку аргументів
# __init__ у всіх класах.
class ArgumentProcessingMeta(type):
    def __init__(cls, name, bases, attrs):
        original_init = getattr(cls, '__init__', None)

        def new_init(self, *args, **kwargs):
            if original_init:

                processed_args = tuple(arg.upper() if isinstance(arg, str) else arg for arg in args)
                processed_kwargs = {key: value.upper() if isinstance(value, str) else value for key, value in
                                    kwargs.items()}
                original_init(self, *processed_args, **processed_kwargs)
        cls.__init__ = new_init

        super().__init__(name, bases, attrs)

class MyClass(metaclass=ArgumentProcessingMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass("John", 30)
print(obj.name)
print(obj.age)



