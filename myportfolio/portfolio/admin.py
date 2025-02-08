from django.contrib import admin
from .models import Skill, Project, Testimonial, BlogPost

# Skill Admin
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'icon')  # Columns to display in the admin list view
    list_filter = ('proficiency',)  # Add filters for proficiency
    search_fields = ('name', 'description')  # Add search functionality
    ordering = ('-proficiency',)  # Default ordering

admin.site.register(Skill, SkillAdmin)


# Project Admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('status', 'created_at')  # Add filters for status and creation date
    search_fields = ('title', 'description', 'tags')  # Add search functionality
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
    filter_horizontal = ('skills_used',)  # Better UI for many-to-many fields
    date_hierarchy = 'created_at'  # Add a date hierarchy navigation

admin.site.register(Project, ProjectAdmin)


# Testimonial Admin
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'role', 'is_featured', 'created_at')  # Columns to display
    list_filter = ('is_featured', 'created_at')  # Add filters for featured testimonials
    search_fields = ('author', 'role', 'content')  # Add search functionality
    list_editable = ('is_featured',)  # Allow editing 'is_featured' directly from the list view

admin.site.register(Testimonial, TestimonialAdmin)


# Blog Post Admin
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('category', 'is_published', 'created_at')  # Add filters for category and publication status
    search_fields = ('title', 'content', 'tags')  # Add search functionality
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from title
    list_editable = ('is_published',)  # Allow editing 'is_published' directly from the list view
    date_hierarchy = 'created_at'  # Add a date hierarchy navigation

admin.site.register(BlogPost, BlogPostAdmin)