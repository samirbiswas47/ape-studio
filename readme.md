# To create python environment
python -m venv venv

# To activte python environment
source venv/Scripts/activate # Windows bash
venv\Scripts\activate # Windows

# To install python dependency library
pip install -r ./requirements.txt

# To database migrate
python ./manage.py makemigrations
python ./manage.py migrate

# To create super admin
python manage.py createsuperuser

# Example: 
Username: superuser
Email address: super@gmail.com
Password: as user defined

# To start application
python manage.py runserver
or change port
python manage.py runserver 127.0.0.1:9000

# environment setup
APP_TYPE=development|production
DEBUG=True|False
SECRET_KEY=your-app-secret-key
EMAIL_HOST=smtp.hostinger.com
EMAIL_PORT=587
EMAIL_HOST_USER=user email
EMAIL_HOST_PASSWORD= userpassword
EMAIL_USE_TLS=True
DATABASE_URL=

# Note: We used to database based on "APP_TYPE" one is sqlite3 for development and another postgres for production

# Following url for the application
Admin Backend: https://ape-studio.onrender.com/admin (Note: to login admin panel user must have Staff role)
System User Api Endpoint: https://ape-studio.onrender.com (Note: User only can perform CRUD operation once they login throuh admin or admin panel)
Developer Api endpoint: https://ape-studio.onrender.com/api/schema/swagger-ui/
Developer API Docs: https://ape-studio.onrender.com/api/schema/redoc

# Module:
1. Group: Admin can create  group for permission
2. Users: All user action
3. Email templates: Pre defined email template for email
4. Enquirys: Store enquiries (Name, Email, Phone, Service Interest, Message) in a database.
5. Services: Services list
6. Portfolio: 
7. Newsletter Subscribers:
8. Testimonials:


# GitHub Repository 
https://github.com/samirbiswas47/ape-studio

# We made softdelete for All modlue user delete action (Finally admin can delete based on delete permission through admin panel)

# Technology Recomendation:
I built the backend using Django and Django REST Framework because they provide a scalable and secure architecture for rapid backend development. The project follows a modular structure with separate apps for APIs, admin management, and email services. SQLite3 was used for local development due to its simplicity and quick setup, while PostgreSQL was configured for production to ensure better scalability and reliability. Database switching is handled dynamically using the APP_TYPE environment variable. Session-based authentication was implemented for secure admin access, and protected API routes were added for authenticated users. Automated email acknowledgments are sent asynchronously to improve performance and user experience. The backend is deployed on Render with environment-based configuration management for security and maintainability.

Admin Backend: Admin Panel (Session base authentication)
System User API Endpoint: API Base URL (Session base authentication)
Developer Swagger Docs: Swagger UI (JWT token base authentication)
Developer ReDoc: ReDoc Documentation
