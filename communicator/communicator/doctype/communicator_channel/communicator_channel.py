import frappe
from frappe.model.document import Document


class CommunicatorChannel(Document):
    def validate(self):
        self._set_education_context()

    def _set_education_context(self):
        if self.channel_type == "Class" and not self.student_group:
            frappe.throw(frappe._("Student Group is required for class channels"))
        if self.channel_type == "Guardians" and not self.guardian:
            frappe.throw(frappe._("Guardian is required for guardian channels"))
        if self.channel_type == "Staff" and not self.instructor:
            frappe.throw(frappe._("Instructor is required for staff channels"))

