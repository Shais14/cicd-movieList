import unittest

from movies import generator

def test_sample_single_movie():
    l = ('foo', 'bar')
    word = generator.generate_movie(l)
    assert word in l

def test_sample_single_review():
    l = ('foo', 'bar')
    word = generator.generate_review(l)
    assert word in l

# def test_sample_movie_review():
#     lm = ('foo', 'bar')
#     lr = (' foo', 'bar')
#     words = generator.generate_movie(lm) + generator.generate_review(lr)
#     assert words[0] in lm
#     assert words[1] in lr
