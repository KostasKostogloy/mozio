# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Vertice.latitude2'
        db.add_column('service_area_vertice', 'latitude2',
                      self.gf('django.db.models.fields.DecimalField')(default=1, max_digits=14, decimal_places=12),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Vertice.latitude2'
        db.delete_column('service_area_vertice', 'latitude2')


    models = {
        'service_area.servicearea': {
            'Meta': {'object_name': 'ServiceArea'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.Supplier']"}),
            'x1': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '12'}),
            'x2': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '12'}),
            'y1': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12'}),
            'y2': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12'})
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
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '12'}),
            'latitude2': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '12'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12'}),
            'next_vertice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.Vertice']"}),
            'service_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.ServiceArea']"})
        }
    }

    complete_apps = ['service_area']