from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from datetime import datetime, date
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['iat'] = datetime.now()
        token['username'] = user.username
        token['user_id'] = user.id
        token['date'] = str(date.today())

        return token