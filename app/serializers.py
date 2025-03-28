from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Sport, Location, Comment, SportAdvert

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['id', 'name']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'city', 'country']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Read-only to prevent updating user data directly
    sport = SportSerializer(read_only=True)
    sport_id = serializers.PrimaryKeyRelatedField(
        queryset=Sport.objects.all(), source='sport', write_only=True
    )
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), source='location', write_only=True
    )

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'sport', 'sport_id', 'location', 'location_id',
            'bio', 'phone_number', 'specialization', 'certifications',
            'experience_years', 'created_at', 'updated_at'
        ]

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Read-only to prevent user modification
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), source='profile', write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'user', 'profile', 'profile_id', 'text', 'created_at']


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentUser
#         fields = (
#             'username',
#             'email',
#             'role',
#             'password'
#             # 'password2'
#         )

#     def create(self, validated_data):
#         auth_user = StudentUser.objects.create_user(**validated_data)
#         return auth_user

# class SuperUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentUser
#         fields = (
#             'is_superuser',
#         )

# class ActiveUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentUser
#         fields = (
#             'is_active',
#         )

# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentUser
#         fields = (
#             'first_name',
#             'last_name'
#         )
    


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=128)
#     password = serializers.CharField(max_length=128, write_only=True)
#     access = serializers.CharField(read_only=True)
#     refresh = serializers.CharField(read_only=True)
#     role = serializers.CharField(read_only=True)

#     def create(self, validated_date):
#         pass

#     def update(self, instance, validated_data):
#         pass

#     def validate(self, data):
#         username = data['username']
#         password = data['password']
#         user = authenticate(username=username, password=password)

#         if user is None:
#             raise serializers.ValidationError("Invalid login credentials")

#         try:
#             refresh = RefreshToken.for_user(user)
#             refresh_token = str(refresh)
#             access_token = str(refresh.access_token)

#             # update_last_login(None, user)

#             validation = {
#                 'access': access_token,
#                 'refresh': refresh_token,
#                 'username': user.username,
#                 'role': user.role,
#             }

#             return validation
#         except StudentUser.DoesNotExist:
#             raise serializers.ValidationError("Invalid login credentials")

# class UserListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StudentUser
#         fields = (
#             'id',
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'role',
#             'is_active',
#             'is_staff',
#             'is_superuser',
#         )

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'category_name')

# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(), source="user.username",)
#     category = CategorySerializer( read_only=True)

#     class Meta:
#         model = Profile
#         fields = ('id', 'user','profile_photo','category','profile_email','phone_number', 'created_at')
