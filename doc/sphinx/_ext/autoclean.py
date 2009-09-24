# Copyright (C) 2009 Osmo Salomaa
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re

def on_autodoc_process_docstring(app, what, name, obj, options, lines):
    """Replace inline ':var:' markup with '.. attribute:' paragraphs."""
    parent = (name.split(".")[-1] if what == "class" else name)
    pattern = r"^:[ci]?var +(\w+): +(.*?)$"
    replacement = r".. attribute:: %s.\1\n\n   \2\n" % parent
    re_var = re.compile(pattern, re.MULTILINE)
    text = re_var.sub(replacement, "\n".join(lines))
    lines[:] = text.split("\n")

def setup(app):
    app.connect("autodoc-process-docstring",
                on_autodoc_process_docstring)

    # Don't add the directive header to classes.
    from sphinx.ext.autodoc import ClassDocumenter
    ClassDocumenter.add_directive_header = lambda: None