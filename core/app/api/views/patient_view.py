from core.domain.use_cases.patient import *
from core.app.api.views.mixins import *
from core.app.api.serializers import RetrieverPatientSerializer, PatientSerializer


class PatientAPIView(MixinDetailAPIView):
    serializer_class = RetrieverPatientSerializer
    detail_use_case = DetailPatientUseCase()
    delete_use_case = DeletePatientUseCase()
    update_use_case = UpdatePatientUseCase()


class PatientsAPIView(MixinCreateAndListAPIView):
    serializer_class = RetrieverPatientSerializer
    retriever_serializer_class = PatientSerializer
    create_instance_use_case = CreatePatientUseCase()
    use_case = ListPatientUseCase()
