# Toowitter
This is a twitter like social media backend.

## How to start the project?

1. Create a virtual environment.
   ```
   python -m venv venv
   ```

2. Activate the environment.
   ```
   source venv/bin/activate
   ```
   
3. Install packages.
   ```
   pip install -r requirements.txt
   ```

4. Config MySQL settings in settings.py file.

5. Migrate models.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run server.

   ```
   python manage.py runserver
   ```
