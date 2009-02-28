# Copyright (C) 2006-2009 Osmo Salomaa
#
# This file is part of NFO Viewer.
#
# NFO Viewer is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# NFO Viewer is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# NFO Viewer. If not, see <http://www.gnu.org/licenses/>.

import nfoview
import os


class TestBuilderDialog(nfoview.TestCase):

    def setup_method(self, method):

        path = os.path.join(nfoview.DATA_DIR, "preferences-dialog.ui")
        self.dialog = nfoview.BuilderDialog(path)
        self.dialog.show()

    def test___getattr__(self):

        self.dialog.hide()
        self.dialog.show()

    def test___init__(self):

        assert hasattr(self.dialog, "_builder")
        assert hasattr(self.dialog, "_dialog")

    def test___setattr__(self):

        self.dialog.props.visible = False
        self.dialog.props.visible = True
        self.dialog.props.visible = False

    def test_run(self):

        self.dialog._dialog.run = lambda: None
        self.dialog.run()
