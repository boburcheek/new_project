from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProfileData(BaseModel):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post/")
    body = models.TextField()

    def __str__(self):
        return self.full_name


class SocialLink(BaseModel):
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.CharField(max_length=55)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.name


class Tool(BaseModel):
    skill = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.skill} - {self.percentage}"


class About(BaseModel):
    text = models.TextField()
    donation = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    volunteers = models.PositiveIntegerField()

    def __str__(self):
        return self.donation


class Service(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="service/")
    order = models.PositiveIntegerField()


class Meta:
    ordering = ("order",)


def __str__(self):
    return self.title


class Post(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="post/")
    body = models.TextField()
    views_count = models.IntegerField()

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def str(self):
        return self.name


class Projects(BaseModel):
    name = models.CharField(max_length=255)
    link = models.URLField()
    desciption = models.TextField()
    used_tools = models.ManyToManyField(Tool)
    categories = models.ManyToManyField(Category)

    def str(self):
        return self.name