from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FeedSerializer
from .models import Feed


class Feeds(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        # many=True, feeds 객체가 단일 객체이면 many=False(기본값)
        # Feed 모델은 다른 객체도 참조하고 있기 때문에 many=True로 변경 필요. (여러 객체 직렬화)
        # 객체 -> JSON (시리얼라이즈)
        serializer = FeedSerializer(feeds, many=True)
        return Response(serializer.data)


class FeedList(APIView):
    def get(self, request):
        feeds = Feed.objects.all()
        serializer = FeedListSerializer(feeds, many=True)
        return Response(serializer.data)
