from core.domain.use_cases.symptom import *
from core.app.api.views.mixins import *
from core.app.api.serializers import RetrieverSymptomSerializer, SymptomSerializer


class SymptomAPIView(MixinDetailAPIView):
    detail_use_case = DetailSymptomUseCase()
    delete_use_case = DeleteSymptomUseCase()
    update_use_case = UpdateSymptomUseCase()
    serializer_class = RetrieverSymptomSerializer


class SymptomsAPIView(MixinCreateAndListAPIView):
    serializer_class = RetrieverSymptomSerializer
    use_case = ListSymptomUseCase()
    create_instance_use_case = CreateSymptomUseCase()
    retriever_serializer_class = SymptomSerializer
