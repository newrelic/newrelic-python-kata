# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Choice.poll'
        db.add_column(u'query_choice', 'poll',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['query.Poll']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Choice.poll'
        db.delete_column(u'query_choice', 'poll_id')


    models = {
        u'query.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['query.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'query.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['query']