from django.contrib import admin
from api.models import User, Service, Portfolio, Testimonial, Enquiry, NewsletterSubscriber, EmailTemplate
from django_summernote.admin import SummernoteModelAdmin


admin.site.site_header = "APE STUDIO"
admin.site.site_title = "APE STUDIO"
admin.site.index_title = "APE Studio Dashboard"
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'get_full_name', 'is_active', 'is_superuser','date_joined')
    list_filter = ('date_joined',)
    search_fields = ('username',)
    ordering = ('-date_joined',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon', 'is_active', 'is_deleted', 'created_at','updated_at')
    list_filter = ('title', 'created_at',)
    search_fields = ('title',)
    ordering = ('-created_at',)
    # Show deleted items also
    def get_queryset(self, request):
        return Service.all_objects.all()

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project_url', 'technologies', 'featured', 'is_active', 'is_deleted', 'created_at','updated_at')
    list_filter = ('created_at', 'is_active', 'is_deleted')
    search_fields = ('title',)
    ordering = ('-created_at',)

    # Show deleted items also
    def get_queryset(self, request):
        return Portfolio.all_objects.all()

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'company', 'rating', 'is_published', 'is_active', 'is_deleted', 'created_at','updated_at')
    list_filter = ('client_name', 'company', 'rating', 'is_active', 'is_deleted')
    search_fields = ('title',)
    ordering = ('-created_at',)

    # Show deleted items also
    def get_queryset(self, request):
        return Testimonial.all_objects.all()
    

@admin.register(Enquiry)
class EnquiryAdmin(SummernoteModelAdmin):
    summernote_fields = ('message',)
    list_display = (
        'id',
        'name',
        'email',
        'phone',
        'service_interest',
        'is_read',
        'is_deleted', 
        'is_active',
        'created_at',
        'updated_at'
    )

    list_filter = ('service_interest', 'is_read')

    search_fields = (
        'name',
        'email',
        'phone'
    )

    # Show deleted items also
    def get_queryset(self, request):
        return Enquiry.all_objects.all()

   

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'email',
        'subscribed_at',
        'is_deleted', 
        'is_active',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'email',
    )

    list_filter = (
        'is_active',
        'subscribed_at'
    )

    def get_queryset(self, request):
        return NewsletterSubscriber.all_objects.all()

@admin.register(EmailTemplate)
class EmailTemplateAdmin(SummernoteModelAdmin):
    summernote_fields = ('template_content',)
    list_display = ('id', 'type', 'template_identifier', 'template_subject', 'template_content', 'template_keyword', 'body_font_style', 'footer_font_style', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('type', 'template_identifier')
    ordering = ('type', 'template_identifier', '-created_at',)

    def get_queryset(self, request):
        return EmailTemplate.all_objects.all()