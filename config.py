formats = ['H2H', 'CATs']
positions = ['PG', 'SG', 'SF', 'PF', 'C', 'G', 'F']
default_pos = ['PG', 'SG', 'SF', 'PF', 'C']
categories = ['PTS', 'BLK', 'AST', 'STL', 'FT%', 'FG%', '3P', 'TOV',
              'TRB', 'ORB', 'DRB', 'PF', 'G', 'GS', 'MP', 'FG', 'FGA',
              '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', '3PA', '3P%', 'PF']
default_fantasy = ['PTS', 'BLK', 'AST', 'STL', 'FT',
                   'FTA', 'FG', 'FGA', '3P', 'TOV', 'TRB']

def update(dict, values, decimals="2"):
  for i in range(len(values)):
    dict[values[i]] = '{:.' + decimals + 'f}'

categories_style_dict = {categories[i]: '{:.1f}' for i in range(len(categories))}
update(categories_style_dict, ['FG%', 'FT%', '2P%', 'eFG%', '3P%'])
update(categories_style_dict, ['G', 'GS'], "0")


