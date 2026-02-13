import frappe
from frappe.model.document import Document


class CurriculumFramework(Document):
    def autoname(self):
        if self.organization and self.academic_year:
            self.name = f"{self.organization}-{self.academic_year}"

    def validate(self):
        if self.valid_from and self.valid_to and self.valid_to < self.valid_from:
            frappe.throw("Valid To must be after Valid From")
