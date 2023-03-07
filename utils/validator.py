def validate_arguments(**kwargs):
    for key, value in kwargs.items():
        if not value:
            raise ValueError(f'{key} value is empty. After rewriting, please press the "submit" button.')
