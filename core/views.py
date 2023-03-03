from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from core.serializers import (
    SymptomSerializer,
    RetrieverSymptomSerializer,
    RetrieverSubstanceSerializer,
    RetrieverSubCategorySerializer,
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
)

# Create your views here.


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    page_query_param = "page"


class SymptomAPIView(APIView):
    permission_classes = (AllowAny,)
    detail_use_case = DetailSymptomUseCase()
    delete_use_case = DeleteSymptomUseCase()
    update_use_case = UpdateSymptomUseCase()
    serializer_class = RetrieverSymptomSerializer

    def __init__(
        self,
        detail_use_case=None,
        delete_use_case=None,
        update_use_case=None,
        serializer=None,
        permission=None,
    ):
        self.detail_use_case = detail_use_case or self.detail_use_case
        self.delete_use_case = delete_use_case or self.delete_use_case
        self.update_use_case = update_use_case or self.update_use_case
        self.serializer_class = serializer or self.serializer_class
        self.permission = permission or self.permission_classes

    def get(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.detail_use_case.execute(serializer.data), context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.delete_use_case.execute(serializer.data)

        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id):
        body = request.data.copy()
        body["id"] = id
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.update_use_case.execute(serializer.data), context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class SymptomsAPIView(APIView, CustomPagination):
    permission_classes = (AllowAny,)
    serializer_class = RetrieverSymptomSerializer
    use_case = ListSymptomUseCase()
    create_symptom_use_case = CreateSymptomUseCase()

    def __init__(
        self,
        serializer=None,
        permission=None,
        use_case=None,
        create_symptom_use_case=None,
    ):
        self.serializer_class = serializer or self.serializer_class
        self.permission = permission or self.permission_classes
        self.use_case = use_case or self.use_case
        self.create_symptom_use_case = (
            create_symptom_use_case or self.create_symptom_use_case
        )

    def get(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.GET.dict(), context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = SymptomSerializer(
            self.paginate_queryset(self.use_case.execute(), request, view=self),
            many=True,
            context=context,
        ).data

        return self.get_paginated_response(response)

    def post(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.data, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        response = self.create_symptom_use_case.execute(serializer.data)
        return Response(response, status=status.HTTP_200_OK)


class SubstanceAPIView(APIView):
    serializer_class = RetrieverSubstanceSerializer
    detail_use_case = DetailSubstanceUseCase()
    delete_use_case = DeleteSubstanceUseCase()
    update_use_case = UpdateSubstanceUseCase()

    def __init__(
        self,
        detail_use_case=None,
        delete_use_case=None,
        update_use_case=None,
        serializer_class=None,
    ):
        self.detail_use_case = detail_use_case or self.detail_use_case
        self.delete_use_case = delete_use_case or self.delete_use_case
        self.update_use_case = update_use_case or self.update_use_case
        self.serializer_class = serializer_class or self.serializer_class

    def get(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.detail_use_case.execute(serializer.data), context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.delete_use_case.execute(serializer.data)

        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id):
        body = request.data.copy()
        body["id"] = id
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.update_use_case.execute(serializer.data), context=context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubstancesAPIView(APIView, CustomPagination):
    permission_classes = (AllowAny,)
    serializer_class = RetrieverSubstanceSerializer
    use_case = ListSubstanceUseCase()
    create_substance_use_case = CreateSubstanceUseCase()

    def __init__(
        self,
        serializer_class=None,
        use_case=None,
        create_substance_use_case=None,
        permission=None,
    ):
        self.serializer_class = serializer_class or self.serializer_class
        self.use_case = use_case or self.use_case
        self.create_substance_use_case = (
            create_substance_use_case or self.create_substance_use_case
        )
        self.permission = permission or self.permission_classes

    def get(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.GET.dict(), context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.serializer_class(
            self.paginate_queryset(self.use_case.execute(), request, view=self),
            many=True,
            context=context,
        ).data

        return self.get_paginated_response(response)

    def post(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.data, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        response = self.create_substance_use_case.execute(serializer.data)
        return Response(response, status=status.HTTP_200_OK)


class SubCategoryAPIView(APIView):
    serializer_class = RetrieverSubCategorySerializer
    detail_use_case = DetailSubCategoryUseCase()
    delete_use_case = DeleteSubCategoryUseCase()
    update_use_case = UpdateSubCategoryUseCase()
    permission_classes = (AllowAny,)

    def __init__(
        self,
        update_use_case=None,
        delete_use_case=None,
        detail_use_case=None,
        serializer_class=None,
        permission=None,
    ):
        self.update_use_case = update_use_case or self.update_use_case
        self.delete_use_case = delete_use_case or self.delete_use_case
        self.detail_use_case = detail_use_case or self.detail_use_case
        self.serializer_class = serializer_class or self.serializer_class
        self.permission = permission or self.permission_classes

    def get(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.detail_use_case.execute(serializer.data), context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        body = {**request.GET.dict(), "id": id}
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.delete_use_case.execute(serializer.data)

        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id):
        body = request.data.copy()
        body["id"] = id
        context = {"request": request}
        serializer = self.serializer_class(data=body, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.update_use_case.execute(serializer.data), context=context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoriesAPIView(APIView, CustomPagination):
    serializer_class = RetrieverSubCategorySerializer
    permission_classes = (AllowAny,)
    create_sub_category_use_case = CreateSubCategoryUseCase()
    use_case = ListSubCategoryUseCase()

    def __init__(
        self,
        serializer_class=None,
        permission=None,
        create_sub_category_use_case=None,
        use_case=None,
    ):
        self.serializer_class = serializer_class or self.serializer_class
        self.permission = permission or self.permission_classes
        self.create_sub_category_use_case = (
            create_sub_category_use_case or self.create_sub_category_use_case
        )
        self.use_case = use_case or self.use_case

    def get(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.GET.dict(), context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.serializer_class(
            self.paginate_queryset(self.use_case.execute(), request, view=self),
            many=True,
            context=context,
        ).data

        return self.get_paginated_response(response)

    def post(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.data, context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
        response = self.create_sub_category_use_case.execute(serializer.data)
        return Response(response, status=status.HTTP_200_OK)
