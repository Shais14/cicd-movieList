import random


def generate_review(r):
	review = random.choice(r)
	return review

def generate_movie(m):
	movie = random.choice(m)
	return movie

def generate_movie_review():
	movies = ('Star Wars', 'Lord of the Rings', 'The Dark Knight', 'Troy', 
		'Se7en', 'Guardians of the Galay')
	reviews = (' is a great movie.', ' is an okay movie.', ' is my favorite movie.', ' sucks!')

	movie = generate_movie(movies)
	review = generate_review(reviews)
	return movie + review


if __name__ == "__main__":
	result = generate_movie_review()
	print result
