# StudyPeer - Peer Study Group Finder

StudyPeer is a comprehensive full-stack web application designed to connect students through peer-led study groups. Built with Django for the backend and JavaScript for dynamic frontend interactions, this platform addresses the real-world challenge of academic collaboration by enabling students to discover, create, and manage study groups based on their academic subjects, availability, and learning preferences.

The application provides a seamless user experience where students can register for accounts, create detailed study group listings, browse available groups by subject matter, join groups that match their interests, and manage their participation across multiple groups through an intuitive dashboard interface. The platform emphasizes user autonomy and social interaction while maintaining proper access controls and data integrity.


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

### Distinctiveness from Course Projects

StudyPeer fundamentally differs from all previous course projects in both its core purpose and implementation approach. Unlike the course's social network project (Project 4), StudyPeer is not about general social networking, following users, or sharing posts. Instead, it serves a specific educational purpose by facilitating academic collaboration through structured study groups with defined subjects, capacity limits, and membership management.

The application diverges significantly from the e-commerce project (Project 2) as it contains no buying, selling, auction mechanics, or financial transactions. While both projects involve users interacting with listings, StudyPeer's "listings" are study opportunities rather than commercial products, and the interaction model is collaborative rather than transactional. Users join study groups to participate in shared learning experiences, not to purchase or bid on items.

StudyPeer also distinguishes itself from the wiki project (Project 1) and mail project (Project 3) through its focus on group formation and membership management rather than content creation or communication. The core functionality revolves around matching students with compatible learning opportunities and managing the resulting social academic relationships.

### Technical Complexity

The application demonstrates significant technical complexity through multiple sophisticated components working in harmony. The membership system implements a complex many-to-many relationship between users and study groups that goes beyond simple associations. Each membership tracks join dates, enforces capacity constraints, and maintains referential integrity across multiple database operations. This required implementing custom Django model methods, complex querysets with annotations and aggregations, and careful handling of edge cases like concurrent join attempts.

The AJAX-powered membership management system represents another layer of complexity, requiring seamless coordination between frontend JavaScript and backend Django views. Users can join or leave groups without page refreshes, with real-time updates to member counts, button states, and capacity indicators. This involved implementing proper CSRF handling, JSON response formatting, error handling for various membership scenarios (full groups, already joined, etc.), and ensuring the UI remains consistent with the database state.

The dashboard functionality showcases advanced Django queryset manipulation, as it must efficiently retrieve and categorize a user's groups into "Created" and "Joined" categories while avoiding N+1 query problems. This required using select_related and prefetch_related optimizations, custom annotations, and complex filtering logic to present data efficiently even as the number of users and groups scales.

Permission and access control systems add another dimension of complexity. The application implements granular permissions where only group creators can modify their groups, users can only join groups with available capacity, and various UI elements adapt based on the current user's relationship to each group. This required custom permission checking, conditional template rendering, and secure view implementations that prevent unauthorized access or modifications.

### User Experience Complexity

Beyond technical implementation, StudyPeer addresses complex user experience challenges. The application must present information clearly across different contexts (browsing vs. dashboard vs. detailed views), provide intuitive navigation between related concepts (subjects, groups, memberships), and maintain consistent state across different interaction patterns (page loads vs. AJAX updates).

The responsive design implementation ensures consistent functionality across desktop, tablet, and mobile devices, requiring careful consideration of touch interfaces, variable screen sizes, and different interaction patterns. This complexity extends beyond simple CSS media queries to involve JavaScript behavior adaptations and Django template logic that serves appropriate content for different contexts.

## File Documentation

### Backend Files

**models.py**
This file contains the core data structures that define StudyPeer's functionality. The Subject model stores academic subjects with name and description fields, providing the categorization system for study groups. The StudyGroup model is the central entity, containing fields for title, description, subject (foreign key), creator (foreign key to User), maximum_members integer, created_at timestamp, etc. It includes custom methods like is_full() that checks current membership against capacity, and current_member_count() that efficiently counts current members. The Membership model implements the many-to-many relationship between Users and StudyGroups with additional metadata, storing user, study group, and joined_at fields. This through-table approach allows tracking when users joined groups and enables complex queries about membership history.

