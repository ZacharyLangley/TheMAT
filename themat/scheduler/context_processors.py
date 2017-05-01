from .models import UserProfile

def add_variable_to_context(request):
    if request.user.is_authenticated():  # make sure user is logged in
        up = UserProfile.objects.get(user=request.user)
        return {
            'up': up
        }
    else:
        return {
        }
