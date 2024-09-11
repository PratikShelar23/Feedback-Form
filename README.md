# Feedback Form Project

## Overview
This is a feedback form application built using Django for the backend, React.js for the frontend, and Tailwind CSS for styling. The application stores data in a MySQL database and has been tested using Postman.

## Features
- User-friendly feedback form
- Responsive design using Tailwind CSS
- API endpoints for submitting feedback
- Data stored in MySQL database

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Frontend**: React.js, Tailwind CSS
- **Database**: MySQL
- **Testing**: Postman

## Setup Instructions

### Prerequisites
- Python 3.x
- Node.js and npm
- MySQL

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/PratikShelar23/Feedback-Form.git
   cd Feedback-Form/main

2. Create and activate a virtual environment:

        python -m venv .venv
        .venv\Scripts\activate  # Windows
        source .venv/bin/activate  # macOS/Linux

3. Install the required Python packages:

        pip install -r requirements.txt

4. Set up your database in MySQL and update the DATABASES settings in settings.py:

          DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'feedback',  # Your database name
              'USER': 'root',      # Your database user
              'PASSWORD': 'your_password',  # Your database password
              'HOST': '127.0.0.1',
              'PORT': '3306',
          }
        }
5. Run the Django server:
   
          python manage.py runserver
   
7. Navigate to the frontend folder:
   
          cd frontend
          npm install
          npm start
   
Contributing
Feel free to open issues and submit pull requests.

            
          





