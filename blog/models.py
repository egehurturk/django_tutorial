from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField() # Text field is similar to charfield, but unrestricted text
    date_posted = models.DateTimeField(default=timezone.now) # You can't ever update the datetime created field with auto_add=True.
    author = models.ForeignKey(User,  on_delete=models.CASCADE) # If a user is deleted, then delete its posts.

    def __str__(self):
        return self.title


# Se exact SQL Code: python manage.py sqlmigrate blog 0001
# ORM helps us to write SQL code without even writing it.
# Migrations are useful because it allows to make changes to our database without even writing SQL update code.
# Open Django Shell: python manage.py shell
# ORM Queries:
#     `User.objects.all()` returns all the users
#     `User.objects.first()/.last()` returns first/last users
#     `User.objects.filter(username='EgeH')` returns the specified filter
#     `user = User.objects.filter(username='EgeH').first()` returns 'EgeH'.
#     We can access User attributes:
#         `user.id`
#         `user.pk ` (Primary Key)
#    `User.objects.get(id=1)` queries the User with ID 1.
#    `Post(title='First Post', content='First Blog Post content', author=user)` will create a new Post.
#    When we create a post object, we should save to database using `post_1.save()`
# To Create a nice representation of our Object, we should define a `__str__()` method.
# We can access the ForeignKey Classes's fields with the associated class:
#    `post.author.email` -> 'ege@hurturk.com'
# We've deleted the dummy data, and instead queired the posts from our database.
# We've applied filters in our home template page.
# We've registered our Post model to the admin page:
#    `admin.site.register(Post)`