# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Vertice.next_vertice'
        db.delete_column('service_area_vertice', 'next_vertice_id')


    def backwards(self, orm):
        # Adding field 'Vertice.next_vertice'
        db.add_column('service_area_vertice', 'next_vertice',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service_area.Vertice'], null=True, blank=True),
                      keep_default=False)


    models = {
        'service_area.servicearea': {
            'Meta': {'object_name': 'ServiceArea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.Supplier']"}),
            'x1': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '15'}),
            'x2': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '15'}),
            'y1': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '16'}),
            'y2': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '16'})
        },
        'service_area.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'service_area.vertice': {
            'Meta': {'object_name': 'Vertice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '14'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'decimal_places': '12', 'max_digits': '15'}),
            'service_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.ServiceArea']"})
        }
    }

    complete_apps = ['service_area']