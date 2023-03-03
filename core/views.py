from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.serializers import SymptomSerializer
from core.use_cases import (
    DetailSymptomUseCase,
    DeleteSymptomUseCase,
    UpdateSymptomUseCase,
)

# Create your views here.
class SymptomsAPIView(APIView):
    permission_classes = (AllowAny,)
    detail_use_case = DetailSymptomUseCase()
    delete_use_case = DeleteSymptomUseCase()
    update_use_case = UpdateSymptomUseCase()
    serializer_class = SymptomSerializer

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
            print(serializer.data)
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(
            self.update_use_case.execute(serializer.data), context=context
        )

        return Response(serializer.data, status=status.HTTP_200_OK)
