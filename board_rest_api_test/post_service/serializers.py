from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # ModelSerializer 를 이용해서 아래와 같이 짧은 코드로 직렬화 필드를 정의할 수 있다
    class Meta:
        model = Post
        fields = ('title','body','author','regdate')

    # 신규 Bbs instance를 생성해서 리턴해준다
    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    # 생성되어 있는 Bbs instance 를 저장한 후 리턴해준다
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.regdate = validated_data.get('regdate', instance.regdate)
        instance.save()
        return instance