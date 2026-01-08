import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogpro.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

def populate():
    # Create Users
    user1, created = User.objects.get_or_create(username='geopolitico')
    if created:
        user1.set_password('password123')
        user1.save()
        print(f"Created user: {user1.username}")

    user2, created = User.objects.get_or_create(username='stratfor_fan')
    if created:
        user2.set_password('password123')
        user2.save()
        print(f"Created user: {user2.username}")

    # Create Posts
    posts = [
        {
            'title': 'The New Great Game: Arctic Dominance',
            'content': 'As ice caps melt, the Arctic becomes the new frontier for resource extraction and strategic positioning. Nations are scrambling to assert their sovereignty over these icy waters.',
            'author': user1
        },
        {
            'title': 'Energy Security in 2026: Beyond Oil',
            'content': 'The shift to rare earth minerals for battery production has created new dependencies. Who controls the supply chains for lithium and cobalt now controls the future of energy.',
            'author': user2
        },
        {
            'title': 'The Return of Multipolarity',
            'content': 'The era of a single superpower is fading. We are entering a complex web of regional alliances and competing power blocs that requires a nuance approach to diplomacy.',
            'author': user1
        },
        {
            'title': 'Cyber Warfare: The Invisible Front',
            'content': 'State-sponsored cyber attacks are no longer just about espionage; they are about disrupting critical infrastructure and sowing discord in rival nations.',
            'author': user2
        },
        {
            'title': 'Water Wars: The Next Conflict?',
            'content': 'With freshwater resources becoming scarcer, downstream nations are increasingly at odds with upstream dam builders. The Nile and Mekong basins are flashpoints to watch.',
            'author': user1
        }
    ]

    for post_data in posts:
        post = Post.objects.create(
            title=post_data['title'],
            content=post_data['content'],
            author=post_data['author'],
            date_posted=timezone.now()
        )
        print(f"Created post: {post.title}")

if __name__ == '__main__':
    print("Populating database...")
    populate()
    print("Done!")
