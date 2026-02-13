import frappe
from frappe.model.document import Document


class UnitPlan(Document):
    def validate(self):
        if self.end_date and self.start_date and self.end_date < self.start_date:
            frappe.throw("Unit end date cannot be earlier than start date")
