#! /usr/bin/env python3

import os
import zipfile
import plistlib
import json

# unzip all of plugins and read the Cornucopia.Info into the plugins dictionary which will be used to overwrite the manifest.json

plugins = []

files = os.listdir(os.getcwd() + '/plugins')
for file in files:
	plugin_path = os.getcwd() + '/plugins/' + file
	if zipfile.is_zipfile(plugin_path):
		src = zipfile.ZipFile(plugin_path, 'r')
		for each in src.namelist():
			if each == 'Cornucopia.plist':
				plugin = plistlib.loads(src.read(each))
				plugins.append(plugin)

manifest_str = json.dumps(plugins)

with open(os.getcwd() + '/manifest.json', "w") as file:
    file.write(manifest_str)