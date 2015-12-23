# -*- coding: utf-8 -*-
import pytz

from datetime import datetime


def get_utc_crontab_kwargs(**kwargs):
    """
    Return a celery crontab parameter dictionary converting the given year,
    month, day, hour, and minute kwargs from the local Mexico City time to UTC.

    Example:
        get_utc_crontab_kwargs(hour=0, minute=0)
        >>> {'hour': 5, 'minute': 0}

        get_utc_crontab_kwargs(2014, 12, 25, 0, 0)
        >>> {'mont_of_year': 12, 'day_of_month': 25, 'hour': 6, 'minute': 0}
    """
    # Available parameters to be returned.
    AVAILABLE = ['month', 'day', 'hour', 'minute']

    # Celery crontab parameter name replacements.
    REPLACEMENTS = {
        'month': 'month_of_year',
        'day': 'day_of_month'
    }

    # Mexico city timezone.
    MX_TZ = pytz.timezone('America/Mexico_City')

    # Get the current datetime.
    now = datetime.utcnow().replace(tzinfo=pytz.utc)

    # Replace the current datetime data with the given kwarg parameters.
    now = now.replace(**kwargs)

    # Create a new localized datetime object with the specified data.
    dt = datetime(now.year, now.month, now.day, now.hour, now.minute)
    mx_dt = MX_TZ.localize(dt)

    # Tranform the localized datetime to UTC.
    utc_dt = mx_dt.astimezone(pytz.utc)

    # Return only the available parameters.
    print(dict((
        (REPLACEMENTS.get(key, key), getattr(utc_dt, key)) for
        key, value in kwargs.iteritems() if key in AVAILABLE
    ))
    )
    return dict((
        (REPLACEMENTS.get(key, key), getattr(utc_dt, key)) for
        key, value in kwargs.iteritems() if key in AVAILABLE
    ))
