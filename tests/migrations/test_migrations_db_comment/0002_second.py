from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("migrations", "0001_initial"),
    ]

    operations = [

        migrations.DeleteModel("Tribble"),

        migrations.AlterField(
            model_name='author',
            name='silly_field',
            field=models.BooleanField(default=True, db_comment='')
        ),

        migrations.AddField("Author", "rating",
                            models.IntegerField(default=0, db_comment='new comment for rating Column')),

        migrations.CreateModel(
            "Book",
            [
                ("id", models.AutoField(primary_key=True)),
                (
                    "author",
                    models.ForeignKey("migrations.Author", models.SET_NULL, db_comment='this is FK', null=True)
                ),
            ],
        )

    ]
