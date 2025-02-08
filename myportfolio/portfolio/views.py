from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Testimonial, BlogPost

# Home Page View
def home(request):
    featured_projects = Project.objects.filter(status='completed')[:3]  # Show 3 featured projects
    testimonials = Testimonial.objects.filter(is_featured=True)[:5]  # Show 5 featured testimonials
    latest_blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')[:3]  # Show 3 latest blog posts

    context = {
        'featured_projects': featured_projects,
        'testimonials': testimonials,
        'latest_blog_posts': latest_blog_posts,
    }
    return render(request, 'home.html', context)



def about(request):
    context = {
        'linkedin_url': 'https://www.linkedin.com/in/robert-sichomba',
        'pitch_deck_url': 'https://example.com/pitch-deck',
        'contact_url': '/contact',
        'skills': [
            {'name': 'Python', 'proficiency': 90, 'description': 'Experienced with data analysis and web development.'},
            {'name': 'Django', 'proficiency': 85, 'description': 'Proficient in building scalable web applications.'},
            {'name': 'Tailwind CSS', 'proficiency': 80, 'description': 'Skilled in responsive and modern UI design.'},
        ],
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'page_title': 'Contact me on',
        'contact_email': 'sichombarobertbob@gmail.com',
        'phone_number': '+260974609823',
    }
    return render(request, 'contact.html', context)




# Projects Page View
def projects(request):
    all_projects = Project.objects.all().order_by('-created_at')  # Show all projects ordered by creation date
    context = {
        'projects': all_projects,
    }
    return render(request, 'projects.html', context)


# Project Detail View
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)


# Blog Page View
def blog(request):
    all_blog_posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')  # Show all published blog posts
    context = {
        'blog_posts': all_blog_posts,
    }
    return render(request, 'blog.html', context)


# Blog Post Detail View
def blog_detail(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    context = {
        'blog_post': blog_post,
    }
    return render(request, 'blog_detail.html', context)


# Testimonials Page View
def testimonials(request):
    all_testimonials = Testimonial.objects.all().order_by('-created_at')  # Show all testimonials ordered by creation date
    context = {
        'testimonials': all_testimonials,
    }
    return render(request, 'testimonials.html', context)


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email
        send_mail(
            f"New Contact Form Submission: {subject}",
            f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return render(request, 'contact.html')










def terms(request):
    return render(request, 'terms.html')






def privacy(request):
    return render(request, 'privacy.html')