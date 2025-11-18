from communicator import __version__ as app_version

app_name = "communicator"
app_title = "Communicator"
app_publisher = "DappoF"
app_description = "Education-focused messaging module"
app_email = "support@example.com"
app_license = "MIT"

# Desk assets are served directly from public without a build step
app_include_css = ["/assets/communicator/css/communicator.css"]
app_include_js = ["/assets/communicator/js/communicator.js"]

# Installation
after_install = "communicator.install.after_install"

# Fixtures ensure the module record travels with the app
fixtures = [
    {
        "dt": "Module Def",
        "filters": {"module_name": "Communicator"},
    },
]
