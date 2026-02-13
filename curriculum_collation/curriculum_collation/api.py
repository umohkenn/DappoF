import frappe


def workspace_has_permission() -> bool:
    return bool(frappe.has_permission("Curriculum Framework", ptype="read"))


@frappe.whitelist()
def curriculum_overview(filters=None):
    """Aggregated metrics used by Curriculum Hub."""
    framework_count = frappe.db.count("Curriculum Framework")
    active_courses = frappe.db.count("Course Plan", {"status": "Active"})
    weekly_schemes = frappe.db.count("Scheme of Work")
    pending_grading = frappe.db.count("Homework Submission", {"grading_status": "Submitted"})

    return {
        "framework_count": framework_count,
        "active_courses": active_courses,
        "weekly_schemes": weekly_schemes,
        "pending_grading": pending_grading,
    }
