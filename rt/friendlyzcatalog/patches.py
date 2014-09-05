# -*- coding: utf-8 -*-

from App.special_dtml import DTMLFile
from Products.ZCatalog.ZCatalog import ZCatalog
from rt.friendlyzcatalog import logger

logger.warning('Patching "Catalog" view')
ZCatalog.manage_catalogView = DTMLFile('dtml/catalogView', globals())

