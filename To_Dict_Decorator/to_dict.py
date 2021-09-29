def to_dict(attributes):
    def wrapper(cls):
        def to_dict(self):
            result_dict = {}
            for a in attributes:
                if a not in self.__dict__:
                    raise ValueError(f"{a} not a member of the object {self}")
                # check if attribut is an iterable...
                try:
                    _ = iter(self.__dict__[a])
                    if getattr(self.__dict__[a]):
                        result_dict[a] = [item.to_dict() for item in self.__dict__[a]]
                except TypeError:
                    # Not an iterable
                    result_dict[a] = self.__dict__[a]
            return result_dict
        cls.to_dict = to_dict
        return cls
    return wrapper