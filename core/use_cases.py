from core.repositories import (
    SymptomRepository,
    SubstanceRepository,
    SubCategoryRepository,
    PatientRepository,
)


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


class CreateSubCategoryUseCase:
    repository = SubCategoryRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.create(data)


class DetailSubCategoryUseCase:
    repository = SubCategoryRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.get(data["id"])


class DeleteSubCategoryUseCase:
    repository = SubCategoryRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.delete(data["id"])


class UpdateSubCategoryUseCase:
    repository = SubCategoryRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.update(data)


class ListSubCategoryUseCase:
    repository = SubCategoryRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self):
        return self.repository.list()


class ListPatientUseCase:
    repository = PatientRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self):
        return self.repository.list()


class CreatePatientUseCase:
    repository = PatientRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.create(data)


class DetailPatientUseCase:
    repository = PatientRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.get(data["id"])


class DeletePatientUseCase:
    repository = PatientRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.delete(data["id"])


class UpdatePatientUseCase:
    repository = PatientRepository()

    def __init__(self, repository=None):
        self.repository = repository or self.repository

    def execute(self, data):
        return self.repository.update(data)
