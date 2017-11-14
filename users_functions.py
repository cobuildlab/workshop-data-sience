def get_first_profile_id(service):
    """Traverses Management API to return the first profile id.
    This first queries the Accounts collection to get the first account ID.
    This ID is used to query the Webproperties collection to retrieve the first
    webproperty ID. And both account and webproperty IDs are used to query the
    Profile collection to get the first profile id.
    Args:
      service: The service object built by the Google API Python client library.
    Returns:
      A string with the first profile ID. None if a user does not have any
      accounts, webproperties, or profiles.
    """

    accounts = service.management().accounts().list().execute()

    if accounts.get('items'):
        firstAccountId = accounts.get('items')[0].get('id')
        webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()

        if webproperties.get('items'):
            firstWebpropertyId = webproperties.get('items')[0].get('id')
            profiles = service.management().profiles().list(accountId=firstAccountId,
                                                            webPropertyId=firstWebpropertyId).execute()

            if profiles.get('items'):
                ent = profiles.get('items')[0]
                print("%s" % ent.get('websiteUrl'))
                print("%s" % ent.get('name'))
                return ent.get('id')

    return None