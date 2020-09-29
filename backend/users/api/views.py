from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from backend.users.api.serializers import UserSerializer
from backend.users.permissions import IsOwner

from backend.song.api.serializers import (
    TranslationSerializer,
    LyricSerializer,
    LyricRequestSerializer
)
from backend.song.models import (
    Translation,
    Lyric,
    LyricRequest
)

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=HTTP_200_OK, data=serializer.data)


class UserTranslationsView(ListModelMixin, GenericViewSet):

    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserLyricsView(ListModelMixin, GenericViewSet):

    serializer_class = LyricSerializer
    queryset = Lyric.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserLyricRequestView(ListModelMixin, GenericViewSet):

    serializer_class = LyricRequestSerializer
    queryset = LyricRequest.objects.all()
    lookup_field = "username"
    permission_classes = [IsAuthenticated, IsOwner, ]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
