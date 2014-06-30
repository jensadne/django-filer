# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Folder'
        db.create_table(u'filer_folder', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'children', null=True, to=orm['filer.Folder'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'filer_owned_folders', null=True, to=orm['hsauth.User'])),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'filer', ['Folder'])

        # Adding unique constraint on 'Folder', fields ['parent', 'name']
        db.create_unique(u'filer_folder', ['parent_id', 'name'])

        # Adding model 'FolderPermission'
        db.create_table(u'filer_folderpermission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Folder'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'filer_folder_permissions', null=True, to=orm['hsauth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'filer_folder_permissions', null=True, to=orm['auth.Group'])),
            ('everybody', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_edit', self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True)),
            ('can_read', self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True)),
            ('can_add_children', self.gf('django.db.models.fields.SmallIntegerField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'filer', ['FolderPermission'])

        # Adding model 'File'
        db.create_table(u'filer_file', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_filer.file_set', null=True, to=orm['contenttypes.ContentType'])),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'all_files', null=True, to=orm['filer.Folder'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=255, null=True, blank=True)),
            ('_file_size', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sha1', self.gf('django.db.models.fields.CharField')(default=u'', max_length=40, blank=True)),
            ('has_all_mandatory_data', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=u'', max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'owned_files', null=True, to=orm['hsauth.User'])),
            ('uploaded_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'filer', ['File'])

        # Adding model 'Clipboard'
        db.create_table(u'filer_clipboard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'filer_clipboards', to=orm['hsauth.User'])),
        ))
        db.send_create_signal(u'filer', ['Clipboard'])

        # Adding model 'ClipboardItem'
        db.create_table(u'filer_clipboarditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.File'])),
            ('clipboard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['filer.Clipboard'])),
        ))
        db.send_create_signal(u'filer', ['ClipboardItem'])

        # Adding model 'Image'
        db.create_table(u'filer_image', (
            (u'file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['filer.File'], unique=True, primary_key=True)),
            ('_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date_taken', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('default_alt_text', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('default_caption', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('must_always_publish_author_credit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('must_always_publish_copyright', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('subject_location', self.gf('django.db.models.fields.CharField')(default=None, max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal('filer', ['Image'])


    def backwards(self, orm):
        # Removing unique constraint on 'Folder', fields ['parent', 'name']
        db.delete_unique(u'filer_folder', ['parent_id', 'name'])

        # Deleting model 'Folder'
        db.delete_table(u'filer_folder')

        # Deleting model 'FolderPermission'
        db.delete_table(u'filer_folderpermission')

        # Deleting model 'File'
        db.delete_table(u'filer_file')

        # Deleting model 'Clipboard'
        db.delete_table(u'filer_clipboard')

        # Deleting model 'ClipboardItem'
        db.delete_table(u'filer_clipboarditem')

        # Deleting model 'Image'
        db.delete_table(u'filer_image')


    models = {
        u'actor.actor': {
            'Meta': {'object_name': 'Actor', 'db_table': "u'actor'"},
            'actor_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actor.ActorType']"}),
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['locations.Location']", 'symmetrical': 'False'}),
            'bitflag': ('core.models.fields.HSBitflagField', [], {'default': '0', 'bitflagmask': '47'}),
            'contactable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '75', 'blank': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_actor.actor_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"})
        },
        u'actor.actortype': {
            'Meta': {'object_name': 'ActorType', 'db_table': "u'actor_type'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'filer.clipboard': {
            'Meta': {'object_name': 'Clipboard'},
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'in_clipboards'", 'symmetrical': 'False', 'through': u"orm['filer.ClipboardItem']", 'to': u"orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'filer_clipboards'", 'to': u"orm['hsauth.User']"})
        },
        u'filer.clipboarditem': {
            'Meta': {'object_name': 'ClipboardItem'},
            'clipboard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.Clipboard']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.File']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'all_files'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'owned_files'", 'null': 'True', 'to': u"orm['hsauth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_filer.file_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'filer.folder': {
            'Meta': {'ordering': "(u'name',)", 'unique_together': "((u'parent', u'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_owned_folders'", 'null': 'True', 'to': u"orm['hsauth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['filer.Folder']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'filer.folderpermission': {
            'Meta': {'object_name': 'FolderPermission'},
            'can_add_children': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'can_edit': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'can_read': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'everybody': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['filer.Folder']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_folder_permissions'", 'null': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filer_folder_permissions'", 'null': 'True', 'to': u"orm['hsauth.User']"})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': [u'filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'hsauth.user': {
            'Meta': {'object_name': 'User', '_ormbases': [u'actor.Actor']},
            u'actor_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['actor.Actor']", 'unique': 'True', 'primary_key': 'True'}),
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "u'u'", 'max_length': '1'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_security_number': ('django.db.models.fields.CharField', [], {'max_length': '172', 'null': 'True', 'blank': 'True'})
        },
        u'locations.country': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Country', 'db_table': "u'country'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number_regex': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'phone_prefix': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'postal_code_regex': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'second_level_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'third_level_name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'locations.county': {
            'Meta': {'ordering': "(u'country', u'name', u'identifier')", 'object_name': 'County', 'db_table': "u'county'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'counties'", 'to': u"orm['locations.Country']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'locations.location': {
            'Meta': {'object_name': 'Location', 'db_table': "u'location'"},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'locations'", 'to': u"orm['locations.PostalCode']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'valid_until': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True'})
        },
        u'locations.municipality': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Municipality', 'db_table': "u'municipality'"},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'municipalities'", 'to': u"orm['locations.County']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'locations.postalcode': {
            'Meta': {'object_name': 'PostalCode', 'db_table': "u'postal_code'"},
            'address_type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'postal_codes'", 'to': u"orm['locations.Municipality']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'urban_district': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'postal_codes'", 'null': 'True', 'to': u"orm['locations.UrbanDistrict']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'locations.urbandistrict': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'UrbanDistrict'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.CharField', [], {'default': "u'a'", 'max_length': '1', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'municipality': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'urban_districts'", 'to': u"orm['locations.Municipality']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['filer']