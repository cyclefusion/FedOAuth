#!/usr/bin/python
# Copyright (C) 2014 Patrick Uiterwijk <patrick@puiterwijk.org>
#
# This file is part of FedOAuth.
#
# FedOAuth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FedOAuth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FedOAuth.  If not, see <http://www.gnu.org/licenses/>.

# These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

import time

from fedoauth.model import Remembered, OpenIDAssociation

print 'Starting cleanup'
cleared_remembered = Remembered.cleanup()
cleared_openid = OpenIDAssociation.query.filter(
                    (OpenIDAssociation.issued + OpenIDAssociation.lifetime) <
                    time.time()).delete()

print 'Entries cleared from database: %s remembered, %s openid associations' % (cleared_remembered, cleared_openid)
