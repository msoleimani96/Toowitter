# Toowitter
This is a twitter like social media backend.


## How to start the project?

1. Clone or download the project.

   
2. Create a virtual environment.
   ```
   python -m venv venv
   ```

3. Activate the environment.
   ```
   source venv/bin/activate
   ```
   
4. Install packages.
   ```
   pip install -r requirements.txt
   ```

5. Config MySQL settings in settings.py file.

6. Migrate models.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Run server.

   ```
   python manage.py runserver
   ```
