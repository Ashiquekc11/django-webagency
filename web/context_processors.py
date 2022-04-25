from .models import SocialMedia, About


def main_context(request):
    socials = SocialMedia.objects.all()
    random = "as56hi8qu551e"
    about = About.objects.last()

    return {
        "socials": socials,
        "random": random,
        "about": about,

    }
