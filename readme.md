
```markdown
# Student Management System (Django)

This is a simple Django-based Student Management System that allows users to manage students’ records. The project uses **Supabase** as the database and is deployed on **Render**. This guide provides instructions for setting up, running, and deploying the project.

---

## Features

- **Add, Edit, Delete Students**: Manage student records with basic CRUD operations.
- **Admin Interface**: Django admin for managing data through a user-friendly interface.
- **PostgreSQL Database**: Using Supabase (PostgreSQL) as the database backend.
- **Responsive UI**: Beautifully styled with Django templates and Bootstrap.
- **Deployed on Render**: Free and easy deployment on Render platform.

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.10+**
- **Django 5.1.1**
- **Supabase account** (for database)
- **Render account** (for deployment)

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/K-Ananthamoorthy/student_management-FSD.git
cd student-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root of the project and add the following:

```plaintext
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=sms-fsd.onrender.com,localhost,127.0.0.1
DATABASE_URL=postgres://your-supabase-db-url
```

Replace:

- `your-django-secret-key` with your own secret key.
- `your-supabase-db-url` with your Supabase PostgreSQL connection URL.

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the admin credentials.

### 7. Collect Static Files

```bash
python manage.py collectstatic
```

### 8. Run the Server Locally

```bash
python manage.py runserver
```

Your project should now be running locally at `http://127.0.0.1:8000/`.

---

## Supabase Setup

1. **Create a Supabase Project**:
   - Go to [Supabase](https://supabase.com/), sign in, and create a new project.
   - In the **Settings** > **Database** section, get the connection details (URL, user, password).

2. **Set Database Configuration**:
   - Use the `DATABASE_URL` in your `.env` file to connect to Supabase.

---

## Deployment on Render

### 1. Connect Your Repository

- Go to [Render](https://render.com/), create a new web service, and connect your GitHub or GitLab repository.
- Select your branch and deploy.

### 2. Environment Variables on Render

- In your Render project settings, add the same environment variables from your `.env` file into Render’s **Environment** section.

### 3. Update Start Command

Make sure your **Start Command** in Render is set up to run migrations and collect static files:

```bash
python manage.py collectstatic --noinput && python manage.py migrate && gunicorn student_management.wsgi:application
```

---

## Admin Panel Access

Once deployed, you can access the Django admin panel at:

```
https://yourhost.com/admin
```

Log in using the superuser credentials you created.

---

## Troubleshooting

### 1. **Static Files (CSS not Loading)**

If the CSS for the admin panel isn’t loading, ensure that static files are properly configured. Make sure you have run `collectstatic` and added `whitenoise` to your middleware in `settings.py`.

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### 2. **Database Connection Issues**

If the app isn’t connecting to Supabase, check that:

- The `DATABASE_URL` is correctly set in Render’s environment variables.
- You have allowed access from Render's IP addresses in Supabase.

### 3. **Creating a Superuser in Deployment**

If you cannot access a shell in Render to create a superuser, follow these steps:

1. **Option 1: Add a Custom Management Command**:
   - Create a custom management command to create a superuser and run it on deploy.
   
2. **Option 2: Create Superuser via Temporary Route**:
   - Add a temporary view that creates a superuser when accessed.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

```


