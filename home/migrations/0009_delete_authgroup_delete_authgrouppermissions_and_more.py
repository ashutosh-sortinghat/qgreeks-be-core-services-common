# Generated by Django 5.0.2 on 2024-03-01 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_authgroup_authgrouppermissions_authpermission_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AuthGroup",
        ),
        migrations.DeleteModel(
            name="AuthGroupPermissions",
        ),
        migrations.DeleteModel(
            name="AuthPermission",
        ),
        migrations.DeleteModel(
            name="AuthUser",
        ),
        migrations.DeleteModel(
            name="AuthUserGroups",
        ),
        migrations.DeleteModel(
            name="AuthUserUserPermissions",
        ),
        migrations.DeleteModel(
            name="DjangoAdminLog",
        ),
        migrations.DeleteModel(
            name="DjangoContentType",
        ),
        migrations.DeleteModel(
            name="DjangoMigrations",
        ),
        migrations.DeleteModel(
            name="DjangoSession",
        ),
        migrations.AlterModelOptions(
            name="account",
            options={},
        ),
        migrations.AlterModelOptions(
            name="employees",
            options={},
        ),
        migrations.AlterModelOptions(
            name="homeproduct",
            options={},
        ),
        migrations.AlterModelOptions(
            name="stockdetails",
            options={},
        ),
        migrations.AlterModelOptions(
            name="stockscreener",
            options={},
        ),
    ]
