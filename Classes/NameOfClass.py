from Classes.Exceptions import InvalidClassNameType, ClassAlreadyExists, ClassDoesNotExist


class NameOfClass:
    className = []

    @classmethod
    def add_class(cls, classname: str):
        if not isinstance(classname, str):
            raise InvalidClassNameType("Nazwa klasy musi być w formie tekstu")
        if classname in cls.className:
            raise ClassAlreadyExists(f"Klasa '{classname}' już istnieje")
        cls.className.append(classname)

    @classmethod
    def del_class(cls, classname: str):
        if not isinstance(classname, str):
            raise InvalidClassNameType("Nazwa klasy musi być w formie tekstu")
        if classname not in cls.className:
            raise ClassDoesNotExist("Klasa '{classname}' nie istnieje")
        cls.className.remove(classname)

    @classmethod
    def show_class_names(cls):
        return cls.className
