

class NameOfClass:
    className = []
    @classmethod
    def add_class(cls, classname): #hintery i wyjątek jak zły typ lub jak już istnieje
        cls.className.append(classname)

    @classmethod
    def del_class(cls, classname): #hintery i wyjątek jak zły typ albo nie instnieje
        cls.className.remove(classname)

    @classmethod
    def show_class_names(cls):
        return cls.className
