from rest_framework import serializers

from users.models import CustomUser


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "phone_number",
            "city",
            "avatar",
            "tg_chat_id",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    tg_chat_id = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password", "tg_chat_id")

    def create(
        self, validated_data
    ):  # if we won't use create method password won't be saved using salt
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            tg_chat_id=validated_data.get("tg_chat_id", None),
        )
        return user
