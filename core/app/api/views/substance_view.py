from core.domain.use_cases.substance import *
from core.app.api.views.mixins import *
from core.app.api.serializers import RetrieverSubstanceSerializer


class SubstanceAPIView(MixinDetailAPIView):
    serializer_class = RetrieverSubstanceSerializer
    detail_use_case = DetailSubstanceUseCase()
    delete_use_case = DeleteSubstanceUseCase()
    update_use_case = UpdateSubstanceUseCase()


class SubstancesAPIView(MixinCreateAndListAPIView):
    serializer_class = RetrieverSubstanceSerializer
    retriever_serializer_class = RetrieverSubstanceSerializer
    use_case = ListSubstanceUseCase()
    create_instance_use_case = CreateSubstanceUseCase()
