# Curriculum Collation

A Frappe / ERPNext app for collecting multi-organization curricula and translating them into operational classroom delivery:

- Units, lessons, notes, assignments, homework and projects
- Weekly schemes of work
- Student homework submission and grading workflow
- Curriculum status and version tracking
- Desk workspace and script report for planning visibility

## Install in a Frappe Cloud bench

1. Add this repository as a private app in Frappe Cloud.
2. Install app on site:
   - **Apps** → **Install App** → `curriculum_collation`
3. Run migration and build assets:

```bash
bench --site <site_name> migrate
bench --site <site_name> clear-cache
```

## Module Overview

- **Curriculum Framework**: source organization curricula (e.g. Cambridge)
- **Curriculum Topic**: hierarchical curriculum elements
- **Course Plan**: course mapped to framework and topics
- **Unit Plan**: course units
- **Lesson Plan**: daily lesson planning and notes
- **Scheme of Work**: weekly breakdown with objectives and activities
- **Homework Assignment**: assignment details and publication status
- **Homework Submission**: student submission and grading

## Permissions

This app ships with role-based defaults:

- **Curriculum Manager**: full planning lifecycle
- **Teacher**: lesson planning, homework publishing, grading
- **Student**: homework submission only

Adjust role permissions in **Role Permission Manager** to match your implementation.
