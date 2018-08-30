#positional formating

print ('to {}. Lorem ipsum dolor sit amet, consectetur adipisicing elit{}, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo {}consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse {} cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format('fjsekf','fjsekf2','fjsekf3','fjsekf4'))




#Named placeholders
person = {'first':'fsekf','second':'fjsekf1','third':'fjsekf3'}
print ('{p[first]} Lorem ipsum dolor sit amet,{p[second]} consectetur adipisicing elit,{p[third]} sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format(p=person))
