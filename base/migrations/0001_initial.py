# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Seccion'
        db.create_table('base_seccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('materia', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('profesor', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('base', ['Seccion'])

        # Adding model 'Alumno'
        db.create_table('base_alumno', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Seccion'])),
        ))
        db.send_create_signal('base', ['Alumno'])

        # Adding model 'Asistencia'
        db.create_table('base_asistencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Alumno'])),
            ('clase', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Clase'])),
            ('punto', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('base', ['Asistencia'])

        # Adding model 'Clase'
        db.create_table('base_clase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(default='L', max_length=1)),
        ))
        db.send_create_signal('base', ['Clase'])


    def backwards(self, orm):
        # Deleting model 'Seccion'
        db.delete_table('base_seccion')

        # Deleting model 'Alumno'
        db.delete_table('base_alumno')

        # Deleting model 'Asistencia'
        db.delete_table('base_asistencia')

        # Deleting model 'Clase'
        db.delete_table('base_clase')


    models = {
        'base.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'asistencias': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['base.Clase']", 'through': "orm['base.Asistencia']", 'symmetrical': 'False'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Seccion']"})
        },
        'base.asistencia': {
            'Meta': {'object_name': 'Asistencia'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Alumno']"}),
            'clase': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Clase']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'punto': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'base.clase': {
            'Meta': {'object_name': 'Clase'},
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar': ('django.db.models.fields.CharField', [], {'default': "'L'", 'max_length': '1'})
        },
        'base.seccion': {
            'Meta': {'object_name': 'Seccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'profesor': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['base']