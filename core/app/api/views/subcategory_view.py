from core.domain.use_cases.subcategory import *
from core.app.api.views.mixins import *
from core.app.api.serializers import RetrieverSubCategorySerializer


class SubCategoryAPIView(MixinDetailAPIView):
    serializer_class = RetrieverSubCategorySerializer
    detail_use_case = DetailSubCategoryUseCase()
    delete_use_case = DeleteSubCategoryUseCase()
    update_use_case = UpdateSubCategoryUseCase()


class SubCategoriesAPIView(MixinCreateAndListAPIView):
    serializer_class = RetrieverSubCategorySerializer
    retriever_serializer_class = RetrieverSubCategorySerializer
    create_instance_use_case = CreateSubCategoryUseCase()
    use_case = ListSubCategoryUseCase()
