from builtins import str, bytes
import gettext
import logging
import six
import sys


# See http://lxml.de/tutorial.html for the source of the includes
def get_etree(log):
    try:
        from lxml import etree
        log.debug(_("Running with lxml.etree"))
    except ImportError: # pragma: no cover
        try:
            import xml.etree.ElementTree as etree
            log.debug(_("Running with ElementTree"))
        except ImportError:
            try:
                import cElementTree as etree
                log.debug(_("Running with cElementTree"))
            except ImportError:
                try:
                    import elementtree.ElementTree as etree
                    log.debug(_("Running with ElementTree"))
                except ImportError:
                    msg = _("Failed to import ElementTree from any known place")
                    raise ImportError(msg)
    return etree

def install_gettext(app_name, localedir):
    if six.PY2:
        gettext.install(app_name.lower(), localedir=localedir, unicode=1)
    else:
        gettext.install(app_name.lower(), localedir=localedir)
    gettext.bindtextdomain('argparse', localedir)
    gettext.textdomain('argparse')


class Terminal(object):

    def __init__(self, encoding):
        self.encoding = encoding

    def encode(self, msg):
        """Encode strings to W$ terminal with Python2"""
        return str(msg) if sys.stdout.encoding == 'utf-8' else \
            bytes(msg, self.encoding).decode(sys.stdout.encoding)

