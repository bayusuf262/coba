# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoderedcmsAccordion(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'coderedcms_accordion'


class CoderedcmsAccordionpanel(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    content = models.JSONField()
    custom_css_class = models.CharField(max_length=255)
    custom_id = models.CharField(max_length=255)
    accordion = models.ForeignKey(CoderedcmsAccordion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_accordionpanel'


class CoderedcmsAnalyticssettings(models.Model):
    ga_tracking_id = models.CharField(max_length=255)
    ga_track_button_clicks = models.BooleanField()
    site = models.OneToOneField('WagtailcoreSite', models.DO_NOTHING)
    body_scripts = models.TextField(blank=True, null=True)
    head_scripts = models.TextField(blank=True, null=True)
    ga_g_tracking_id = models.CharField(max_length=255)
    gtm_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'coderedcms_analyticssettings'


class CoderedcmsCarousel(models.Model):
    name = models.CharField(max_length=255)
    show_controls = models.BooleanField()
    show_indicators = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'coderedcms_carousel'


class CoderedcmsCarouselslide(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    background_color = models.CharField(max_length=255)
    custom_css_class = models.CharField(max_length=255)
    custom_id = models.CharField(max_length=255)
    content = models.JSONField()
    carousel = models.ForeignKey(CoderedcmsCarousel, models.DO_NOTHING)
    image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coderedcms_carouselslide'


class CoderedcmsClassifier(models.Model):
    slug = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'coderedcms_classifier'


class CoderedcmsClassifierterm(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=255)
    classifier = models.ForeignKey(CoderedcmsClassifier, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_classifierterm'


class CoderedcmsCoderedpage(models.Model):
    page_ptr = models.OneToOneField('WagtailcorePage', models.DO_NOTHING, primary_key=True)
    index_show_subpages = models.BooleanField()
    index_order_by = models.CharField(max_length=255)
    index_num_per_page = models.IntegerField()
    custom_template = models.CharField(max_length=255)
    struct_org_type = models.CharField(max_length=255)
    struct_org_name = models.CharField(max_length=255)
    struct_org_phone = models.CharField(max_length=255)
    struct_org_address_street = models.CharField(max_length=255)
    struct_org_address_locality = models.CharField(max_length=255)
    struct_org_address_region = models.CharField(max_length=255)
    struct_org_address_postal = models.CharField(max_length=255)
    struct_org_address_country = models.CharField(max_length=255)
    struct_org_geo_lat = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    struct_org_geo_lng = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    struct_org_hours = models.JSONField()
    struct_org_actions = models.JSONField()
    struct_org_extra_json = models.TextField()
    cover_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    og_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    struct_org_image = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    struct_org_logo = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    content_walls = models.JSONField()
    canonical_url = models.CharField(max_length=255)
    index_order_by_classifier = models.ForeignKey(CoderedcmsClassifier, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedpage'


class CoderedcmsCoderedpageClassifierTerms(models.Model):
    id = models.BigAutoField(primary_key=True)
    coderedpage = models.ForeignKey(CoderedcmsCoderedpage, models.DO_NOTHING)
    classifierterm = models.ForeignKey(CoderedcmsClassifierterm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedpage_classifier_terms'
        unique_together = (('coderedpage', 'classifierterm'),)


class CoderedcmsCoderedpageIndexClassifiers(models.Model):
    id = models.BigAutoField(primary_key=True)
    coderedpage = models.ForeignKey(CoderedcmsCoderedpage, models.DO_NOTHING)
    classifier = models.ForeignKey(CoderedcmsClassifier, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedpage_index_classifiers'
        unique_together = (('coderedpage', 'classifier'),)


class CoderedcmsCoderedsessionformsubmission(models.Model):
    form_data = models.JSONField()
    submit_time = models.DateTimeField()
    session_key = models.CharField(max_length=40, blank=True, null=True)
    thumbnails_by_path = models.TextField()
    last_modification = models.DateTimeField()
    status = models.CharField(max_length=10)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedsessionformsubmission'
        unique_together = (('page', 'session_key'), ('page', 'user'),)


class CoderedcmsCoderedsubmissionrevision(models.Model):
    type = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    submission_id = models.TextField()
    data = models.TextField()
    summary = models.TextField()
    submission_ct = models.ForeignKey('DjangoContentType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedsubmissionrevision'


class CoderedcmsCoderedtag(models.Model):
    content_object = models.ForeignKey(CoderedcmsCoderedpage, models.DO_NOTHING)
    tag = models.ForeignKey('TaggitTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_coderedtag'


class CoderedcmsContentwall(models.Model):
    name = models.CharField(max_length=255)
    content = models.JSONField()
    is_dismissible = models.BooleanField()
    show_once = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'coderedcms_contentwall'


class CoderedcmsFooter(models.Model):
    name = models.CharField(max_length=255)
    custom_css_class = models.CharField(max_length=255)
    custom_id = models.CharField(max_length=255)
    content = models.JSONField()

    class Meta:
        managed = False
        db_table = 'coderedcms_footer'


class CoderedcmsFooterorderable(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    footer = models.ForeignKey(CoderedcmsFooter, models.DO_NOTHING, blank=True, null=True)
    footer_chooser = models.ForeignKey('CoderedcmsLayoutsettings', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_footerorderable'


class CoderedcmsLayoutsettings(models.Model):
    navbar_color_scheme = models.CharField(max_length=50)
    navbar_class = models.CharField(max_length=255)
    navbar_fixed = models.BooleanField()
    navbar_content_fluid = models.BooleanField()
    navbar_collapse_mode = models.CharField(max_length=50)
    navbar_format = models.CharField(max_length=50)
    navbar_search = models.BooleanField()
    frontend_theme = models.CharField(max_length=50)
    favicon = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    logo = models.ForeignKey('WagtailimagesImage', models.DO_NOTHING, blank=True, null=True)
    site = models.OneToOneField('WagtailcoreSite', models.DO_NOTHING)
    external_new_tab = models.BooleanField()
    from_email_address = models.CharField(max_length=255)
    google_maps_api_key = models.CharField(max_length=255)
    mailchimp_api_key = models.CharField(max_length=255)
    search_num_results = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coderedcms_layoutsettings'


class CoderedcmsNavbar(models.Model):
    name = models.CharField(max_length=255)
    custom_css_class = models.CharField(max_length=255)
    custom_id = models.CharField(max_length=255)
    menu_items = models.JSONField()

    class Meta:
        managed = False
        db_table = 'coderedcms_navbar'


class CoderedcmsNavbarorderable(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    navbar = models.ForeignKey(CoderedcmsNavbar, models.DO_NOTHING, blank=True, null=True)
    navbar_chooser = models.ForeignKey(CoderedcmsLayoutsettings, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coderedcms_navbarorderable'


class CoderedcmsReusablecontent(models.Model):
    name = models.CharField(max_length=255)
    content = models.JSONField()

    class Meta:
        managed = False
        db_table = 'coderedcms_reusablecontent'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class WagtailadminAdmin(models.Model):

    class Meta:
        managed = False
        db_table = 'wagtailadmin_admin'


class WagtailcoreCollection(models.Model):
    path = models.CharField(unique=True, max_length=255, db_collation='C')
    depth = models.IntegerField()
    numchild = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collection'


class WagtailcoreCollectionviewrestriction(models.Model):
    restriction_type = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction'


class WagtailcoreCollectionviewrestrictionGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    collectionviewrestriction = models.ForeignKey(WagtailcoreCollectionviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_collectionviewrestriction_groups'
        unique_together = (('collectionviewrestriction', 'group'),)


class WagtailcoreComment(models.Model):
    text = models.TextField()
    contentpath = models.TextField()
    position = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    resolved_at = models.DateTimeField(blank=True, null=True)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)
    resolved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    revision_created = models.ForeignKey('WagtailcoreRevision', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_comment'


class WagtailcoreCommentreply(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    comment = models.ForeignKey(WagtailcoreComment, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_commentreply'


class WagtailcoreGroupapprovaltask(models.Model):
    task_ptr = models.OneToOneField('WagtailcoreTask', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask'


class WagtailcoreGroupapprovaltaskGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupapprovaltask = models.ForeignKey(WagtailcoreGroupapprovaltask, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupapprovaltask_groups'
        unique_together = (('groupapprovaltask', 'group'),)


class WagtailcoreGroupcollectionpermission(models.Model):
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_groupcollectionpermission'
        unique_together = (('group', 'collection', 'permission'),)


class WagtailcoreGrouppagepermission(models.Model):
    permission_type = models.CharField(max_length=20)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    page = models.ForeignKey('WagtailcorePage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_grouppagepermission'
        unique_together = (('group', 'page', 'permission_type'),)


class WagtailcoreLocale(models.Model):
    language_code = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'wagtailcore_locale'


class WagtailcoreModellogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    content_changed = models.BooleanField()
    deleted = models.BooleanField()
    object_id = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(blank=True, null=True)
    revision_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_modellogentry'


class WagtailcorePage(models.Model):
    path = models.CharField(unique=True, max_length=255, db_collation='C')
    depth = models.IntegerField()
    numchild = models.IntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    live = models.BooleanField()
    has_unpublished_changes = models.BooleanField()
    url_path = models.TextField()
    seo_title = models.CharField(max_length=255)
    show_in_menus = models.BooleanField()
    search_description = models.TextField()
    go_live_at = models.DateTimeField(blank=True, null=True)
    expire_at = models.DateTimeField(blank=True, null=True)
    expired = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    locked = models.BooleanField()
    latest_revision_created_at = models.DateTimeField(blank=True, null=True)
    first_published_at = models.DateTimeField(blank=True, null=True)
    live_revision = models.ForeignKey('WagtailcoreRevision', models.DO_NOTHING, blank=True, null=True)
    last_published_at = models.DateTimeField(blank=True, null=True)
    draft_title = models.CharField(max_length=255)
    locked_at = models.DateTimeField(blank=True, null=True)
    locked_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    translation_key = models.UUIDField()
    locale = models.ForeignKey(WagtailcoreLocale, models.DO_NOTHING)
    alias_of = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    latest_revision = models.ForeignKey('WagtailcoreRevision', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_page'
        unique_together = (('translation_key', 'locale'),)


class WagtailcorePagelogentry(models.Model):
    label = models.TextField()
    action = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    content_changed = models.BooleanField()
    deleted = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    page_id = models.IntegerField()
    revision_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagelogentry'


class WagtailcorePagesubscription(models.Model):
    comment_notifications = models.BooleanField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pagesubscription'
        unique_together = (('page', 'user'),)


class WagtailcorePageviewrestriction(models.Model):
    password = models.CharField(max_length=255)
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    restriction_type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction'


class WagtailcorePageviewrestrictionGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    pageviewrestriction = models.ForeignKey(WagtailcorePageviewrestriction, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_pageviewrestriction_groups'
        unique_together = (('pageviewrestriction', 'group'),)


class WagtailcoreReferenceindex(models.Model):
    object_id = models.CharField(max_length=255)
    to_object_id = models.CharField(max_length=255)
    model_path = models.TextField()
    content_path = models.TextField()
    content_path_hash = models.UUIDField()
    base_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    to_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_referenceindex'
        unique_together = (('base_content_type', 'object_id', 'to_content_type', 'to_object_id', 'content_path_hash'),)


class WagtailcoreRevision(models.Model):
    submitted_for_moderation = models.BooleanField()
    created_at = models.DateTimeField()
    content = models.JSONField()
    approved_go_live_at = models.DateTimeField(blank=True, null=True)
    object_id = models.CharField(max_length=255)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    base_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    object_str = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_revision'


class WagtailcoreSite(models.Model):
    hostname = models.CharField(max_length=255)
    port = models.IntegerField()
    is_default_site = models.BooleanField()
    root_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)
    site_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailcore_site'
        unique_together = (('hostname', 'port'),)


class WagtailcoreTask(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_task'


class WagtailcoreTaskstate(models.Model):
    status = models.CharField(max_length=50)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(blank=True, null=True)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    revision = models.ForeignKey(WagtailcoreRevision, models.DO_NOTHING)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow_state = models.ForeignKey('WagtailcoreWorkflowstate', models.DO_NOTHING)
    finished_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_taskstate'


class WagtailcoreWorkflow(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflow'


class WagtailcoreWorkflowcontenttype(models.Model):
    content_type = models.OneToOneField(DjangoContentType, models.DO_NOTHING, primary_key=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowcontenttype'


class WagtailcoreWorkflowpage(models.Model):
    page = models.OneToOneField(WagtailcorePage, models.DO_NOTHING, primary_key=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowpage'


class WagtailcoreWorkflowstate(models.Model):
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    current_task_state = models.OneToOneField(WagtailcoreTaskstate, models.DO_NOTHING, blank=True, null=True)
    object_id = models.CharField(max_length=255)
    requested_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    base_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowstate'
        unique_together = (('base_content_type', 'object_id'),)


class WagtailcoreWorkflowtask(models.Model):
    sort_order = models.IntegerField(blank=True, null=True)
    task = models.ForeignKey(WagtailcoreTask, models.DO_NOTHING)
    workflow = models.ForeignKey(WagtailcoreWorkflow, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailcore_workflowtask'
        unique_together = (('workflow', 'task'),)


class WagtaildocsDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_size = models.IntegerField(blank=True, null=True)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_document'


class WagtaildocsUploadeddocument(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtaildocs_uploadeddocument'


class WagtailembedsEmbed(models.Model):
    url = models.TextField()
    max_width = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=10)
    html = models.TextField()
    title = models.TextField()
    author_name = models.TextField()
    provider_name = models.TextField()
    thumbnail_url = models.TextField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField()
    hash = models.CharField(unique=True, max_length=32)
    cache_until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailembeds_embed'


class WagtailformsFormsubmission(models.Model):
    form_data = models.JSONField()
    submit_time = models.DateTimeField()
    page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailforms_formsubmission'


class WagtailimagesImage(models.Model):
    title = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField()
    focal_point_x = models.IntegerField(blank=True, null=True)
    focal_point_y = models.IntegerField(blank=True, null=True)
    focal_point_width = models.IntegerField(blank=True, null=True)
    focal_point_height = models.IntegerField(blank=True, null=True)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    collection = models.ForeignKey(WagtailcoreCollection, models.DO_NOTHING)
    file_hash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wagtailimages_image'


class WagtailimagesRendition(models.Model):
    file = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    focal_point_key = models.CharField(max_length=16)
    filter_spec = models.CharField(max_length=255)
    image = models.ForeignKey(WagtailimagesImage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailimages_rendition'
        unique_together = (('image', 'filter_spec', 'focal_point_key'),)


class WagtailimagesUploadedimage(models.Model):
    file = models.CharField(max_length=200)
    uploaded_by_user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wagtailimages_uploadedimage'


class WagtailredirectsRedirect(models.Model):
    old_path = models.CharField(max_length=255)
    is_permanent = models.BooleanField()
    redirect_link = models.CharField(max_length=255)
    redirect_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey(WagtailcoreSite, models.DO_NOTHING, blank=True, null=True)
    automatically_created = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    redirect_page_route_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailredirects_redirect'
        unique_together = (('old_path', 'site'),)


class WagtailsearchIndexentry(models.Model):
    object_id = models.CharField(max_length=50)
    title_norm = models.FloatField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    autocomplete = models.TextField()  # This field type is a guess.
    title = models.TextField()  # This field type is a guess.
    body = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'wagtailsearch_indexentry'
        unique_together = (('content_type', 'object_id'),)


class WagtailsearchQuery(models.Model):
    query_string = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_query'


class WagtailsearchQuerydailyhits(models.Model):
    date = models.DateField()
    hits = models.IntegerField()
    query = models.ForeignKey(WagtailsearchQuery, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailsearch_querydailyhits'
        unique_together = (('query', 'date'),)


class WagtailseoSeosettings(models.Model):
    og_meta = models.BooleanField()
    twitter_meta = models.BooleanField()
    twitter_site = models.CharField(max_length=16)
    struct_meta = models.BooleanField()
    site = models.OneToOneField(WagtailcoreSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wagtailseo_seosettings'


class WagtailusersUserprofile(models.Model):
    submitted_notifications = models.BooleanField()
    approved_notifications = models.BooleanField()
    rejected_notifications = models.BooleanField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    preferred_language = models.CharField(max_length=10)
    current_time_zone = models.CharField(max_length=40)
    avatar = models.CharField(max_length=100)
    updated_comments_notifications = models.BooleanField()
    dismissibles = models.JSONField()

    class Meta:
        managed = False
        db_table = 'wagtailusers_userprofile'


class WebsiteArticleindexpage(models.Model):
    coderedpage_ptr = models.OneToOneField(CoderedcmsCoderedpage, models.DO_NOTHING, primary_key=True)
    body = models.JSONField(blank=True, null=True)
    show_images = models.BooleanField()
    show_captions = models.BooleanField()
    show_meta = models.BooleanField()
    show_preview_text = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'website_articleindexpage'


class WebsiteArticlepage(models.Model):
    coderedpage_ptr = models.OneToOneField(CoderedcmsCoderedpage, models.DO_NOTHING, primary_key=True)
    body = models.JSONField(blank=True, null=True)
    caption = models.CharField(max_length=255)
    author_display = models.CharField(max_length=255)
    date_display = models.DateField(blank=True, null=True)
    author = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_articlepage'


class WebsiteFormconfirmemail(models.Model):
    id = models.BigAutoField(primary_key=True)
    to_address = models.CharField(max_length=255)
    from_address = models.CharField(max_length=255)
    reply_address = models.CharField(max_length=255)
    cc_address = models.CharField(max_length=255)
    bcc_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    page = models.ForeignKey('WebsiteFormpage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'website_formconfirmemail'


class WebsiteFormpage(models.Model):
    coderedpage_ptr = models.OneToOneField(CoderedcmsCoderedpage, models.DO_NOTHING, primary_key=True)
    body = models.JSONField(blank=True, null=True)
    to_address = models.CharField(max_length=255)
    reply_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    save_to_database = models.BooleanField()
    button_text = models.CharField(max_length=255)
    button_style = models.CharField(max_length=255)
    button_size = models.CharField(max_length=255)
    button_css_class = models.CharField(max_length=255)
    form_css_class = models.CharField(max_length=255)
    form_id = models.CharField(max_length=255)
    form_golive_at = models.DateTimeField(blank=True, null=True)
    form_expire_at = models.DateTimeField(blank=True, null=True)
    spam_protection = models.BooleanField()
    thank_you_page = models.ForeignKey(WagtailcorePage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_formpage'


class WebsiteFormpagefield(models.Model):
    id = models.BigAutoField(primary_key=True)
    sort_order = models.IntegerField(blank=True, null=True)
    clean_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    required = models.BooleanField()
    choices = models.TextField()
    default_value = models.TextField()
    help_text = models.CharField(max_length=255)
    field_type = models.CharField(max_length=16)
    page = models.ForeignKey(WebsiteFormpage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'website_formpagefield'


class WebsiteWebpage(models.Model):
    coderedpage_ptr = models.OneToOneField(CoderedcmsCoderedpage, models.DO_NOTHING, primary_key=True)
    body = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'website_webpage'
