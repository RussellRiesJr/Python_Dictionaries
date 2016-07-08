
stockDict = { 'GM': 'General Motors', 'CAT': 'Caterpillar', 'DC': 'Detective Comics', 'BS': 'Fox News'}

purchases = [ ( 'GM', 150, '11-sep-2001', 60 ), ( 'CAT', 225, '5-aug-1983', 2000 ), ( 'BS', 10, '17-jul-1994', 100 ), ( 'DC', 30, '31-jan-1987', 300), ( 'GM', 200, '15-dec-2008', 75), ( 'DC', 45, '23-dec-1987', 230 ), ( 'BS', 25, '27-feb-1997', 150), ( 'CAT', 260, '6-jun-1988', 100) ]

def purchase_history():
  '''Convert stock info into a human readable string

  No keywords

  Prints: string
  '''
  for trans in purchases:
    print('purchased %s shares of %s worth $%s' % ( trans[1], stockDict[trans[0]], trans[1]*trans[3] ))

def purchase_summary():
  '''
  '''
  # purchase_total = []
  # for trans in purchases:
  #   company_initials = trans[0]
  #   share_amount = 0
  #   date = trans[2]
  #   price = trans[3]

  #   total = share_amount * price
  #   company_name = stockDict[company_initials]
  #   if
  #     share_amount += trans[1]
    # summary = dict(zip(stockDict[trans[0]], trans[3]))
    # print(summary)
  summary = dict()
  for (company, name) in stockDict.items():
    summary[company] = list()
    for trans in purchases:
      if company == trans[0]:
        summary[company].append(trans)
  for (company, sale) in summary.items():
    shares = 0
    for s in sale:
      shares += s[3]
    print('sold {0} shares of {1} stock'.format(str(shares), company))

import code
code.interact(local=locals())
