def print_results(results):
    """Prints out the results.
    This prints out the profile name, the column headers, and all the rows of
    data.
    Args:
      results: The response returned from the Core Reporting API.
    """

    print()

    # Print header.
    output = []
    for header in results.get('columnHeaders'):
        output.append('%35s' % header.get('name'))
    print(''.join(output))

    # Print data table.
    if results.get('rows', []):
        for row in results.get('rows'):
            output = []
            for cell in row:
                output.append('%35s' % cell)
            print(''.join(output))

    else:
        print('No Rows Found')