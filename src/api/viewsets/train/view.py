from rest_framework import viewsets, status, mixins
from rest_framework.response import Response


class TrainViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
