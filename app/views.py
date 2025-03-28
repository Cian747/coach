from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import CoachRegistrationForm
from django.contrib import messages
from .models import Sport,Profile,SportAdvert,Wishlist,Location
# Create your views here.


def home(request):
    '''
    Show coaches in the area as per their sport choice
    '''
    all_sports = Sport.objects.all()
    all_coaches = Profile.objects.all()

    return render(request,'index.html',{'sports':all_sports, 'coaches':all_coaches})

def register(request):
    """
    Register users
    """
    rgf = CoachRegistrationForm()
    if request.method == 'POST':
        rgf = CoachRegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_user')
    
    return render(request, 'registration/register.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
            

    return render(request, 'registration/login.html')

def profile(request):
    '''
    View all coaches available in your area
    * Future implementation - Coaches in your locations
    '''
    all_coaches = Profile.objects.all()

    return render(request,'profile.html',{'coaches':all_coaches})


def profile_detail(request,id):
    '''
    See more etails about an individual coach
    '''
    coach = Profile.objects.get(id=id)

    context={
        'coach':coach,
    }

    return render(request,'profile/profile-detail.html',context)

def all_coaches(request):
    '''
    * List all of the coaches
    '''
    
    return render(request,'coach.html')


def user_page(request,profile):
    '''
    * The user gets to view the coaches in the area only as per their selection while registering
    * User gets to see the coaches on their wishlist
    * Show sports services available in given sport choice
    '''

def rate_coach(request):
    '''
    * Rate the coach and comment on their service
    '''

def coaches_in_area(request):
    '''
    * See coaches in your/the area 
    * Implement the map feature from google
    '''

def sport_services(request):
    '''
    * Show all sports services
    '''

def comment_on_coach(request, profile):
    '''
    * Make review on service offered by a coach
    '''