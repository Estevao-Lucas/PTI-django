from abc import ABC, abstractmethod


class ABCRepository(ABC):
    """Abstract base class for all repositories."""

    @abstractmethod
    def create(self, data):
        """Creates a new instance of the domain object.

        Args:
            data: dict. A dictionary containing all fields required to create
        """
        pass

    @abstractmethod
    def get(self, id):
        """Returns an instance of the domain object with the given id.

        Args:
            entity_id: str. The id of the domain object.

        Returns:
            *. The domain object with the given id.
        """
        pass

    @abstractmethod
    def update(self, data):
        """Updates an instance of the domain object and returns the updated

        Args:
            data: dict. A dictionary containing all fields required to update

        Returns:
            *. The updated domain object.
        """
        pass

    @abstractmethod
    def delete(self, id):
        """Deletes an instance of the domain object from the datastore.

        Args:
            entity_id: str. The id of the domain object to be deleted.
        """
        pass

    @abstractmethod
    def list(self):
        """Returns all instances of the domain object.

        Returns:
            list(*). All domain objects of the given type.
        """
        pass