**views.py**
The views file handles all application logic across multiple view functions. Starting with user's authentication functionality (login_view, logout_view and register). The index view queries and displays featured study groups with member count annotations. create_group handles both GET requests (displaying the form) and POST requests (processing new group creation with proper validation). group_detail retrieves individual groups with member information and handles the complex logic for determining button states based on current user membership status. join_group and leave_group are AJAX endpoints that process membership changes, validate capacity constraints, prevent duplicate memberships, and return JSON responses with updated counts and status messages. dashboard implements complex querying to separate user-created groups from user-joined groups efficiently. profile and edit_profile handle user account management with proper authentication checks and form validation. Each view includes appropriate authentication decorators, CSRF protection, and error handling.

**urls.py**
Defines the URL routing structure connecting URLs to view functions. Includes both static patterns (dashboard/, profile/, groups/, create/) and dynamic patterns using path converters (<int:group_id>/ for group details, join/, leave/, etc.). The URL configuration supports both human-readable URLs for navigation and API-style endpoints for AJAX operations. Each URL pattern is named to support reverse URL lookup in templates and views, maintaining consistency across the application.

**forms.py**
contains a single Django ModelForm class called StudyGroupForm that handles the creation and editing of study groups. This form is built on Django's ModelForm framework, which automatically generates form fields based on the corresponding StudyGroup model.

**admin.py**
Registers models with Django's admin interface to enable administrative management. Includes admin configurations for better usability for users, subjects, studygroups and memberships.

### Frontend Files

**templates/layout.html**
This template serves as the base layout for the StudyPeer application, defining the overall structure and navigation for other templates to extend. It includes a responsive Bootstrap-based navigation bar with dynamic links based on user authentication status, displaying options like "Browse Groups," "Dashboard," "Log Out" for authenticated users, or "Log In" and "Register" for unauthenticated users. The template links to Bootstrap 4.4.1 CSS and a custom stylesheet (styles.css) for consistent styling. It features a main content area that handles dynamic message alerts and a placeholder for specific page content via the `body` block. A footer with a copyright notice is included, ensuring a professional and cohesive layout across the site.

**templates/login.html**
The login page template that extends layout.html and provides a simple, user-friendly interface for user authentication. It includes a form with fields for username and password, styled with Bootstrap classes for a clean, responsive design. The form supports CSRF protection and handles error messages dynamically through a conditional message display. A clear call-to-action button submits the login request, and a link to the registration page is provided for users without an account, ensuring a smooth navigation flow.

**templates/register.html**
The registration page template that extends layout.html, providing a straightforward interface for new user sign-up. It features a form with fields for username, email, password, and password confirmation, styled with Bootstrap classes for a responsive and clean design. The form includes CSRF protection and displays error messages dynamically if registration fails. A prominent "Register" button submits the form, and a link to the login page is provided for existing users, facilitating easy navigation. The template maintains a clear visual hierarchy to guide users through the registration process.

**templates/index.html**
The homepage template that extends layout.html and displays featured study groups. Implements a responsive grid layout using Bootstrap classes, shows group cards with key information (title, subject, member count, creator), and includes clear call-to-action buttons for viewing details or joining groups. The template handles empty states gracefully when no groups exist and provides visual hierarchy to guide user attention to important information.

**templates/group_list.html**
The study groups listing template that extends layout.html, displaying a list of available study groups. It presents each group as a clickable link to its detail page, showing the group’s title and associated subject name in an unordered list. The template uses a simple, clean layout to ensure clarity and ease of navigation. A horizontal rule separates the group list from a conditional section: authenticated users see a "Create New Group" button styled with Bootstrap, while unauthenticated users are prompted with a message and a link to the login page to create or join groups, enhancing user engagement and access control.

**templates/group_detail.html**
A complex template for displaying individual study group information with interactive elements. Shows comprehensive group details including description, subject, creator information, current member count vs. capacity. Includes conditional rendering of join/leave buttons based on user authentication status, current membership, and group capacity. Integrates JavaScript for AJAX functionality and provides clear visual feedback for different group states (full, available, already joined).

