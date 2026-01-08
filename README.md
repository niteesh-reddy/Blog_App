# Geopolitics Blog

A Django-based blogging platform focused on Geopolitics Insights.

## Features
- **User Authentication**: Secure Login, Registration, and Logout.
- **User Profiles**: Profile management with image uploads and default avatars.
- **Blog Management**: Create, Read, Update, and Delete (CRUD) blog posts.
- **Geopolitics Theme**: Curated sidebar with insights and external resources on global affairs.
- **Responsive Design**: Built with Bootstrap 4 for mobile-friendly layouts.

## Project Structure
- `blogpro/`: Main Django project configuration.
- `blog/`: App handling blog posts and home page.
- `users/`: App handling user authentication and profiles.
- `media/`: User-uploaded content (profile pictures).

## Setup Instructions

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    ```bash
    pip install django django-crispy-forms crispy-bootstrap4 pillow
    ```
3.  **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
4.  **Run the server**:
    ```bash
    python manage.py runserver
    ```
5.  **Access the application**:
    Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Key Fixes & Improvements
- Fixed `TemplateSyntaxError` by installing `crispy-bootstrap4`.
- Fixed profile image display by configuring `MEDIA_ROOT`.
- Fixed `NoReverseMatch` on Profile page.
- Fixed `Method Not Allowed` on Logout.
- Populated with initial Geopolitics dataset.
