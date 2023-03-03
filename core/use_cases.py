from core.repositories import SymptomRepository, SubstanceRepository


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


class DetailSubstanceUseCase:

    repository = SubstanceRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.get(data["id"])


class DeleteSubstanceUseCase:

    repository = SubstanceRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.delete(data["id"])


class UpdateSubstanceUseCase:

    repository = SubstanceRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.update(data)


class ListSubstanceUseCase:

    repository = SubstanceRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self):
        return self.repository.list()


class CreateSubstanceUseCase:

    repository = SubstanceRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.create(data)
