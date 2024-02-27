from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"  # Model의 전체 field 가져옴
#         fields = ("nickname", "email")  # 원하는 특정 field만 가져옴
#         exclude = ("password",)  # 특정 field 제외 가능

# (1) 전체 데이터를 다 보여주는 Serialize
# class FeedSerializer(ModelSerializer):
#     class Meta:
#         model = Feed
#         fields = "__all__"

# 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻
# Feed - User 모델 => 현재 코드는 Feed 모델 객체를 직렬화 하고 있지만,
# depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
# depth = 1  # objects도 serialize화 시킴

# (2) 일부 데이터만 보여주는 Serialize
# class FeedListSerializer(ModelSerializer):
#     class Meta:
#         model = Feed
#         fields = ("id", "content", "like")


class FeedSerializer(ModelSerializer):

    user = FeedUserSerializer(read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1


# (2) 일부 데이터만 보여주는 Serialize
class FeedListSerializer(ModelSerializer):

    class Meta:
        model = Feed
        fields = ("id", "user", "title", "content")
