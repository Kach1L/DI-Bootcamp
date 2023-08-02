import psycopg2

# CONNECT TO THE DATABASE
connection = psycopg2.connect(
    database="dvdrental", #your database name
    user='postgres',
    password='Kachikwulu1',
    host='localhost', #or IP address
    port='5432'
)

def retrieve_actors () :
    print("retrieving an actor...")
    try :
        with connection:
            with connection.cursor() as curs: #open and close the cursor
                query = "SELECT * FROM actor"
                curs.execute(query)
                data = curs.fetchall()
                print(data)
    except Exception as err :
        print(err)

# retrieve_actors()         


def retrieve_actors_numberoscars () :
    try :
        with connection:
            with connection.cursor() as curs: #open and close the cursor
                query = "SELECT number_oscars FROM actor"
                curs.execute(query)
                data = curs.fetchall() #get a list of tuples
                print(data) #or do a loop
    except Exception as err :
        print(err)

# retrieve_actors_numberoscars() 

def retrieve_actors_cars (last_name) :
    try :
        with connection:
            with connection.cursor() as curs: #open and close the cursor
                query = f"""
                SELECT first_name, brand, color
                FROM actor
                INNER JOIN car ON actor.id = car.owner_id
                WHERE last_name = '{last_name}'
                """
                curs.execute(query)
                data = curs.fetchone() #get only 1 tuple
                print(data) #('George', 'Mazda', 'white')
                
                # for info in data :
                #     print(info)

                print(f"{data[0]} has a {data[2]} {data[1]}")

    except Exception as err :
        print("IN THE EXCEPT", err)

# retrieve_actors_cars("Clooney")
# retrieve_actors_cars("Damon") 

# *args --> tuple
def insert_actor (*info) :
    print("adding an actor...")
    # info will look like this ("Johnny", "Depp", 1)
    try :
        with connection:
            with connection.cursor() as curs: #open and close the cursor
                query = f"""
                INSERT INTO actor (first_name, last_name, number_oscars)
                VALUES {info}
                """
                curs.execute(query)
                connection.commit() #actually commit the data

    except Exception as err :
        print("IN THE EXCEPT", err)

insert_actor("Johnny", "Depp", 1)
retrieve_actors()

connection.close() #close the connection