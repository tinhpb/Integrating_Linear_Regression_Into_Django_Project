# Generated by Django 2.1.4 on 2018-12-18 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_bed', models.IntegerField()),
                ('year_built', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018)], default=2018, verbose_name='year')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('num_room', models.IntegerField()),
                ('num_bath', models.IntegerField()),
                ('living_area', models.FloatField()),
                ('property_type', models.IntegerField()),
                ('num_parking', models.IntegerField()),
                ('accessible_buildings', models.IntegerField()),
                ('family_quality', models.IntegerField()),
                ('art_expos', models.IntegerField()),
                ('emergency_shelters', models.IntegerField()),
                ('emergency_water', models.IntegerField()),
                ('Facilities', models.IntegerField()),
                ('fire_stations', models.IntegerField()),
                ('Cultural', models.IntegerField()),
                ('Monuments', models.IntegerField()),
                ('police_stations', models.IntegerField()),
                ('Vacant', models.IntegerField()),
                ('Free_Parking', models.IntegerField()),
                ('askprice', models.IntegerField()),
            ],
        ),
    ]
