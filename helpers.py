"""Convert datetimes to and from strings.NASA's dataset provides timestamps (corresponding to UTC).

The `cd_to_datetime` function converts a string, formatted as the `cd` field of
NASA's close approach data, into a Python `datetime`

The `datetime_to_str` function converts a Python `datetime` into a string.
`datetime`s string representations,displays seconds, but NASA's data (and our datetimes!) don't
provide that level of resolution, so the output format also will not.
"""

import datetime


def cd_to_datetime(calendar_date):
    """Convert a NASA-formatted calendar date/time description into a datetime.

    NASA's format,in the `cd` field of close approach data, uses the
    month names. For example, December 31st, 2020 at noon is: 2020-Dec-31 12:00.

    This becomes the Python object `datetime.datetime(2020, 12, 31, 12, 0)`.

    :paramater calendar_date: A calendar date in YYYY-bb-DD hh:mm format.
    :returning `datetime` corresponding to the calendar date and time.
    """
    return datetime.datetime.strptime(calendar_date, "%Y-%b-%d %H:%M")


def datetime_to_str(dt):
    """Convert a naive Python datetime into a human-readable string.

    The default string representation of a datetime includes seconds; however,
    our data isn't that precise, so this function only formats the year, month,
    date, hour, and minute values. Additionally, this function provides the date:
    in the usual ISO 8601 YYYY-MM-DD format to avoid ambiguities with
    locale-specific month names. 
    Parameter dt: A naive Python datetime.
    Returning: That datetime, readable string without seconds.
    """
    return datetime.datetime.strftime(dt, "%Y-%m-%d %H:%M")