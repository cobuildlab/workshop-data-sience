#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import GoogleCredentials

from data_functions import get_sessions
from users_functions import get_first_profile_id
from util import print_results


def main(argv):
    credentials = GoogleCredentials.get_application_default()
    service = build('analytics', 'v3', credentials=credentials)

    # Try to make a request to the API. Print the results or handle errors.
    try:
        first_profile_id = get_first_profile_id(service)
        if not first_profile_id:
            print('Could not find a valid profile for this user.')
        else:
            print(first_profile_id)
            results = get_sessions(service, first_profile_id)
            print_results(results)

    except TypeError as error:
        # Handle errors in constructing a query.
        print(('There was an error in constructing your query : %s' % error))

    except HttpError as error:
        # Handle API errors.
        print(('Arg, there was an API error : %s : %s' %
               (error.resp.status, error._get_reason())))

    except AccessTokenRefreshError:
        # Handle Auth errors.
        print('The credentials have been revoked or expired, please re-run '
              'the application to re-authorize')


if __name__ == '__main__':
    main(sys.argv)
