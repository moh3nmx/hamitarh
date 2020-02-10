from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    regex=r'^\+?\d{4,15}$',
    message="Phone number must be numeric (except an optional `+` at the start) and including between 4 and 15 digits",
    code='nomatch'
)

def get_numeric_validator(min_length=0, max_length=10):
    return RegexValidator(
        regex=r'^\d{%s,%s}$' % (min_length, max_length),
        message="This field can only contain between %s and %s digits" % (min_length, max_length),
        code='nomatch'
    )
