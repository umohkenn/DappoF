import frappe


def after_install():
    ensure_module()
    ensure_roles()
    ensure_workspace()


def ensure_module():
    if not frappe.db.exists("Module Def", "Communicator"):
        module = frappe.new_doc("Module Def")
        module.module_name = "Communicator"
        module.app_name = "communicator"
        module.save(ignore_permissions=True)


def ensure_roles():
    for role_name in ("Communicator User", "Communicator Admin"):
        if not frappe.db.exists("Role", role_name):
            role = frappe.new_doc("Role")
            role.role_name = role_name
            role.desk_access = True
            role.save(ignore_permissions=True)


def ensure_workspace():
    if frappe.db.exists("Workspace", {"name": "Communicator"}):
        return

    workspace = frappe.new_doc("Workspace")
    workspace.title = "Communicator"
    workspace.name = "Communicator"
    workspace.content = None
    workspace.module = "Education"
    workspace.public = 1
    workspace.for_user = ""
    workspace.parent_page = "Education"
    workspace.append(
        "links",
        {
            "label": "Communicator Channels",
            "type": "DocType",
            "name": "Communicator Channel",
        },
    )
    workspace.append(
        "links",
        {
            "label": "Communicator Messages",
            "type": "DocType",
            "name": "Communicator Message",
        },
    )
    workspace.save(ignore_permissions=True)

