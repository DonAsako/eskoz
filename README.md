# Eskoz

**Eskoz** is a Django-based project designed to help you quickly and easily create a multilingual blog, with a straightforward deployment process.

## Requirements

Make sure you have the following installed on your system:
- Docker
- Docker Compose

## Installation

### 1. Clone the repository:
```sh
git clone git@github.com:DonAsako/eskoz.git
cd eskoz
```

### 2. Copy the example environment variables file:
```sh
cp .env.example .env
```

### 3. Edit the .env file to configure your environment variables.
The .env file stores your environment-specific settings. Here's what each variable does:
```yaml
# --- Django Settings ---
DEBUG=0                         # Enable (1) or disable (0) Django debug mode
DJANGO_SECRET_KEY=              # Secret key for Django security
DJANGO_ALLOWED_HOSTS=           # Space-separated list of allowed hostnames
ADMIN_URL=                      # Custom URL path for the Django admin (e.g., "admin")

# --- PostgreSQL Settings ---
POSTGRES_DB=                    # Name of the PostgreSQL database
POSTGRES_USER=                  # PostgreSQL username
POSTGRES_PASSWORD=              # PostgreSQL password

# --- NGINX / Domain Configuration ---
DOMAIN=                         # Your domain name (e.g., example.com)
EMAIL=                          # Email address used for SSL certificate
```
### 4. Build and start the Docker containers in detached mode:
```sh
docker compose up --build -d
```

### 5. Creating the first admin user
To create the first Django superuser, run :
```sh
docker compose exec web python manage.py createsuperuser
```

## To-do 
### Logs
- [ ] Add Django logging configuration
- [ ] Set up log rotation (e.g. RotatingFileHandler)
- [ ] Mount Docker volume for log files
- [ ] Define log levels (INFO, WARNING, ERROR, etc.)
- [ ] Redirect container logs to files
- [ ] Add .env variable for log level
### Admin
- [x] Add a color palette to choose a color in the theme section.
### Translate
- [ ] Make translation
### Style
- [ ] Make the layout responsive
- [ ] Improve article detail view
- [ ] Add article parameters to the article list page
### Deploy
- [ ] Add automatic script to load SSL/Certificates and easy deploy..
### Features 
- [ ] New Theme Manager
    - [ ] Options to load Theme
    - [ ] Theme structure


## Key Features
- Ready-to-use multilingual blog
- Easy deployment with Docker
- Built-in Django admin interface

## License
This project is licensed under the GNU General Public License v3.0.
See the [LICENSE](LICENSE) file for more details.
