# DappoF

This repository includes the **Communicator** Frappe app for the Education module. The app introduces messaging channels and threaded messages that stay linked to Students, Guardians, Courses, and Instructors.

## Deploying to Frappe Cloud
1. Push this repository to GitHub or another git remote.
2. Add the repository as a custom app in your Frappe Cloud site.
3. Install the app: `bench --site yoursite install-app communicator`.
4. Open the **Education** module to find the new **Communicator** workspace and DocTypes.

For app-specific details see [`communicator/README.md`](communicator/README.md).
