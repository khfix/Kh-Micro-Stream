# Generated by Django 5.0.1 on 2024-01-13 11:59

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth_system", "0001_initial"),
        ("khapi", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "apiuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth_system.apiuser",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
            bases=("auth_system.apiuser",),
        ),
        migrations.CreateModel(
            name="Login",
            fields=[
                (
                    "loginapi_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth_system.loginapi",
                    ),
                ),
            ],
            bases=("auth_system.loginapi",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="StreamerRegister",
            fields=[
                (
                    "registerapi_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth_system.registerapi",
                    ),
                ),
            ],
            bases=("auth_system.registerapi",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserRegister",
            fields=[
                (
                    "registerapi_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="auth_system.registerapi",
                    ),
                ),
            ],
            bases=("auth_system.registerapi",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="UserRetrieveByIDAPI",
            fields=[
                (
                    "getbyidapi_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="khapi.getbyidapi",
                    ),
                ),
            ],
            bases=("khapi.getbyidapi",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name="UsersAPI",
            fields=[
                (
                    "listapi_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="khapi.listapi",
                    ),
                ),
            ],
            bases=("khapi.listapi",),
            managers=[
                ("objects", django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
