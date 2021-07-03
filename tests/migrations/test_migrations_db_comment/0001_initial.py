from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    operations = [
        migrations.CreateModel(
            "Author",
            [
                ("id", models.AutoField(primary_key=True)),
                ("name", models.CharField(max_length=255, db_comment='db comment to name Field')),
                ("slug", models.SlugField(null=True)),
                ("age", models.IntegerField(default=0, db_comment='db comment to age Field')),
                ("silly_field", models.BooleanField(default=False, db_comment='db comment to bool Field')),
            ],
            options={
                "db_table_comment": "I am table Comment",
            }
        ),
        migrations.CreateModel(
            "Tribble",
            [
                ("id", models.AutoField(primary_key=True)),
                ("fluffy", models.BooleanField(default=True)),
            ],
            options={
                "db_table_comment": "I am tribble table Comment",
            }
        ),
        migrations.AddField(
            model_name='tribble',
            name='bool_field',
            field=models.BooleanField(default=False, db_comment='new db comment'),
        ),
        migrations.AlterField(
            model_name='author',
            name='silly_field',
            field=models.BooleanField(default=True, db_comment='changed db comment')
        ),
    ]
