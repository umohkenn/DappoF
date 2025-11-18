# Communicator

Communicator is a lightweight messaging extension for the Frappe Education module. It introduces channels and threaded messages with links back to Education records (students, instructors, courses, and guardians) so conversations stay context-aware, and it bundles a Messenger desk page styled after the classic Gibbon UI.

## Installation
1. Push this repository to your GitHub account and add it as a custom app in Frappe Cloud.
2. Install the app on your site: `bench --site yoursite install-app communicator`.
3. Assign roles to users (Educator, Student, Guardian, or System Manager) and open the **Communicator** workspace under Education. Launch the **Communicator Messenger** page from that workspace to chat in real time with the Communicator Channel and Communicator Message DocTypes.

## Included DocTypes
- **Communicator Channel**: Defines audience, privacy, and links to Education entities.
- **Communicator Message**: Threaded messages with optional file attachments, notifications, and reply-to threading.

## Notes
The app registers a Communicator entry inside the Education module sidebar and seeds a workspace plus default roles during install.
