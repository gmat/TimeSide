# Generated by Django 2.2 on 2020-02-03 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0007_auto_20191204_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='experiences',
            field=models.ManyToManyField(blank=True, help_text='include other experiences in an experience', related_name='other_experiences', to='timeside_server.Experience', verbose_name='other experiences'),
        ),
        migrations.AlterField(
            model_name='item',
            name='audio_duration',
            field=models.FloatField(blank=True, help_text='Duration of audio track', null=True, verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='item',
            name='external_id',
            field=models.CharField(blank=True, help_text="\n        Provider's id of the audio source.\n        e.g. for Deezer preview: 4763165\n        e.g. for YouTube: oRdxUFDoQe0\n        ", max_length=256, verbose_name='external_id'),
        ),
        migrations.AlterField(
            model_name='item',
            name='external_uri',
            field=models.CharField(blank=True, help_text="\n        Provider's URI of the audio source.\n        e.g. for Deezer preview: http://www.deezer.com/track/4763165\n        e.g. for YouTube: https://www.youtube.com/watch?v=oRdxUFDoQe0\n        ", max_length=1024, verbose_name='external_uri'),
        ),
        migrations.AlterField(
            model_name='item',
            name='provider',
            field=models.ForeignKey(blank=True, help_text='Audio provider (e.g. Deezer, Youtube, etc.)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='timeside_server.Provider', verbose_name='provider'),
        ),
        migrations.AlterField(
            model_name='item',
            name='source_file',
            field=models.FileField(blank=True, help_text='Audio file to process', max_length=1024, upload_to='items/%Y/%m/%d', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='item',
            name='source_url',
            field=models.URLField(blank=True, help_text='URL of a streamable audio source to process', max_length=1024, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='source_access',
            field=models.BooleanField(default=False, help_text='whether or not the audio is\n            freely available from the provider'),
        ),
        migrations.AlterField(
            model_name='result',
            name='file',
            field=models.FileField(blank=True, help_text='\n        non numerical result (image, transcoded audio, etc.)\n        stored in a file\n        ', max_length=1024, upload_to='results/%Y/%m/%d', verbose_name='Output file'),
        ),
        migrations.AlterField(
            model_name='result',
            name='hdf5',
            field=models.FileField(blank=True, help_text='numerical result of the processing stored in an hdf5 file', max_length=1024, upload_to='results/%Y/%m/%d', verbose_name='HDF5 result file'),
        ),
        migrations.AlterField(
            model_name='result',
            name='item',
            field=models.ForeignKey(blank=True, help_text='item on which a preset has been applied', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results', to='timeside_server.Item', verbose_name='item'),
        ),
        migrations.AlterField(
            model_name='result',
            name='preset',
            field=models.ForeignKey(blank=True, help_text='preset applied on an item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='results', to='timeside_server.Preset', verbose_name='preset'),
        ),
        migrations.AlterField(
            model_name='result',
            name='run_time',
            field=models.DurationField(blank=True, help_text='duration of the result computing', null=True, verbose_name='Run time'),
        ),
        migrations.AlterField(
            model_name='result',
            name='status',
            field=models.IntegerField(choices=[(0, 'failed'), (1, 'draft'), (2, 'pending'), (3, 'running'), (4, 'done')], default=1, help_text='\n        status of the task giving the result:\n        failed: 0\n        draft: 1\n        pending: 2\n        running: 3\n        done: 4\n        ', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='selection',
            name='selections',
            field=models.ManyToManyField(blank=True, help_text='include other selections in an selection', related_name='other_selections', to='timeside_server.Selection', verbose_name='other selections'),
        ),
        migrations.AlterField(
            model_name='task',
            name='experience',
            field=models.ForeignKey(blank=True, help_text='experience prossessed in the task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='timeside_server.Experience', verbose_name='experience'),
        ),
        migrations.AlterField(
            model_name='task',
            name='item',
            field=models.ForeignKey(blank=True, help_text='single item prossessed in the task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='timeside_server.Item', verbose_name='item'),
        ),
        migrations.AlterField(
            model_name='task',
            name='selection',
            field=models.ForeignKey(blank=True, help_text='selection prossessed in the task', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to='timeside_server.Selection', verbose_name='selection'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(0, 'failed'), (1, 'draft'), (2, 'pending'), (3, 'running'), (4, 'done')], default=1, help_text="\n        Task's status:\n        failed: {_FAILED}\n        draft: {_DRAFT}\n        pending: {_PENDING}\n        running: {_RUNNING}\n        done: {_DONE}\n        ", verbose_name='status'),
        ),
    ]
