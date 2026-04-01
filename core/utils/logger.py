import logging

class Log:
    """
    Classe centralizada para gerenciamento de logs do sistema.
    Encapsula a biblioteca de logging para facilitar mudanças futuras
    e manter a consistência em todo o projeto.
    """
    
    @staticmethod
    def _get_logger(name: str = None):
        return logging.getLogger(name or "app")

    @classmethod
    def info(cls, message: str, name: str = None):
        cls._get_logger(name).info(message)

    @classmethod
    def warning(cls, message: str, name: str = None):
        cls._get_logger(name).warning(message)

    @classmethod
    def error(cls, message: str, name: str = None, exc_info: bool = False):
        cls._get_logger(name).error(message, exc_info=exc_info)

    @classmethod
    def debug(cls, message: str, name: str = None):
        cls._get_logger(name).debug(message)

    @classmethod
    def critical(cls, message: str, name: str = None, exc_info: bool = True):
        cls._get_logger(name).critical(message, exc_info=exc_info)
