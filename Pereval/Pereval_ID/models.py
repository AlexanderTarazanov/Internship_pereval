from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)


class pereval_added(models.Model):
    STATUS_CHOICES = (
        ('new', 'новый'),
        ('pending', 'в работе'),
        ('accepted', 'принято'),
        ('rejected', 'отклонено'),
    )

    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField('Coords', on_delete=models.CASCADE)
    tourist_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    level = models.ForeignKey('Level', on_delete=models.CASCADE)


class Coords(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    height = models.IntegerField(default=0)


class Level(models.Model):
    LEVEL_CHOICES = (
        ('1A', '1A'),
        ('2A', '2A'),
        ('3A', '3A'),
        ('4A', '4A'),
    )
    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default='1A')


class Images(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=255)
    pereval_id = models.ForeignKey(pereval_added, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title