
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#import os
#from pathlib import Path
#import environ

#BASE_DIR = Path(__file__).resolve().parent.parent.parent
#env = environ.Env()
#environ.Env.read_env()

#STATICFILES_STORAGE='storages.backends.s3boto3.S3Boto3Storage'


#AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
#AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
# A path prefix that will be prepended to all uploads
#AWS_LOCATION = 'static'
#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'



# Django Static Files Directory
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)