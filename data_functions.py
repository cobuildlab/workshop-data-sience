#!/usr/bin/python

# -*- coding: utf-8 -*-

def get_top_keywords(service, profile_id):
    """Executes and returns data from the Core Reporting API.
    This queries the API for the top 25 organic search terms by visits.
    Args:
      service: The service object built by the Google API Python client library.
      profile_id: String The profile ID from which to retrieve analytics data.
    Returns:
      The response returned from the Core Reporting API.
    """

    return service.data().ga().get(
        ids='ga:' + profile_id,
        start_date='2017-01-01',
        end_date='2017-12-31',
        metrics='ga:visits',
        dimensions='ga:source,ga:keyword',
        sort='-ga:visits',
        filters='ga:medium==organic',
        start_index='1',
        max_results='500').execute()


def get_sessions(service, profile_id):

    return service.data().ga().get(
        ids='ga:' + profile_id,
        start_date='2017-01-01',
        end_date='2017-12-31',
        metrics='ga:newUsers,ga:avgSessionDuration',
        # filters='ga:adDestinationUrl!=(not set)',
        # filters='ga:adFormat!=(not set);ga:city!=(not set)',
        # dimensions='ga:city,ga:browser,ga:source,ga:medium,ga:adFormat,ga:operatingSystem,ga:deviceCategory',
        # dimensions='ga:city,ga:browser,ga:source,ga:medium,ga:adDisplayUrl,ga:adDestinationUrl',
        dimensions='ga:month',
        start_index='1',
        max_results='50').execute()