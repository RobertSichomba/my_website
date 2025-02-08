from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse

# Skill Model
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency percentage (0-100)"
    )
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome or other icon class")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-proficiency']


# Project Model
class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('planned', 'Planned'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto-generated from title")
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True, help_text="Link to live project or GitHub repository")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills_used = models.ManyToManyField(Skill, related_name='projects', blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags (e.g., Django, Tailwind, Python)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


# Testimonial Model
class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="Author's role or company")
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial by {self.author}"

    class Meta:
        ordering = ['-created_at']


# Blog Post Model
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('web_dev', 'Web Development'),
        ('design', 'Design'),
        ('career', 'Career'),
        ('tutorial', 'Tutorial'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, help_text="Auto-generated from title")
    content = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='web_dev')
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags (e.g., Django, Tailwind, Python)")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']



from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"