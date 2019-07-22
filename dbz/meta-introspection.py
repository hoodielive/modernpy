def randomCall(obj):
    all_attrs = [
        getattr(obj, attr_name)
        for attr_name in dir(obj)]

    all_methods = [
        attr for attr in all_attrs if callable(attr) ]

    some_method = random.choice(all_methods)
    some_method()