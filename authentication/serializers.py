from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from django.contrib import auth

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["username", "name", "email", "role", "phone_number", "password"]

    def validate_self(attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        name = attrs.get("name", "")
        role = attrs.get("role", "")
        phone_number = attrs.get("role", "")

        if not username.isalnum():
            raise serializers.ValidationError("The username should only contain alphanumeric characters")

        if User.objects.filter(email=email).exists():
            raise serializers.VlidationError({
                "email" : ("Email is already in use")
                })

        return super().validate(attrs)


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    name = serializers.CharField(max_length=255, min_length = 3, read_only=True)
    username = serializers.CharField(max_length=255, min_length = 3, read_only=True)
    password = serializers.CharField(max_length=60, min_length = 6, write_only=True)

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = ["email", "password","username", "name", "tokens"]


    def get_tokens(self, obj):
        user = User.objects.get(email=obj["email"])

        return {
        'refresh' : user.tokens()['refresh'],
        'access' : user.tokens()['access']
        }

    def validate(self, attrs):
        email = attrs.get("email", "")
        password = attrs.get("password", "")
        filtered_user_by_email = User.objects.filter(email= email)

        user = auth.authenticate(email = email, password = password)

        if not user:
            raise AuthenticationFailed("Invalid Credentials, Try again")

        if not user.is_active:
            raise AuthenticationFailed("Account disabled, contact admin")

        return {
            "email": user.email,
            "name": user.name,
            "role": user.role,
            "phone_number": user.phone_number,
            "username": user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
         # "password",
         "id",
         "last_login",
        "is_superuser",
        "first_name",
        "last_name",
        "date_joined",
        "username",
        "name",
        "email",
        "role",
        "phone_number",
        "is_verified",
        "is_active",
        "is_staff",
        "created_at",
        "updated_at",
        "groups",
        "user_permissions"
        ]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        name = attrs.get("name", "")
        phone_number = attrs.get("phone_number", "")
        role = attrs.get("role", "")
        is_staff = attrs.get("is_staff", "")
        is_superuser = attrs.get("is_superuser", "")

        if role == 'supplier' and is_staff == True:
            raise serializers.ValidationError("The Supplier can not be a staff member")

        if role == 'supplier' and is_superuser == True:
            raise serializers.ValidationError("The Supplier can not be a super user")


        return super().validate(attrs)

    # def update(self, validated_data):
    #     return User.objects.create_user(**validated_data)



class UpdateMemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length = 6, read_only=True)

    class Meta:
        model = User
        fields = ["username", "name", "email", "is_superuser", "is_staff"]

    def validate_self(attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        name = attrs.get("name", "")
        phone_number = attrs.get("phone_number", "")
        role = attrs.get("role", "")
        is_staff = attrs.get("is_staff", "")
        is_superuser = attrs.get("is_superuser", "")

        if role == 'supplier' and is_staff == True:
            raise serializers.ValidationError("The Supplier can not be a staff member")

        if role == 'supplier' and is_superuser == True:
            raise serializers.ValidationError("The Supplier can not be a super user")

        # if not username.isalnum():
        #     raise serializers.ValidationError("The username should only contain alphanumeric characters")

        # if User.objects.filter(email=email).exists():
        #     raise serializers.VlidationError({
        #         "email" : ("Email is already in use")
        #         })

        return super().validate(attrs)


    def update(self, validated_data):
        return User.objects.create_user(**validated_data)
