my_family = {
  'sister': {
    'name': 'Krista',
    'age': 42
  },
  'mother': {
    'name': 'Cathie',
    'age': 70
  },
  'brother': {
    'name': 'Bruce Jr.',
    'age': 37
  },
  'father': {
    'name': 'Bruce Sr.',
    'age': 74
  }
}

{print('{0} is my {1} and is {2}-years-old'.format(v['name'], k, v['age'])) for k, v in my_family.items()}

















import code
code.interact(local=locals())
