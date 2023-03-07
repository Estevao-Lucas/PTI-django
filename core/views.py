from core.mixins import MixinDetailAPIView, MixinCreateAndListAPIView
from core.serializers import (
    SymptomSerializer,
    RetrieverSymptomSerializer,
    RetrieverSubstanceSerializer,
    RetrieverSubCategorySerializer,
    RetrieverPatientSerializer,
    PatientSerializer,
)
from core.use_cases import (
    DetailSymptomUseCase,
    DeleteSymptomUseCase,
    UpdateSymptomUseCase,
    CreateSymptomUseCase,
    ListSymptomUseCase,
    CreateSubstanceUseCase,
    DetailSubstanceUseCase,
    DeleteSubstanceUseCase,
    UpdateSubstanceUseCase,
    ListSubstanceUseCase,
    DeleteSubCategoryUseCase,
    DetailSubCategoryUseCase,
    UpdateSubCategoryUseCase,
    CreateSubCategoryUseCase,
    ListSubCategoryUseCase,
    DeletePatientUseCase,
    DetailPatientUseCase,
    CreatePatientUseCase,
    ListPatientUseCase,
    UpdatePatientUseCase,
)

# Create your views here.


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
