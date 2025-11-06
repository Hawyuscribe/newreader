# Neurology MCQ Reader - Django Application

This is a Django-based application for managing and studying neurology MCQs. The application allows users to:

- Browse MCQs by subspecialty
- Create flashcards for spaced repetition
- Generate AI explanations using OpenAI
- Track study progress
- Import MCQs from text files
- Bookmark and add notes to MCQs

## Setup Instructions

1. **Activate the virtual environment**
   ```bash
   source ../venv/bin/activate
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the project**
   ```bash
   ./init_django_project.sh
   ```
   This will:
   - Create database migrations
   - Apply the migrations
   - Set up static files
   - Migrate data from the old database
   - Create a superuser

4. **Run the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - Open your browser and go to http://127.0.0.1:8000/
   - Login with:
     - Username: demo
     - Password: demo
   - Admin interface: http://127.0.0.1:8000/admin/
     - Username: admin
     - Password: admin

## Project Structure

- **mcq/** - The main Django app
  - **models.py** - Database models (MCQ, Bookmark, Flashcard, Note)
  - **views.py** - View functions for handling requests
  - **urls.py** - URL routing
  - **admin.py** - Admin interface configuration
  - **openai_integration.py** - Integration with OpenAI API

- **templates/mcq/** - HTML templates
- **static/** - Static files (CSS, JS, images)
- **neurology_mcq/** - Project settings
- **migrate_data.py** - Script to migrate data from the old database

## Features

- **Dashboard**: Overview of subspecialties and progress
- **MCQ Browser**: Filter and browse MCQs by subspecialty
- **Flashcard System**: Spaced repetition for efficient learning
- **AI Explanations**: OpenAI-powered explanations for MCQs
- **User Authentication**: Secure login system
- **Admin Interface**: Manage MCQs, users, and more
- **Bookmarks and Notes**: Personal study aids
- **Search**: Full-text search across all MCQs