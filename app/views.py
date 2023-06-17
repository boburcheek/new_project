from django.shortcuts import render
from .models import ProfileData, Tool, SocialLink, About, Service, Category, Projects, Post
from django.views import generic


def home(request):
    profile = ProfileData.objects.first()
    tools = Tool.objects.all().order_by("order")
    social_links = SocialLink.objects.all().order_by('order')
    about = About.objects.last()
    services = Service.objects.all().order_by('order')
    categories = Category.objects.all()
    projects = Projects.objects.all()[:4]
    posts = Post.objects.all()[:4]
    contex = {
        "profile": profile,
        "tools": tools,
        "social_links": social_links,
        "about": about,
        "services": services,
        "categories": categories,
        "projects": projects,
        "posts": posts
    }
    return render(request, "index.html", contex)


def about(request):
    about = About.objects.last()
    tools = Tool.objects.all().order_by("order")

    context = {
        "about": about,
        "tools": tools
    }
    return render(request, "about-us.html", context)


def portfolio(request):
    categories = Category.objects.all()
    projects = Projects.objects.all()

    context = {
        "categories": categories,
        "projects": projects
    }
    return render(request, "portfolio.html", context)


class PostListView(generic.ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        popular_posts = Post.objects.all().order_by("-views_count")[:4]
        context['popular_posts'] = popular_posts
        social_links = SocialLink.objects.all().order_by("order")
        context['social_links'] = social_links
        profile_data = ProfileData.objects.first()
        context['profile_data'] = profile_data
        return context

    def get_queryset(self):
        search = self.request.GET.get("search", "")
        queryset = super().get_queryset()

        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "single-blog.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        social_links = SocialLink.objects.all().order_by("order")
        context['links'] = social_links
        profile_data = ProfileData.objects.first()
        context.update({"profile_data": profile_data})
        popular_post = Post.objects.all().order_by("-views_count")[:4]
        context.update({"profile_data": profile_data,
                        "most_watched_posts": popular_post})
        return context
