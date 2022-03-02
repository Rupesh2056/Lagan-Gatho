# Generated by Django 4.0.1 on 2022-01-28 07:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.UUIDField(default=uuid.uuid4)),
                ('slug', models.SlugField()),
                ('age', models.PositiveIntegerField()),
                ('marital_status', models.CharField(choices=[('NM', 'Never Married'), ('D', 'Divorced'), ('AD', 'Awaiting Divorce')], max_length=5)),
                ('DOB', models.DateField()),
                ('religion', models.CharField(choices=[('H', 'Hindu'), ('M', 'Muslim'), ('C', 'Christian'), ('B', 'Buddhist'), ('S', 'Sikh'), ('J', 'Jain'), ('JW', 'Jewish'), ('O', 'Other'), ('N', 'No Religion')], max_length=5)),
                ('location', models.CharField(choices=[('achham', 'Achham'), ('arghakhanchi', 'Arghakhanchi'), ('baglung', 'Baglung'), ('baitadi', 'Baitadi'), ('bajhang', 'Bajhang'), ('bajura', 'Bajura'), ('banke', 'Banke'), ('bara', 'Bara'), ('bardiya', 'Bardiya'), ('bhaktapur', 'Bhaktapur'), ('bhojpur', 'Bhojpur'), ('chitwan', 'Chitwan'), ('dadeldhura', 'Dadeldhura'), ('dailekh', 'Dailekh'), ('dang', 'Dang'), ('darchula', 'Darchula'), ('dhading', 'Dhading'), ('dhankuta', 'Dhankuta'), ('dhanusa', 'Dhanusa'), ('dolakha', 'Dolakha'), ('dolpa', 'Dolpa'), ('doti', 'Doti'), ('gorkha', 'Gorkha'), ('gulmi', 'Gulmi'), ('humla', 'Humla'), ('ilam', 'Ilam'), ('jajarkot', 'Jajarkot'), ('jhapa', 'Jhapa'), ('jumla', 'Jumla'), ('kailali', 'Kailali'), ('kalikot', 'Kalikot'), ('kanchanpur', 'Kanchanpur'), ('kapilvastu', 'Kapilvastu'), ('kaski', 'Kaski'), ('kathmandu', 'Kathmandu'), ('kavrepalanchok', 'Kavrepalanchok'), ('khotang', 'Khotang'), ('lalitpur', 'Lalitpur'), ('lamjung', 'Lamjung'), ('mahottari', 'Mahottari'), ('makawanpur', 'Makawanpur'), ('manang', 'Manang'), ('morang', 'Morang'), ('mugu', 'Mugu'), ('mustang', 'Mustang'), ('myagdi', 'Myagdi'), ('nawalpur', 'Nawalpur'), ('nuwakot', 'Nuwakot'), ('okhaldhunga', 'Okhaldhunga'), ('palpa', 'Palpa'), ('panchthar', 'Panchthar'), ('parasi', 'Parasi'), ('parbat', 'Parbat'), ('parsa', 'Parsa'), ('pyuthan', 'Pyuthan'), ('ramechhap', 'Ramechhap'), ('rasuwa', 'Rasuwa'), ('rautahat', 'Rautahat'), ('rolpa', 'Rolpa'), ('rukum', 'Rukum'), ('rukum paschim', 'Rukum Paschim'), ('rupandehi', 'Rupandehi'), ('salyan', 'Salyan'), ('sankhuwasabha', 'Sankhuwasabha'), ('saptari', 'Saptari'), ('sarlahi', 'Sarlahi'), ('sindhuli', 'Sindhuli'), ('sindhupalchok', 'Sindhupalchok'), ('siraha', 'Siraha'), ('solukhumbu', 'Solukhumbu'), ('sunsari', 'Sunsari'), ('surkhet', 'Surkhet'), ('syangja', 'Syangja'), ('tanahu', 'Tanahu'), ('taplejung', 'Taplejung'), ('terhathum', 'Terhathum'), ('udayapur', 'Udayapur')], max_length=20)),
                ('family_type', models.CharField(choices=[('J', 'Joint'), ('N', 'Nuclear')], max_length=1)),
                ('Rashi', models.CharField(choices=[('mesh', 'Mesh'), ('bris', 'Bris'), ('mithun', 'Mithun'), ('karkat', 'Karkat'), ('singha', 'Singha'), ('kanya', 'Kanya'), ('tula', 'Tula'), ('brischik', 'Brischik'), ('dhanu', 'Dhanu'), ('makar', 'Makar'), ('kumba', 'Kumba'), ('min', 'Min')], max_length=10)),
                ('education', models.CharField(choices=[('slc', 'Slc'), ('high School', 'High School'), ('bachelors', 'Bachelors'), ('master', 'Master')], max_length=20)),
            ],
        ),
    ]
