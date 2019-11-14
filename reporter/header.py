from datetime import date
import warnings


def create_header2(authors, ville = "Paris"):
    """Returns the header strings with authors listed
    
    Parameters
    ----------
    authors : list of dict
        Each element of authors should have the 'first' and 'last' keys
        
    Returns
    -------
    header : str
        The header string at today's date
    
    
    """
    ajd = date.today()
    header_strings = [f"A {ville}, le {ajd.strftime('%A %d %B %Y')}\n",
                      "### auteurs:\n",
                     ]
    for aut in authors :
        _validate(aut, keys=('first','last'))
        
        first = aut.get("first","")
        if not first :
            warnings.warn('first key not found')
            
        try :
            last = aut['last']
        except KeyError:
            warnings.warn('last key not found')
            last = ""

        header_strings.append(f"- {first} {last}")

    Header = "\n".join(header_strings)
    return Header

def _validate(aut, keys=('first', 'last')):
    missing = {"first", "last"}.difference(aut)
    if missing:
        warnings.warn(f'missing key(s) {list(missing)} from dict')
        return False
    return True

def header_json(listfold):
    """Returns the header strings with authors listed in a text folder
    
    Parameters
    ----------
    listfold : a text folder
        The fold must present a list. Each element in listfold should have the 'first' and 'last' keys
        
    Returns
    -------
    header2 : str
        The header string at today's date
    
    
    """    
    
    with open (listfold, 'r') as file_handle:
        authors3 = json.load(file_handle)
            
    header2 = create_header2(authors3)
        
    return header2