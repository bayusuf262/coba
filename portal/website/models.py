"""
Create or customize your page models here.
"""
from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from django.db import models
from wagtail.models import Page
from django.contrib.auth.models import User
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage,
    CoderedPage
)


class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """

    class Meta:
        verbose_name = "Article"
        ordering = ["-first_published_at"]

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ["website.ArticleIndexPage"]

    template = "coderedcms/pages/article_page.html"
    search_template = "coderedcms/pages/article_page.search.html"


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """

    class Meta:
        verbose_name = "Article Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = "website.ArticlePage"

    # Only allow ArticlePages beneath this page.
    subpage_types = ["website.ArticlePage"]

    template = "coderedcms/pages/article_index_page.html"


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """

    class Meta:
        verbose_name = "Form"

    template = "coderedcms/pages/form_page.html"


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """

    class Meta:
        ordering = ["sort_order"]

    page = ParentalKey("FormPage", related_name="form_fields")


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """

    page = ParentalKey("FormPage", related_name="confirmation_emails")


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    """

    #FIX GET LATEST PAGE

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Mengambil parent WebPage
        parent_page = self.get_parent().specific

        # Mengambil halaman-halaman terbaru berdasarkan waktu publikasi
        latest_pages = Page.objects.live().descendant_of(parent_page).order_by('-first_published_at')[:3]

        context['latest_pages'] = latest_pages

        return context

    class Meta:
        verbose_name = "Web Page"

    template = "coderedcms/pages/web_page.html"



class UserVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visited_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} visited {self.visited_page.title}'