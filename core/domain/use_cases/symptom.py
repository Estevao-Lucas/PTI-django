from core.data.repositories.symptom import SymptomRepository


class DetailSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.get(data["id"])


class DeleteSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.delete(data["id"])


class UpdateSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.update(data)


class ListSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self):
        return self.repository.list()


class CreateSymptomUseCase:
    repository = SymptomRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.create(data)
