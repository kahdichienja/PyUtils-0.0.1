class Utils():
    n = 0
    
    def __init__(self, *args, **kwargs):
        super(Utils, self).__init__(*args, **kwargs)
    '''
    removing dollar sign and white space 
    '''
    def remove_dollar_white_space(n):
        n_as_str=str(n).strip()
        amount= []
        for c in n_as_str:
            if (c.isdigit()) or c == '.':
                amount.append(c)
        res = ("".join(map(str, amount)))
        return float(res)
    '''
    removing commas and white space 
    '''
    def remove_comma_and_spaces(n):
        for spaceanddollar in n:
          test = float(n.replace(',', '').replace(' ', '').replace('', ''))
        
        return test
    """
    Remove Punctuations From a String
    """

    def remove_punctuation(s):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        import string
        no_punct = s.translate(str.maketrans('', '', string.punctuation))
        return no_punct

    def __str__(self):
        return super().__str__()
    
    

