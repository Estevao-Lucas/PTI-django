from core.repositories import SymptomRepository


class DetailSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.get(data["id"])
