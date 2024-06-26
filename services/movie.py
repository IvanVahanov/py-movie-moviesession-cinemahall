from db.models import Movie, Genre, Actor


def get_movies(genres_ids: list[int] = None,
               actors_ids: list[int] = None) -> list[Movie]:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids).distinct()
    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids).distinct()
    return movies


def get_movie_by_id(movie_id: int) -> str:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list[int]
                 = None, actors_ids: list[int] = None) -> list[Movie]:
    movie = Movie.objects.create(title=movie_title,
                                 description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie


if __name__ == "__main__":
    Genre.objects.all()
    Actor.objects.all()
