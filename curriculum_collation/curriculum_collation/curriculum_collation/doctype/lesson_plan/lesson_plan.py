import frappe
from frappe.model.document import Document


class LessonPlan(Document):
    def validate(self):
        if self.duration_minutes and self.duration_minutes <= 0:
            frappe.throw("Duration must be greater than zero")


def mark_scheme_progress(doc, method=None):
    if not doc.scheme_of_work:
        return

    scheme = frappe.get_doc("Scheme of Work", doc.scheme_of_work)
    if scheme.status in {"Draft", "In Progress"}:
        scheme.status = "In Progress"
        scheme.flags.ignore_permissions = True
        scheme.save()
