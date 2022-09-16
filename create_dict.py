import yaml


NOT_AVAILABLE = ['Not Available']


def add_to_dict(git_contributors, git_title, git_family_name, git_given_name, git_url,family_names, given_names, title, year, url, doi, publisher, journal):

    dict_file = {'cff-version': '1.2.0',
                 'message': 'If you use this plugin, please cite it using these metadata',
                 }

   
    git_title_dict_file = {'title': git_title}
    for key, value in git_title_dict_file.items():
        if key in dict_file:
            dict_file[key].extend(value)
        else:
            dict_file[key] = value

    if(git_contributors) and (len(git_contributors)>1):
        for i in range(len(git_contributors)):
            author_dict_file = {'authors': [
                {'given-names': git_contributors[i]}], }

            for key, value in author_dict_file.items():
                if key in dict_file:
                    dict_file[key].extend(value)
                else:
                    dict_file[key] = value
    else:
        git_author_dict_file = {'authors': [
                    {'family-names': git_family_name, 'given-names': git_given_name}], }

        for key, value in git_author_dict_file.items():
                    if key in dict_file:
                        dict_file[key].extend(value)
                    else:
                        dict_file[key] = value

    git_url_dict_file = {'url':git_url  }

    for key, value in git_url_dict_file.items():
                if key in dict_file:
                    dict_file[key].extend(value)
                else:
                    dict_file[key] = value

     ######
    if (bool(year) and year != NOT_AVAILABLE):

        year_dict_file = {'date-released': year + '-01-01'}
    elif (bool(year) == False):
        year_dict_file = {'date-released': NOT_AVAILABLE}

    for key, value in year_dict_file.items():
        if key in dict_file:
            dict_file[key].extend(value)
        else:
            dict_file[key] = value
   
   

    ######
    # if (bool(family_names) and family_names != NOT_AVAILABLE):
    #     for i in range(len(family_names)):
    #         author_dict_file = {'authors': [
    #             {'family-names': family_names[i], 'given-names': given_names[i]}], }

    #         for key, value in author_dict_file.items():
    #             if key in dict_file:
    #                 dict_file[key].extend(value)
    #             else:
    #                 dict_file[key] = value

    # elif (bool(family_names) == False):
    #     author_dict_file = {'authors': [
    #         {'family-names': 'Not Available', 'given-names': 'Not Available'}], }

    #     for key, value in author_dict_file.items():
    #         if key in dict_file:
    #             dict_file[key].extend(value)
    #         else:
    #             dict_file[key] = value

   

    ######
    
    if (bool(publisher) and publisher != NOT_AVAILABLE):

            if (bool(doi)):
                if (bool(title)):
                    if(bool(url)):
                        url = ''.join(map(str, url))
                        publisher_dict_file = {'references': [
                        {'type': 'book', 'title': title, 'publisher': publisher, 'doi': doi, 'url':url}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                    else:
                        publisher_dict_file = {'references': [
                        {'type': 'book', 'title': title, 'publisher': publisher, 'doi': doi, 'url':'Not Available'}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    
                else:

                    if(bool(url)):
                        url = ''.join(map(str, url))
                        publisher_dict_file = {'references': [
                            {'type': 'book', 'title': 'Not Available', 'publisher': publisher, 'doi': doi, 'url':url}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                    else:
                        publisher_dict_file = {'references': [
                            {'type': 'book', 'title': 'Not Available', 'publisher': publisher, 'doi': doi, 'url':'Not Available'}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                
            else:
                if (bool(title)):
                    if(bool(url)):
                        publisher_dict_file = {'references': [
                            {'type': 'book',
                                'title': title,
                            'publisher': publisher, 'doi': 'Not Available', 'url':url}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    else:
                        publisher_dict_file = {'references': [
                            {'type': 'book',
                                'title': title,
                            'publisher': publisher, 'doi': 'Not Available', 'url':'Not Available'}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    
                else:
                    if(bool(url)):
                        publisher_dict_file = {'references': [
                            {'type': 'book',
                                'title': 'Not Available',
                            'publisher': publisher, 'doi': 'Not Available', 'url': url}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    else:
                        publisher_dict_file = {'references': [
                            {'type': 'book',
                                'title': 'Not Available',
                            'publisher': publisher, 'doi': 'Not Available', 'url': 'Not Available'}]}

                        for key, value in publisher_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

    ######
    if (bool(journal) and journal != NOT_AVAILABLE):

            journal = ''.join(map(str, journal))

            if (bool(doi)):
                if (bool(title)):
                    if(bool(url)):
                        url = ''.join(map(str, url))
                        journal_dict_file = {'references': [
                        {'type': 'article', 'title': title, 'journal': journal, 'doi': doi, 'url':url}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                    else:
                        journal_dict_file = {'references': [
                        {'type': 'article', 'title': title, 'journal': journal, 'doi': doi, 'url':'Not Available'}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    
                else:

                    if(bool(url)):
                        url = ''.join(map(str, url))
                        journal_dict_file = {'references': [
                            {'type': 'article', 'title': 'Not Available', 'journal': journal, 'doi': doi, 'url':url}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                    else:
                        journal_dict_file = {'references': [
                            {'type': 'article', 'title': 'Not Available', 'journal': journal, 'doi': doi, 'url':'Not Available'}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

                
            else:
                if (bool(title)):
                    if(bool(url)):
                        journal_dict_file = {'references': [
                            {'type': 'article',
                                'title': title,
                            'journal': journal, 'doi': 'Not Available', 'url':url}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    else:
                        journal_dict_file = {'references': [
                            {'type': 'article',
                                'title': title,
                            'journal': journal, 'doi': 'Not Available', 'url':'Not Available'}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    
                else:
                    if(bool(url)):
                        journal_dict_file = {'references': [
                            {'type': 'article',
                                'title': 'Not Available',
                            'journal': journal, 'doi': 'Not Available', 'url': url}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value
                    else:
                        journal_dict_file = {'references': [
                            {'type': 'article',
                                'title': 'Not Available',
                            'journal': journal, 'doi': 'Not Available', 'url': 'Not Available'}]}

                        for key, value in journal_dict_file.items():
                            if key in dict_file:
                                dict_file[key].extend(value)
                            else:
                                dict_file[key] = value

    ######
    
    if(bool(journal)== False and bool(publisher)== False and bool(doi)== True and bool(url)== True and bool(title)==True ):
        doi = ''.join(map(str, doi))
        url = ''.join(map(str, url))
        doi_dict_file = {'references': [
                    {'type': 'article',
                    'title': title,
                     'doi': doi,
                     'url':url}]}

        for key, value in doi_dict_file.items():
                    if key in dict_file:
                        dict_file[key].extend(value)
                    else:
                        dict_file[key] = value
    
    if(bool(journal)== False and bool(publisher)== False and bool(doi)== True and bool(url)== False and bool(title)==True):
        doi = ''.join(map(str, doi))
        url = ''.join(map(str, url))
        doi_dict_file = {'references': [
                    {'type': 'article',
                    'title': title,
                     'doi': doi,
                     'url':'Not Available'}]}

        for key, value in doi_dict_file.items():
                    if key in dict_file:
                        dict_file[key].extend(value)
                    else:
                        dict_file[key] = value

    if(bool(journal)== False and bool(publisher)== False and bool(doi)== True and bool(url)== False and bool(title)==False):
        doi = ''.join(map(str, doi))
        url = ''.join(map(str, url))
        doi_dict_file = {'references': [
                    {'type': 'article',
                    'title': 'Not Available',
                     'doi': doi,
                     'url':'Not Available'}]}

        for key, value in doi_dict_file.items():
                    if key in dict_file:
                        dict_file[key].extend(value)
                    else:
                        dict_file[key] = value



    print('\n')
    print('Citation Dict File created')

    return dict_file
