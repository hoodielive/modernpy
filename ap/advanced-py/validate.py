def validate(data):
    if data.startswith('_'):
        raise ValueError('Username cannot start with an _')

validate('_larry')

