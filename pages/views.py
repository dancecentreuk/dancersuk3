from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from courses.models import WeeklyDanceClass, Level, DanceStyle
from users.models import Profile, DancersProfile, Account, DancerImage
from jobs.models import Listing
from blog.models import BlogPost
from datetime import date
from django.utils.timezone import now
from .choices import location_choices, age_choices, gender_choices
from jobs.models import Category
from venues.models import Venue


class HomeView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'courses'
    model = WeeklyDanceClass
    paginate_by = 6



    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['styles'] = DanceStyle.objects.all()
        context['courses'] = WeeklyDanceClass.objects.all()[:4]
        context['levels'] = Level.objects.all()
        context['location_choices'] = location_choices
        context['age_choices'] = age_choices
        context['talents'] = DancersProfile.objects.order_by("-pk")[:6]
        context['all_jobs'] = Listing.objects.order_by('-pk')[:4]
        context['listings'] = Listing.objects.filter(is_posting=True).order_by('-pk')
        context['postings'] = Listing.objects.filter(is_posting=False).order_by('date')
        context['all_jobs_count'] = Listing.objects.all().count()
        context['blogposts'] = BlogPost.objects.filter(featured=True)
        context['classes_count'] = WeeklyDanceClass.objects.all().count()
        context['job_categories'] = Category.objects.all()
        return context


# def age_range(min_age, max_age):
#     current = now().date()
#     min_date = date(current.year - min_age, current.month, current.day)
#     max_date = date(current.year - max_age, current.month, current.day)
#
#     return user_profiles.filter(birthdate__gte=max_date,
#                                 birthdate__lte=min_date).order_by("birthdate")


class TalentListView(ListView):
    template_name = 'pages/talent.html'
    context_object_name = 'talents'
    model = DancersProfile
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super(TalentListView, self).get_context_data(**kwargs)
        context['location_choices'] = location_choices
        context['age_choices'] = age_choices
        context['gender_choices'] = gender_choices
        context['all_talent'] = DancersProfile.objects.filter(is_active=True).count()
        return context

class TalentDetailView(DetailView):
    template_name = 'pages/talent-detail.html'
    model = DancersProfile
    context_object_name = 'talent'


    def get_context_data(self, **kwargs):
        context = super(TalentDetailView, self).get_context_data(**kwargs)
        dance_profile = get_object_or_404(DancersProfile, pk=self.kwargs['pk'])
        author = dance_profile.user.id
        context['courses'] = WeeklyDanceClass.objects.filter(author_id=author)
        context['images'] = DancerImage.objects.filter(owner=dance_profile)
        return context


class ProfileInfoView(DetailView):
    template_name = 'pages/profile-info.html'
    model = Profile
    context_object_name = 'profile'


    def get_context_data(self, **kwargs):
        context = super(ProfileInfoView, self).get_context_data(**kwargs)
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        user = profile.user.id
        context['listings'] = Listing.objects.filter(author_id=user)
        context['courses'] = WeeklyDanceClass.objects.filter(author_id=user)
        context['venues'] = Venue.objects.filter(author_id=user)
        context['blogs'] = BlogPost.objects.all()[:3]
        return context



def searchTalent(request):

    queryset_list = DancersProfile.objects.all()


    if 'first_name' in request.GET:
        first_name = request.GET['first_name']
        if first_name:
            queryset_list = queryset_list.filter(user__first_name__icontains=first_name)


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            queryset_list = queryset_list.filter(bio__icontains=keyword)


    if 'gender' in request.GET:
        gender = request.GET['gender']
        if gender:
            queryset_list = queryset_list.filter(user__profile__gender=gender)



    if 'talent_location' in request.GET:
        location = request.GET['talent_location']
        if location:
            queryset_list = queryset_list.filter(user__profile__location=location)


    paginator = Paginator(queryset_list, 2)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'talents': paged_listings,
        'gender_choices': gender_choices,
        'location_choices':location_choices,
        'age_choices': age_choices,
        'values': request.GET

    }

    return render(request, 'pages/talent-search.html', context)
