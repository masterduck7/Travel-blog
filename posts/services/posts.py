from typing import List, Tuple

from posts.models import Post, Review


def get_post_with_reviews(id: int) -> Tuple[Post, List[Review]]:
    post = Post.objects.get(id=id)
    reviews = Review.objects.filter(post=post)
    return (post, reviews)


def get_post_by_id(id: int) -> Post:
    return Post.objects.get(id=id)
