from .models import SocialMedia


def main_context(request):
    socials = SocialMedia.objects.all()
    return {
        "socials": socials,
    }
