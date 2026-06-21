# %%

# must have the .sqlite file in the exact same folder or list your entire path to the file.

sqlite_file = 'lahmansbaseballdb.sqlite'

con = sqlite3.connect(sqlite_file)

q = '''
SELECT * FROM batting LIMIT 2
'''
qr = pd.read_sql_query(q,con)