# Railway Deployment Guide

This application is configured to deploy on Railway.app. Follow these steps to set up your application:

## 1. Deploy from GitHub

1. In Railway, choose "Deploy from GitHub repo"
2. Connect your GitHub account and select the NEWreader repository
3. Railway will automatically detect this as a Django application

## 2. Add a PostgreSQL Database

1. Click "New" → "Database" → "PostgreSQL"
2. Railway will create a PostgreSQL instance and automatically link it to your project

## 3. Configure Environment Variables

Add the following environment variables to your Railway project:

```
OPENAI_API_KEY=your_openai_api_key_here
DJANGO_SETTINGS_MODULE=neurology_mcq.settings_railway
SECRET_KEY=generate_a_random_secret_key_here
RAILWAY_ENVIRONMENT=True
DEBUG=False
```

## 4. Deploy

1. Railway will automatically deploy your application
2. The first deployment will run migrations and collect static files

## 5. Access Your Application

1. Go to the "Settings" tab in your Railway project
2. Look for the generated domain (something like yourapp.railway.app)
3. Click the domain to access your deployed application

## Notes

- The application is configured to use a timeout of 300 seconds for long-running requests
- PostgreSQL connection details are automatically provided by Railway
- CSRF protection is configured to work with Railway domains
- Static files are served using whitenoise

## Troubleshooting

- Check the logs in Railway for any deployment errors
- If you encounter database migration issues, you can run migrations manually:
  ```
  railway run python django_neurology_mcq/manage.py migrate
  ```
- For static file issues:
  ```
  railway run python django_neurology_mcq/manage.py collectstatic --noinput
  ```