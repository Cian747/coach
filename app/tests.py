from django.test import TestCase
from .models import Profile,Sport,Location,SportAdvert,Comment,Wishlist
from django.contrib.auth.models import User

# Create your tests here.

class CoachTestCase(TestCase):
    '''
    Test coach app model functionality
    '''
    def setUp(self):
        '''
        Creating new instances
        '''
        self.new_user = User.objects.create_user(username = 'Coach James',email ='james@moringaschool.com',password='JME!@254')
        self.user2 = User.objects.create_user(username='athlete1', email='ath@gmail.com', password='testpass123')
        # self.new_user.save()

        self.new_sport = Sport.objects.create(sport_image = 'image.jpg',name='Football',description='This is football')
        # self.new_sport.save_sport()

        self.new_location = Location.objects.create(name='Kasarani',address='123 Main St',city='Nairobi',country='Kenya',sport=self.new_sport)
        # self.new_location.save_location()
        # print(self.new_location.name)

        # self.new_profile = Profile(user=self.new_user,sport=self.new_sport,profile_photo='profile.jpg',bio="Hey there, I am a swim coach",phone_number='078998567',specialization='Swimming',certifications='Level 3 Coaching - 2024',experience_years=5,created_at='1909-08-01')
        self.new_profile = Profile.objects.get(user=self.new_user)
        self.new_profile.sport = self.new_sport
        self.new_profile.location = self.new_location
        self.new_profile.experience_years = 5
        self.new_profile.save_profile()
        # print(self.new_sport.name)

        # self.new_enquiry = Enquiry.objects.create(profile=self.new_profile,question="Where are you based?",sent_on='1901-08-09')
        # # self.new_enquiry.save_enquiry()

        self.new_service = SportAdvert.objects.create(sport_punchline='Football',service_image='image.jpg',related_sport=self.new_sport,description='The new season is scheduled to start on March 16th',created_at='2025-09-05',posted_by=self.new_profile)
        # self.new_service.save_service()

        self.new_comment = Comment.objects.create(profile=self.new_profile,comment='I like this',created_at='2025-03-04')
        # # self.new_comment.save_comment()


    # def tearDown(self):
    #     return super().tearDown()

    def test_profile_auto_creation(self):
        """Test that a Profile instance is automatically created for a new User."""
        self.assertTrue(Profile.objects.filter(user=self.new_user).exists())
        profile = Profile.objects.get(user=self.new_user)
        self.assertEqual(profile.user.username, 'Coach James')

    def test_profile_creation(self):
        """Test that a Profile instance is created properly."""
        self.assertEqual(self.new_profile.user.username, 'Coach James')
        self.assertEqual(self.new_profile.sport.name, 'Football')
        self.assertEqual(self.new_profile.role, 2)
        self.assertEqual(self.new_profile.experience_years, 5)

    def test_profile_sport_assignment(self):
        """Test assigning a sport to a Profile."""
        self.assertEqual(self.new_profile.sport.name, 'Football')

    def test_profile_location_assignment(self):
        """Test assigning a location to a Profile."""
        self.assertEqual(self.new_profile.location.name,'Kasarani' )

# Test save functionality
# '''
# Note that there is no save test function for and user class profile as it is automatically created when a user signs up
# '''
    def test_save_sport(self):
        self.new_sport.save_sport()
        sports = Sport.objects.all()
        self.assertTrue(len(sports)==1)

    def test_save_location(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==1)

    def test_save_comment(self):
        profile = Profile.objects.get(user=self.new_user)
        self.new_comment.profile = profile
        comments = Comment.objects.all()
        self.assertTrue(len(comments)==1)
        
    # def test_save_enquiry(self):
    #     self.new_enquiry.save_enquiry()
    #     enquiries = Enquiry.objects.all()
    #     self.assertTrue(len(enquiries)==1)

# Testing is if all models are functioning properly
    def test_user_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_sport_instance(self):
        self.assertTrue(isinstance(self.new_sport,Sport))

    def test_location_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_enquiry_instance(self):
        self.assertTrue(isinstance(self.new_enquiry,Enquiry))

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_service_instance(self):
        self.assertTrue(isinstance(self.new_service,Service))

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_comment_creation(self):
        """Test creating a comment on a Profile."""
        comment = Comment.objects.create(profile=self.new_profile, comment="Great job, coach!")
        self.assertEqual(comment.comment, "Great job, coach!")
        # self.assertEqual(comment.user.username, 'athlete1')
        self.assertEqual(comment.profile.user.username, 'Coach James')

