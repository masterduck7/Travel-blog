from typing import List

from models import Post, Review


def get_all_reviews_of_post_id(id: int) -> List[Review]:
    post = Post.objects.filter(id=id).first()
    return Review.objects.filter(post=post)

def get_all_reviews_of_post_title(title: str) -> List[Review]:
    post = Post.objects.filter(title=title).first()
    return Review.objects.filter(post=post)
