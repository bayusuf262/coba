from wagtail import hooks
from .models import UserVisit
from django.http import HttpRequest
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from .models import UserVisit


class UserVisitPage(ModelAdmin):
    model = UserVisit 
    menu_label = "Audit Trail User"  
    menu_icon = "history" 
    menu_order = 9000
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    # list_display = ('user.name', "visit_date")
    list_filter = ()
    search_fields = ()


modeladmin_register(UserVisitPage)

# modeladmin_register(ReportsAdminGroup)


# from wagtail.admin.views.pages import PageIndexView

# class CustomPageIndexView(PageIndexView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_visits'] = UserVisit.objects.all()
#         return context
@hooks.register('before_serve_page')
def record_user_visit(page, request, serve_args, serve_kwargs):
    if request.user.is_authenticated:
        UserVisit.objects.create(user=request.user, visited_page=page)

# @hooks.register('register_admin_view')
# def register_custom_page_index_view():
#     return {
#         'model': UserVisit,
#         'admin_view_class': CustomPageIndexView
#     }
