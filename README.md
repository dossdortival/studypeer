# StudyPeer: Peer Study Group Finder

StudyPeer is a full-stack web application built using Django (Python) for the backend and JavaScript for frontend interactivity. The platform helps students find, join, and manage peer-led study groups based on subjects, meeting times, and interests. Users can create study groups, join or leave existing ones, manage group membership, and maintain their profiles. The application is fully mobile-responsive, ensuring usability across all devices.

---

## Features

- User authentication (register, login, logout)
- Create, update, and delete study groups
- Join or leave groups via AJAX without page reloads
- Dashboard showing created and joined groups
- Profile page and profile editing
- Responsive design using Bootstrap
- Backend validations and CSRF protection

---

## Distinctiveness and Complexity

### Why StudyPeer Stands Out

This project satisfies the **distinctiveness and complexity** requirements because it’s distinct from the course's projects and is not a basic CRUD or blog app. Instead, it introduces **social interaction mechanics** between users via study groups. The combination of custom membership logic, AJAX-based group joining/leaving, and a user dashboard creates a dynamic and interactive experience similar to real-world educational platforms.

Key complex features include:

- A **membership system** that handles many-to-many user-group relationships, including join dates and maximum capacity enforcement.
- **AJAX functionality** to asynchronously join or leave groups, improving UX.
- A **dashboard** to dynamically show two sets of data: created vs. joined groups.
- A **profile management system** allowing users to update their details securely.
- Use of **dynamic permissions**, where only group creators can edit/delete their groups, and users can only join groups that are not full.

These elements involve multiple models, advanced querysets, template logic, and asynchronous frontend interactions, making StudyPeer a highly customized and non-trivial web application.

---

## File Overview

### Backend

- `models.py`: Contains `StudyGroup`, `Membership`, and `Subject` models.
- `views.py`: Handles all logic for group CRUD, user profile, dashboard, and AJAX membership actions.
- `urls.py`: Maps URL routes to views including dynamic paths.
- `forms.py`: Contain Django forms for editing profiles or creating groups.
- `admin.py`: Registers models for Django admin interface.

### Frontend Templates

- `layout.html`: Base HTML layout with navbar and Bootstrap.
- `index.html`: Homepage showing featured groups.
- `group_detail.html`: Shows a specific group's information and includes JavaScript buttons for AJAX join/leave.
- `dashboard.html`: Shows groups the user created or joined.
- `profile.html`: Displays current user's information.
- `edit_profile.html`: Form for editing user data.

### JavaScript

- `group_detail.js`: Handles AJAX POST requests for joining and leaving groups, updating the member count dynamically.

### Static Files

- `styles.css`: For custom styling beyond Bootstrap.
- Bootstrap CDN and static files to ensure mobile responsiveness.

---

## How to Run the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dossdortival/studypeer.git
   cd studypeer

2. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

3. **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser

4. **Run the development server:**
    ```bash
    python manage.py runserver

5. **Visit the app at:**
    http://127.0.0.1:8000/

## Additional Notes

- **Security:** CSRF protection and login-required decorators are in place to protect form submissions and private pages.

- **Scalability:** The model structure supports future features such as private groups, invitations, or group chat.

- **Extensibility:** The app could easily integrate email notifications, calendar syncing, or study reminders in the future.


Thank you for reviewing the StudyPeer project!