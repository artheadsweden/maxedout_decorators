def add_to_instance(instance):
    """
    This decorator does not take over a function. Event though it takes an argument
    it will not have nested functions on three levels for this reason.
    The inner function will just return a reference to the original function after
    it has done its work
    :param instance: Instance to add the method to
    :return: Reference to the decorator function
    """

    def decorator(f):
        """
        This function will return a reference to the function decorated after it has
        added the function f as a method to the instance
        :param f: Function to be added as a method to instance
        :return: Reference to the original function
        """
        import types
        f = types.MethodType(f, instance)
        setattr(instance, f.__name__, f)
        return f
    return decorator

def add_to_class(cls):
    def decoratator(f):
        # Investigate the types.MethodType
        setattr(cls, f.__name__ , f)

    return decoratator
