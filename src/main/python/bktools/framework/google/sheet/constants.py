# encoding: utf-8

# Standard Library
from typing import Dict

# 3rd Party Library
# Current Folder
# Current Application

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

URL: Dict[str, str] = dict()
URL['base'] = 'https://sheets.googleapis.com/v4/spreadsheets'
URL['general'] = f"{URL['base']}/%s"
URL['batch_update'] = f"{URL['base']}/%s:batchUpdate"
URL['values'] = f"{URL['general']}/values/%s"
URL['values_batch_get'] = f"{URL['general']}/values:batchGet"
URL['values_batch_update'] = f"{URL['general']}/values:batchUpdate"
