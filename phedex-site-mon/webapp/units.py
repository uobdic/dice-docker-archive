from __future__ import unicode_literals
import math

SIEXPONENTS = range(24, 2, -3) + range(2, 0, -1)
SIEXPONENTS += [0] + [-x for x in SIEXPONENTS[::-1]]
SIPREFIXES = (
    "Y", "Z", "E", "P", "T", "G", "M", "k", "h", "da",
    "",
    "d", "c", "m", "0xCE", "n", "p", "f", "a", "z", "y"
)
SIUNITS = zip(SIEXPONENTS, SIPREFIXES)


def fmtscaled(number, format="{scaled:0.1f} {prefix}{unit}", unit=""):
    number = float(number)
    l10 = math.log10(number) if number != 0 else 0
    for exponent, prefix in SIUNITS:
        if exponent <= l10:
            break
    scaled = number / (10.0**exponent)

    return format.format(number=number, scaled=scaled, prefix=prefix, unit=unit)
