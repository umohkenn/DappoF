app_name = "curriculum_collation"
app_title = "Curriculum Collation"
app_publisher = "DappoF"
app_description = "Curriculum collation, schemes of work and assessment delivery for ERPNext"
app_email = "admin@example.com"
app_license = "MIT"

required_apps = ["erpnext"]

add_to_apps_screen = [
    {
        "name": "curriculum_collation",
        "logo": "/assets/curriculum_collation/images/curriculum-collation.svg",
        "title": "Curriculum Collation",
        "route": "/app/curriculum-hub",
        "has_permission": "curriculum_collation.api.workspace_has_permission",
    }
]

app_include_css = ["/assets/curriculum_collation/css/curriculum_hub.css"]
app_include_js = ["/assets/curriculum_collation/js/curriculum_hub.js"]

doctypes_js = {
    "Lesson Plan": "public/js/lesson_plan.js",
    "Homework Submission": "public/js/homework_submission.js",
}

doc_events = {
    "Homework Submission": {
        "validate": "curriculum_collation.curriculum_collation.doctype.homework_submission.homework_submission.validate_grade_rules"
    },
    "Lesson Plan": {
        "on_submit": "curriculum_collation.curriculum_collation.doctype.lesson_plan.lesson_plan.mark_scheme_progress"
    },
}

fixtures = [
    {"dt": "Workspace", "filters": [["name", "in", ["Curriculum Hub"]]]},
    {"dt": "Role", "filters": [["name", "in", ["Curriculum Manager", "Teacher", "Student"]]]},
]
