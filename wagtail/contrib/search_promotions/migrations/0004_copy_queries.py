# Generated by Django 3.1.8 on 2021-06-22 14:56

from django.db import migrations
from django.core.management.color import no_style


def reset_search_promotion_sequence(apps, schema_editor):
    Query = apps.get_model("wagtailsearchpromotions.Query")
    QueryDailyHits = apps.get_model("wagtailsearchpromotions.QueryDailyHits")

    statements = schema_editor.connection.ops.sequence_reset_sql(
        no_style(), [Query, QueryDailyHits]
    )
    for statement in statements:
        schema_editor.execute(statement)


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailsearchpromotions", "0003_query_querydailyhits"),
    ]

    # Columns should be explicitly specified in case the order of columns
    # between each table pair is different, which may be the case for Wagtail
    # instances that were created when we still used django-south.
    operations = [
        migrations.RunSQL(
            """
            INSERT INTO wagtailsearchpromotions_query (id, query_string)
            SELECT id, query_string FROM wagtailsearch_query
            """,
            "",
        ),
        migrations.RunSQL(
            """
            INSERT INTO wagtailsearchpromotions_querydailyhits (id, date, hits, query_id)
            SELECT id, date, hits, query_id FROM wagtailsearch_querydailyhits
            """,
            "",
        ),
        # We set an explicit pk instead of relying on auto-incrementation,
        # so we need to reset the database sequence.
        migrations.RunPython(
            reset_search_promotion_sequence, migrations.RunPython.noop
        ),
    ]
