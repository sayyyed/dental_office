# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dental_office"
app_title = "Dental Office"
app_publisher = "sayed"
app_description = "Dental Office"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sayed@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dental_office/css/dental_office.css"
# app_include_js = "/assets/dental_office/js/dental_office.js"

# include js, css files in header of web template
# web_include_css = "/assets/dental_office/css/dental_office.css"
# web_include_js = "/assets/dental_office/js/dental_office.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dental_office.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dental_office.install.before_install"
# after_install = "dental_office.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dental_office.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dental_office.tasks.all"
# 	],
# 	"daily": [
# 		"dental_office.tasks.daily"
# 	],
# 	"hourly": [
# 		"dental_office.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dental_office.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dental_office.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dental_office.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dental_office.event.get_events"
# }

