## need import pygeoip

readme is [here](https://github.com/appliedsec/pygeoip)

Geoip.dat is from Maxmind

## Quick Documentation ##

Create your GeoIP instance with appropriate access flag. `STANDARD` reads data from disk when needed, `MEMORY_CACHE` loads database into memory on instantiation and `MMAP_CACHE` loads database into memory using mmap.

    import pygeoip
    gi4 = pygeoip.GeoIP('/path/to/GeoIP.dat', pygeoip.MEMORY_CACHE)
    gi6 = pygeoip.GeoIP('/path/to/GeoIPv6.dat', pygeoip.MEMORY_CACHE)

### Country Lookup ###

    >>> gi4.country_code_by_name('google.com')
    'US'
    >>> gi4.country_code_by_addr('64.233.161.99')
    'US'
    >>> gi4.country_name_by_addr('64.233.161.99')
    'United States'
    >>> gi6.country_code_by_name('google.com')
    'IE'
    >>> gi6.country_code_by_addr('2001:7fd::1')
    'EU'
    >>> gi6.country_name_by_addr('2001:7fd::1')
    'Europe'

### Region Lookup ###

    >>> gi = pygeoip.GeoIP('/path/to/GeoIPRegion.dat')
    >>> gi.region_by_name('apple.com')
    {'region_code': 'CA', 'country_code': 'US'}

### City Lookup ###

    >>> gi = pygeoip.GeoIP('/path/to/GeoIPCity.dat')
    >>> gi.record_by_addr('64.233.161.99')
    {
        'city': u'Mountain View',
        'region_code': u'CA',
        'area_code': 650,
        'time_zone': 'America/Los_Angeles',
        'dma_code': 807,
        'metro_code': 'San Francisco, CA',
        'country_code3': 'USA',
        'latitude': 37.41919999999999,
        'postal_code': u'94043',
        'longitude': -122.0574,
        'country_code': 'US',
        'country_name': 'United States',
        'continent': 'NA'
    }
    >>> gi.time_zone_by_addr('64.233.161.99')
    'America/Los_Angeles'

### Organization Lookup ###

    >>> gi = pygeoip.GeoIP('/path/to/GeoIPOrg.dat')
    >>> gi.org_by_name('dell.com')
    'Dell Computer Corporation'

### ISP Lookup ###

    >>> gi = pygeoip.GeoIP('/path/to/GeoIPISP.dat')
    >>> gi.org_by_name('cnn.com')
    'Turner Broadcasting System'

### ASN Lookup ###

    >>> gi = pygeoip.GeoIP('/path/to/GeoIPASNum.dat')
    >>> gi.org_by_name('cnn.com')
    'AS5662 Turner Broadcasting'


