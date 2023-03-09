from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    page_query_param = "page"


class MixinDetailAPIView(APIView):
    permission_classes = (AllowAny,)
    detail_use_case = None
    delete_use_case = None
    update_use_case = None
    serializer_class = None

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


class MixinCreateAndListAPIView(APIView, CustomPagination):
    permission_classes = (AllowAny,)
    serializer_class = None
    use_case = None
    retriever_serializer_class = None
    create_instance_use_case = None

    def __init__(
        self,
        serializer=None,
        permission=None,
        use_case=None,
        create_instance_use_case=None,
        retriever_serializer_class=None,
    ):
        self.serializer_class = serializer or self.serializer_class
        self.permission = permission or self.permission_classes
        self.use_case = use_case or self.use_case
        self.create_instance_use_case = (
            create_instance_use_case or self.create_instance_use_case
        )
        self.retriever_serializer_class = (
            retriever_serializer_class or self.retriever_serializer_class
        )

    def get(self, request):
        context = {"request": request}
        serializer = self.serializer_class(data=request.GET.dict(), context=context)

        if not serializer.is_valid():
            return Response(
                {"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        response = self.retriever_serializer_class(
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
        response = self.create_instance_use_case.execute(serializer.data)
        return Response(response, status=status.HTTP_200_OK)
