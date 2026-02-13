import frappe
from frappe.model.document import Document


class HomeworkSubmission(Document):
    pass


def validate_grade_rules(doc, method=None):
    if doc.score is not None and doc.max_score is not None and doc.score > doc.max_score:
        frappe.throw("Score cannot exceed max score")

    if doc.grading_status == "Graded" and doc.score is None:
        frappe.throw("Score is required for graded submissions")
