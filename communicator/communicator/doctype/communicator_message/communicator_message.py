import frappe
from frappe.model.document import Document


class CommunicatorMessage(Document):
    def before_insert(self):
        self.sender = frappe.session.user
        self.sent_at = frappe.utils.now_datetime()

    def validate(self):
        self._ensure_channel_access()

    def _ensure_channel_access(self):
        if not self.channel:
            frappe.throw(frappe._("Channel is required."))
        if not frappe.has_permission("Communicator Channel", ptype="read", doc=self.channel):
            frappe.throw(frappe._("You do not have access to this channel."))

