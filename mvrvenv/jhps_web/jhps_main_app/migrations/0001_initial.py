# Generated by Django 4.1.4 on 2022-12-25 13:50

import ckeditor.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_page', models.IntegerField(choices=[(0, 'About Us'), (1, 'Vision & Mission'), (2, 'Awards'), (3, 'Presidential Visit')])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='about_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_page', models.IntegerField(choices=[(0, 'Class Room Learning'), (1, 'E-Learning')])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='academics_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_page', models.IntegerField(choices=[(0, 'Admission Policy and Procedure'), (1, 'Fee Structure')])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='admission_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Admission_Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enq_name', models.CharField(max_length=255)),
                ('mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=255)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_page', models.IntegerField(choices=[(0, 'Campus'), (1, 'Class Rooms'), (2, 'Library'), (3, 'Auditorium'), (4, 'Informary Room'), (5, 'Canteen'), (6, 'Stationary'), (7, 'Teacher Welfare')])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='campus_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Circulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('upload_pdf', models.FileField(upload_to='circulars_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('upload_pdf', models.FileField(upload_to='downloads_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='events_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=150)),
                ('staff_designation', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Notice_Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Press_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='press_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Refer_A_Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child_name', models.CharField(max_length=100)),
                ('parent_name', models.CharField(max_length=100)),
                ('mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=150, region=None)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('referee_parent_name', models.CharField(max_length=100)),
                ('referee_child_name', models.CharField(max_length=100)),
                ('referee_mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('referee_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('Note', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Magazines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('upload_pdf', models.FileField(upload_to='Magazines_pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Scroll_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sports_CSA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_page', models.IntegerField(choices=[(0, 'SPORTS'), (1, 'CSA'), (2, 'ECA'), (3, 'HOUSE ACTIVITIES'), (4, 'EDUCATIONAL TOURS')])),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='sports_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='staff_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Video_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('video_URL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.IntegerField(choices=[(0, '2022-23'), (1, '2023-24')])),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('relation', models.IntegerField(choices=[(0, 'FATHER'), (1, 'MOTHER')])),
                ('local_type', models.IntegerField(choices=[(0, 'Local'), (1, 'Non-Local')])),
                ('transfer_from', models.CharField(blank=True, max_length=150, null=True)),
                ('mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('message', models.TextField(blank=True, max_length=500, null=True)),
                ('mother_name', models.CharField(max_length=150)),
                ('mother_organization', models.CharField(blank=True, max_length=150, null=True)),
                ('mother_designation', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_income', models.CharField(blank=True, max_length=12, null=True)),
                ('mother_mobile_No', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('mother_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('father_name', models.CharField(max_length=150)),
                ('father_orgnization', models.CharField(max_length=150)),
                ('father_designation', models.CharField(max_length=50)),
                ('father_income', models.CharField(max_length=12)),
                ('father_mobile_No', phonenumber_field.modelfields.PhoneNumberField(max_length=15, region=None)),
                ('father_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('reference_name', models.CharField(blank=True, max_length=150, null=True)),
                ('reference_designation', models.CharField(blank=True, max_length=50, null=True)),
                ('reference_department', models.CharField(blank=True, max_length=50, null=True)),
                ('reference_company', models.CharField(blank=True, max_length=50, null=True)),
                ('reference_mobile_No', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('reference_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('remarks', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='student_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Video_Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('video_URL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('paragraph_data', ckeditor.fields.RichTextField()),
                ('upload_image', models.ImageField(blank=True, null=True, upload_to='testimonials_images/')),
            ],
        ),
    ]
