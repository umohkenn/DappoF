# Communicator app scaffolding

This repository does not yet contain a Frappe site or app code. Use the following steps to scaffold a Frappe app named **Communicator** and link it to the Education module with a new menu entry.

## 1) Scaffold the Communicator app
1. Ensure you have a working Frappe bench (v14+ recommended).
2. Create the app:
   ```bash
   bench new-app communicator
   ```
3. Install it on your site (replace `mysite.local` with your site):
   ```bash
   bench --site mysite.local install-app communicator
   ```

## 2) Add the Education module dependency
In `communicator/hooks.py` ensure the app loads after Education so we can link DocTypes:
```python
# communicator/hooks.py
required_apps = ["education"]
```

## 3) Define a Communicator Module Def
Create a new Module Def so the menu entry appears under Education:
```bash
bench --site mysite.local execute frappe.core.doctype.module_def.module_def.create_module_definition --kwargs '{"module_name": "Communicator", "app_name": "communicator", "package_name": "communicator"}'
```

## 4) Create DocTypes for messaging
Minimum DocTypes (all under the Communicator module):
- **Message Thread**: fields for subject, participants (Link to `Student`, `Guardian`, `Instructor`, `Employee`), last message time, and status (Open/Closed).
- **Message**: child of Message Thread with sender (Link to `User`), body (Text Editor), attachments (Table MultiSelect to `File`), `seen_by` (Table MultiSelect to `User`), and timestamps.
- **Thread Participant**: child table to track each linked participant type and permissions.

Set role permissions so Education roles (Student, Instructor, Advisor, Guardian) can read/post in threads that include them.

## 5) Desk menu entry under Education
Add a desk shortcut so users find Communicator inside Education. Append to `communicator/config/desktop.py`:
```python
# communicator/config/desktop.py
from frappe import _

def get_data():
    return [
        {
            "module_name": "Communicator",
            "category": "Education",
            "label": _("Communicator"),
            "color": "orange",
            "icon": "octicon octicon-comment-discussion",
            "type": "module",
            "doctype": "Message Thread",
        }
    ]
```

## 6) Module onboarding and menu items
Create a module onboard config to surface common actions:
```python
# communicator/config/communicator.py
from frappe import _

def get_data():
    return {
        "fieldname": "message_thread",
        "transactions": [
            {"label": _("Messaging"), "items": ["Message Thread", "Message"]},
        ],
    }
```
Reference this in `hooks.py`:
```python
# communicator/hooks.py
app_name = "communicator"
app_title = "Communicator"
app_publisher = "Your Name"
app_description = "Education messenger compatible with Gibbon"
app_license = "MIT"
onboarding_module = "communicator"
```

## 7) Education context linking
- Use Link fields to existing Education DocTypes (Student, Course, Program Enrollment) on Message Thread.
- Add a Notification Badge hook so Education users see unread counts:
```python
# communicator/notification_config.py
from communicator.utils import get_unread_count

def get_notification_config():
    return {
        "for": "User",
        "notification_count": get_unread_count,
    }
```
Then reference in `hooks.py`:
```python
notification_config = "communicator.notification_config"
```

## 8) Data migration from Gibbon (if source is available)
- Export conversations from Gibbon Messenger (threads, participants, messages, attachments).
- Map users to existing Frappe/Education users and insert Message Thread + Message records via a one-time patch (e.g., `patches/v1_0/import_gibbon_messages.py`).

## 9) UI alignment
- Create a Workspace page inside Education labeled **Communicator** to surface reports, the Thread list, and shortcuts for composing messages.
- Optionally add a Web Form for student/guardian access if using the website portal.

With a Frappe bench available, these snippets will create the Communicator app, register a menu entry under Education, and prepare DocTypes for messaging.
