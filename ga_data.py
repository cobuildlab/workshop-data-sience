from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
from googleapiclient.discovery import build
service = build('analytics', 'v3',credentials=credentials)

