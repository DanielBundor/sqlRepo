
bookCursor = bookDatabaseConnection.cursor()
bookQuery = ('SELECT Title, Category'
             'FROM Book '
             'WHERE Price > 20.00')
bookCursor.execute(bookQuery)

for resultRow in bookCursor.fetchall():
   print('Title:', resultRow[0])
   print('Category:', resultRow[1])