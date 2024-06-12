from .base import *

# Database
# [START db_setup]
# [START gaestd_py_django_database_config]
# Use django-environ to parse the connection string
DATABASES = {"default": env.db()}

# If the flag has been set, configure to use proxy
if os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None):
    DATABASES["default"]["HOST"] = "127.0.0.1"
    DATABASES["default"]["PORT"] = 5432

# [END gaestd_py_django_database_config]
# [END db_setup]

ALLOWED_HOSTS = ['crassula.io', 'www.crassula.io']
CSRF_TRUSTED_ORIGINS = ['https://crassula.io']
SECURE_SSL_REDIRECT = True

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'crassula'
GS_DEFAULT_ACL = 'publicRead'
MEDIA_URL = 'https://storage.googleapis.com/crassula/'
SITE_ID = 1
