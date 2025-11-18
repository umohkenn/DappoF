from frappe import _


def get_data():
    return [
        {
            "module_name": "Communicator",
            "category": "Education",
            "label": _("Communicator"),
            "color": "blue",
            "icon": "octicon octicon-comment-discussion",
            "type": "module",
            "description": _("Education-first messenger for channels and announcements."),
        }
    ]
