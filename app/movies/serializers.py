from rest_framework.serializers import ModelSerializer

from movies.models import Movie


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)
