from typing import List

from models import Post


def get_all_posts() -> List[Post]:
    return Post.objects.all()

def get_post_by_id(id: int) -> Post:
    return Post.objects.filter(id=id).first()

def get_post_by_title(title: str) -> Post:
    return Post.objects.filter(title=title).first()
