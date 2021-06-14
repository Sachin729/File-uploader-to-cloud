from abc import ABC, abstractmethod


class Cloud_operations(ABC):
    """Abstract class Cloud opertation, To add new cloud platform two abstract methods should be defined in derived classes"""

    @abstractmethod
    def validate_login_credentials(self):
        pass

    @abstractmethod
    def upload_files(self, list_of_files):
        pass
