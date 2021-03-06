# The RDSI - ALLOCATION REQUEST MANAGEMENT SYSTEM
# Copyright (C) 2013 Queensland Cyber Infrastructure Foundation (http://www.qcif.edu.au/)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from com.googlecode.fascinator.common import FascinatorHome
import sys, os
sys.path.append(os.path.join(FascinatorHome.getPath(), "lib", "jython", "display")) 

from Dashboard import Dashboard

class HomeData(Dashboard):
    def __init__(self):
        pass

    def __activate__(self, context):
        self.activate(context, context["page"].getPortal().recordsPerPage)
        auth = context["page"].authentication
        if auth.has_role("admin"):
            self.selected = "admin"
        elif auth.has_role("committee"):
            self.selected = "committee"
        elif auth.has_role("requester"):
            self.selected = "requester"
        elif  auth.has_role("reviewer"):
            self.selected = "reviewer"
        elif auth.has_role("provisioner"):
            self.selected = "provisioner"
