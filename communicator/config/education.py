from frappe import _


def get_data():
    return [
        {
            "label": _("Communicator"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Communicator Channel",
                    "description": _("Manage messaging channels for classes, guardians, and clubs."),
                },
                {
                    "type": "doctype",
                    "name": "Communicator Message",
                    "description": _("Send and view threaded messages within channels."),
                },
            ],
        }
    ]
