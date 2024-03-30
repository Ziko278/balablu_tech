from admin_site.models import SiteInfoModel


def general_info(request):
    site_info = SiteInfoModel.objects.first()
    
    return {
        'site_info': site_info,

    }
