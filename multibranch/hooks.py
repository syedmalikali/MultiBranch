from . import __version__ as app_version

app_name = "multibranch"
app_title = "Multibranch"
app_publisher = "Syed Malik Ali"
app_description = "Multi Branch"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "syedmalikali@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/multibranch/css/multibranch.css"
# app_include_js = "/assets/multibranch/js/multibranch.js"

# include js, css files in header of web template
# web_include_css = "/assets/multibranch/css/multibranch.css"
# web_include_js = "/assets/multibranch/js/multibranch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "multibranch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "multibranch.install.before_install"
# after_install = "multibranch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "multibranch.uninstall.before_uninstall"
# after_uninstall = "multibranch.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "multibranch.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"multibranch.tasks.all"
# 	],
# 	"daily": [
# 		"multibranch.tasks.daily"
# 	],
# 	"hourly": [
# 		"multibranch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"multibranch.tasks.weekly"
# 	]
# 	"monthly": [
# 		"multibranch.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "multibranch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "multibranch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "multibranch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"multibranch.auth.validate"
# ]
fixtures = [
{"doctype":"Custom Field"},# “filters”: [["_user_tags", “like”, ("%myApp%")]]},
{"doctype":"Property Setter"},# “filters”: [["_user_tags", “like”, ("%myApp%")]]},
{"doctype":"Client Script"}
#{“doctype”:“Notification”, “filters”: [{“is_standard”:0}]}, ‘Auto Email Report’, “Translation”,
#{“doctype”:“Print Format”, “filters”: [{“module”:“myApp”}]},
#{“doctype”:“Report”, “filters”: [{“module”:“myApp”}]}
]
