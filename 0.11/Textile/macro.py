""" @package TextileMacro
    @file macro.py
    @brief The textileMacro class

    Implements Textile syntax WikiProcessor as a Trac macro.
    
    @author Patrick Wagstrom <patrick@wagstrom.net>
    @date December, 2009
    @version 0.11.0
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import Formatter, system_message

from genshi.builder import tag

from re import sub, compile, search, I
from StringIO import StringIO

__all__ = ['TextileMacro']

class TextileMacro(WikiMacroBase):
    """Implements Textile syntax [WikiProcessors WikiProcessor] as a Trac macro."""


    def expand_macro(self, formatter, name, content):
        from textile import textile
        try:
            from textile import textile
            return textile(content)
        except ImportError:
            msg = 'Error importing Python Textile, install it from '
            url = 'http://loopcore.com/python-textile/'
            return system_message(tag(msg, tag.a('here', href="%s" % url), '.'))
