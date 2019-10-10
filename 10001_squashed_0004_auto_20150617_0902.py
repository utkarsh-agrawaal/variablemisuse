def create_anonymous(apps, schema_editor):
    User = apps.get_model("users", "User")
    if not User.objects.filter(display_name='AnonymousUser').exists():
        User.objects.create(
            display_name='AnonymousUser',
            password='',
            email=''
        )
