# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Supplier'
        db.create_table('service_area_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('service_area', ['Supplier'])

        # Adding model 'ServiceArea'
        db.create_table('service_area_servicearea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service_area.Supplier'])),
            ('x1', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=12)),
            ('y1', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12)),
            ('x2', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=12)),
            ('y2', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12)),
        ))
        db.send_create_signal('service_area', ['ServiceArea'])

        # Adding model 'Vertice'
        db.create_table('service_area_vertice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service_area.ServiceArea'])),
            ('next_vertice', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service_area.Vertice'])),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=12)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=12)),
        ))
        db.send_create_signal('service_area', ['Vertice'])


    def backwards(self, orm):
        # Deleting model 'Supplier'
        db.delete_table('service_area_supplier')

        # Deleting model 'ServiceArea'
        db.delete_table('service_area_servicearea')

        # Deleting model 'Vertice'
        db.delete_table('service_area_vertice')


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
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '12'}),
            'next_vertice': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.Vertice']"}),
            'service_area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service_area.ServiceArea']"})
        }
    }

    complete_apps = ['service_area']