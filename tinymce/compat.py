# encoding: utf-8

try:
	from django.utils import simplejson
except ImportError:
	import json as simplejson
