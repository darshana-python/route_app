import mysql.connector

def create_connection():
    """Establish a new MySQL connection."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
           # port=3306,
            user='root',
            password='Darshanasiddhesh@28',
           # database='road_db',
            connection_timeout=10  # Set a timeout for the connection attempt
        )
        if conn.is_connected():
            print("Connected to MySQL server.")
            return conn
    except mysql.connector.Error as err:
        print("Failed to connect to MySQL server.")
        return None

def manage_road_data():
    """Manage road data in the database with enhanced error handling."""
    conn = None
    try:
        conn = create_connection()
        if conn is None:
            return  # Exit if connection failed

        cursor = conn.cursor()

        cursor.execute("TRUNCATE TABLE Users1")
        conn.commit()
        print("Table 'Users1' truncated.")

        # Insert initial data
        data = [
            {"name": "Andheri Highway (NH8)", "speedlimit": 90, "coord": (72.841, 19.145)},
            {"name": "Marol Highway (NH8)", "speedlimit": 80, "coord": (72.850, 19.160)},
            {"name": "NH10", "speedlimit": 110, "coord": (72.880, 19.190)},
            {"name": "Mumbai–Pune Expressway", "speedlimit": 120, "coord": (73.400, 18.500)},
            {"name": "NH3 (Agra–Mumbai Road)", "speedlimit": 100, "coord": (73.050, 19.000)},
            {"name": "NH4 (Mumbai–Chennai Road)", "speedlimit": 100, "coord": (73.200, 19.200)},
            {"name": "NH6 (Kolkata–Mumbai Road)", "speedlimit": 90, "coord": (73.500, 19.300)},
            {"name": "NH7 (Varanasi–Kolkata Road)", "speedlimit": 90, "coord": (73.600, 19.400)},
            {"name": "NH8D (Mumbai–Ahmedabad Road)", "speedlimit": 100, "coord": (73.700, 19.500)},
            {"name": "NH66 (Mumbai–Goa Road)", "speedlimit": 80, "coord": (73.800, 19.600)}
        ]

        for item in data:
            lon, lat = item["coord"]
            cursor.execute("""
                INSERT INTO Users1 (name, speedlimit, longitude, latitude)
                VALUES (%s, %s, %s, %s)
            """, (item["name"], item["speedlimit"], lon, lat))

        conn.commit()
        print("Initial data inserted.")

        # # Update Example: Change speedlimit for 'NH10'
        # cursor.execute("""
        #     UPDATE Users1
        #     SET speedlimit = %s
        #     WHERE name = %s
        # """, (100, "NH10"))
        # conn.commit()
        # print("Updated 'NH10' speedlimit to 100.")

        # # Delete Example: Delete by ID (e.g., delete ID = 2)
        # cursor.execute("DELETE FROM Users1 WHERE id = %s", (2,))
        # conn.commit()
        # print("Deleted record with ID = 2.")

        # Fetch All Records
        # cursor.execute("SELECT * FROM Users1")
        # all_rows = cursor.fetchall()
        # print("All Records:")
        # for row in all_rows:
        #     print(row)

        # Fetch One Record by ID (e.g., ID = 1)
        # cursor.execute("SELECT * FROM Users1 WHERE id = %s", (1,))
        # one_row = cursor.fetchone()
        # print("Record with ID = 1:")
        # print(one_row)
    
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("Connection closed.")