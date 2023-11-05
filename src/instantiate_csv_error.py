class InstantiateCSVError(Exception):
    """Класс - исключение"""
    def __init__(self, message='Файл поврежден', *args):
        super().__init__(message, *args)


class InstError:
    def __init__(self, field_name):
        if len(field_name) != 3:
            raise InstantiateCSVError
        else:
            self.field_name = field_name
