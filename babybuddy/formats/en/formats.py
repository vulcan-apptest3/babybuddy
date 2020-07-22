from django.conf import settings
from django.conf.locale.en import formats

# Override the regular locale settings to support 24 hour time.
if settings.USE_24_HOUR_TIME_FORMAT:
    DATETIME_FORMAT = 'N j, Y, H:i:s'
    TIME_FORMAT = 'H:i:s'
    DATETIME_INPUT_FORMATS = [
        '%m/%d/%Y %H:%I:%S'     # '10/25/2006 14:30:59'
    ]
else:
    # These formats are added to support the locale style of Baby Buddy's
    # frontend library, which uses momentjs.
    DATETIME_INPUT_FORMATS = [
        '%m/%d/%Y %I:%M:%S %p',  # '10/25/2006 2:30:59 PM'
        '%m/%d/%Y %I:%M %p',     # '10/25/2006 2:30 PM'
    ]

# Append all other input formats from the base locale.
DATETIME_INPUT_FORMATS.append(formats.DATETIME_INPUT_FORMATS)
