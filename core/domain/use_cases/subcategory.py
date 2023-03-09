from core.data.repositories.subcategory import SubCategoryRepository


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
