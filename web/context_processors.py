from .models import SocialMedia


def main_context(request):
    socials = SocialMedia.objects.all()
    random = "as56hi8qu551e"

    return {
        "socials": socials,
        "random": random,


    }