**templates/group_confirm_delete.html**
The group delete confirmation template that extends layout.html, designed to confirm a user’s intent to delete a specific study group. It displays the group’s title in a heading and includes a prompt asking for confirmation. The template features a form with CSRF protection, containing a "Confirm Delete" button styled with Bootstrap’s danger class to indicate the irreversible action, and a "Cancel" button styled as secondary that links back to the group’s detail page. The layout is clear and focused, ensuring users understand the action they are about to take.

**templates/group_form.html**
The study group form template that extends layout.html, used for creating or updating a study group. It displays a heading with a dynamic `action` variable defined in the create_group function as "Create" and the update_group function as "Update" to indicate the form’s purpose. The template includes a form with CSRF protection, rendering form fields using Django’s `form.as_p` method for a simple, paragraph-based layout. A "Submit" button, styled with Bootstrap’s success class, is labeled with the `action` value to maintain consistency. 

**templates/dashboard.html**
Presents user-specific information in an organized dashboard layout. Displays two distinct sections for groups the user created versus groups they joined, each with appropriate management options. Created groups section includes edit and delete functionality, while joined groups section focuses on easy access and leave options. The template handles empty states for new users and provides clear visual organization using Bootstrap components.

**templates/profile.html** and **templates/edit_profile.html**
Profile management templates that handle user account information display and modification. Profile.html presents current user information in a clean, readable format with navigation to editing functionality. Edit_profile.html provides a comprehensive form interface with proper field labeling, validation error display, and user-friendly form controls. Both templates maintain consistent styling and provide clear navigation back to other sections.

**static/group_detail.js**
Implements sophisticated AJAX functionality for joining and leaving study groups without page refreshes. Handles click events on join/leave buttons, constructs proper AJAX requests with CSRF token handling, processes JSON responses from the backend, and updates the UI dynamically based on response data. The script manages button state changes, member count updates, error message display, and maintains UI consistency. Includes proper error handling for network issues, server errors, and edge cases like groups becoming full during the request process.

**static/styles.css**
contains custom CSS rules that enhance the visual presentation and layout structure of the StudyPeer application beyond Bootstrap's default styling.

## How to Run the Application

### Prerequisites
- Python 3.8 or higher
- Git for cloning the repository
- A command line interface (Terminal, Command Prompt, or PowerShell)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dossdortival/studypeer.git
   cd studypeer
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv studypeer_env
   source studypeer_env/bin/activate  # On Windows: studypeer_env\Scripts\activate
   ```


3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Administrative User**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account for accessing the Django admin interface.

6. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000/`

### Initial Setup
Upon first access, you can:
- Register a new user account through the registration page
- Login with your created account
- Access the admin interface at `http://127.0.0.1:8000/admin/` using your superuser credentials
- Create some initial subjects through the admin interface to populate the subject dropdown.


## Additional Information

### Database Design Considerations
The application uses Django's ORM with SQLite for development, but the model design supports easy migration to PostgreSQL or MySQL for production deployment. Foreign key relationships are properly indexed, and the Membership through-table enables efficient querying of user-group relationships without sacrificing data integrity.

### Security Features
StudyPeer implements multiple security measures including CSRF protection on all forms, login required decorators on protected views, proper user authentication checks before displaying sensitive information, and SQL injection prevention through Django's ORM. User input is validated both on the frontend and backend to prevent malicious data submission.

### Performance Optimizations
The application includes several performance optimizations such as database query optimization using select_related and prefetch_related, efficient counting operations using annotations rather than Python loops, and minimal database queries per page through careful query planning. AJAX operations reduce server load by updating only necessary page elements.

### Future Enhancement Possibilities
The current architecture supports several potential enhancements including email notifications for group updates, calendar integration for scheduling study sessions, private messaging between group members, file sharing capabilities for study materials, and integration with learning management systems. The modular design and clear separation of concerns make these additions straightforward to implement.

### Testing Considerations
While not included in the current submission, the application structure supports comprehensive testing through Django's testing framework. Models include validation logic that can be unit tested, views are designed with clear input/output expectations, and the AJAX functionality can be tested through automated browser testing tools.


Thank you for reviewing the StudyPeer project!