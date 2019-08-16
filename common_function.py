from database.models.contribution_musical_work import ContributionMusicalWork


def parseSource(item_name, item_type):
    try:
        if (item_type.__name__ == 'Section' or
                item_type.__name__ == 'Source'):

            return item_type.objects.get_or_create(title=item_name,
                                                   url='https://docs.google.com/spreadsheets/d/1G1CPeHKjLAIXZPJSuwIOOIoq9BiPm7H97ikBEZ9ayNE/edit#gid=588272074')

        elif (item_type.__name__ == 'GenreAsInStyle' or
              item_type.__name__ == 'Instrument' or
              item_type.__name__ == 'GenreAsInType'):

            return item_type.objects.get_or_create(name=item_name)

    except item_type.DoesNotExist:
        print('Does not exist: ' + item_name)
        return None


def createContribution(p, work):
    """

    :return:
    """
    contribute = ContributionMusicalWork.objects.get_or_create(
        person=p,
        certainty_of_attribution=True,  # We assume these pieces are all secure
        role='COMPOSER',
        contributed_to_work=work
    )[0]
    return contribute

