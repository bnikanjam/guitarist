from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializers import MovieSerializer


class MovieListView(APIView):
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        movies = Movie.objects.all()
        # Pass the many=True flag when a nested representation should be a list of items.
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    def get_object(self, pk):
        try :
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        movie = self.get_object(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
