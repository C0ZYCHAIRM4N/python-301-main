# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not

# the database connection can be established.
import sqlalchemy

try:
    # attempt to connect to database  
    engine = sqlalchemy.create_engine('mysql+pymysql://username:password@localhost/mydatabase')
    print("you are now connected to database")
    connection = engine.connect()
except:
    print("connection unsuccesful")
else:
    print("Connection established, and can now perform database operations.")




