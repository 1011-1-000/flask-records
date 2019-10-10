import sys

PY2 = sys.version_info[0] == 2

if not PY2:
    def iterkeys(d): return iter(d.keys())
    def itervalues(d): return iter(d.values())
    def iteritems(d): return iter(d.items())

    from inspect import getfullargspec as getargspec
else:
    def iterkeys(d): return d.iterkeys()
    def itervalues(d): return d.itervalues()
    def iteritems(d): return d.iteritems()

    from inspect import getargspec
