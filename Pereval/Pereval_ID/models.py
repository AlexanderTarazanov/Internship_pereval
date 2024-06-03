from django.db import models


class Users(models.Model):
    fam = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    otc = models.CharField(max_length=255, verbose_name='Отчество')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255, verbose_name='E-mail')

    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    def __str__(self):
        return f"{self.fam} {self.name} {self.otc}"


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name="Широта", blank=True, null=True)
    longitude = models.FloatField(max_length=50, verbose_name="Долгота", blank=True, null=True)
    height = models.IntegerField(verbose_name="Высота", blank=True, null=True)

    def __str__(self):
        return f"широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}"

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Зима', blank=True, null=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', blank=True, null=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', blank=True, null=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', blank=True, null=True)

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровни сложности"

    def __str__(self):
        return f"зима: {self.winter}, весна: {self.spring}, лето: {self.summer}, осень: {self.autumn}"


class pereval_added(models.Model):
    new = "new"
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    STATUS = [
        (new, "новый"),
        (pending, "модератор взял в работу"),
        (accepted, "модерация прошла успешно"),
        (rejected, "модерация прошла, информация не принята"),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name="Название препятствия", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Название вершины", blank=True, null=True)
    other_titles = models.CharField(max_length=255, verbose_name="Другое название", blank=True, null=True)
    connect = models.TextField(blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.ForeignKey('Coords', on_delete=models.CASCADE, blank=True, null=True)
    tourist_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="tourist_id")
    status = models.CharField(max_length=10, choices=STATUS, default=new)
    level = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"

    def __str__(self):
        return f"{self.pk}: {self.beauty_title}"


class Images(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=255)
    pereval_id = models.ForeignKey(pereval_added, on_delete=models.CASCADE, related_name='images', blank=True,
                                   null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображение"

    def __str__(self):
        return f"{self.pk}: {self.title}"
