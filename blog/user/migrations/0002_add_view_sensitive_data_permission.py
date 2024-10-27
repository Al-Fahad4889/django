from django.db import migrations

def create_custom_permission(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    content_type = ContentType.objects.get(app_label='auth', model='user')
    
    # Add custom permission for viewing sensitive data
    Permission.objects.create(
        codename='view_sensitive_data',
        name='Can view sensitive data',
        content_type=content_type,
    )

class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),  # Use the latest migration in 'auth' as a dependency
    ]

    operations = [
        migrations.RunPython(create_custom_permission),
    ]
