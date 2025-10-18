import mysql.connector
from mysql.connector import Error

def create_tables():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user="root",
            password="is35this67newlife",
            database='alx_book_store',
        )

        if connection.is_connected():
            cursor = connection.cursor()
            print("Connected to the database 'alx_book_store' successfully!")

            tables = {
                "Authors": """
                    CREATE TABLE IF NOT EXISTS Authors (
                        author_id INT PRIMARY KEY,
                        author_name VARCHAR(215) NOT NULL
                    );
                """,
                "Books": """
                    CREATE TABLE IF NOT EXISTS Books (
                        book_id INT PRIMARY KEY,
                        title VARCHAR(130) NOT NULL,
                        author_id INT,
                        published_date DATE,
                        price DOUBLE,
                        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
                    );
                """,
                "Customers": """
                    CREATE TABLE IF NOT EXISTS Customers (
                        customer_id INT PRIMARY KEY,
                        customer_name VARCHAR(215) NOT NULL,
                        email VARCHAR(215) UNIQUE NOT NULL,
                        address TEXT NOT NULL
                    );
                """,
                "Orders": """
                    CREATE TABLE IF NOT EXISTS Orders (
                        order_id INT PRIMARY KEY,
                        customer_id INT,
                        order_date DATE,
                        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                    );
                """,
                "Order_Details": """
                    CREATE TABLE IF NOT EXISTS Order_Details (
                        orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
                        order_id INT,
                        book_id INT,
                        quantity DOUBLE,
                        FOREIGN KEY (order_id) REFERENCES Orders(order_id), 
                        FOREIGN KEY (book_id) REFERENCES Books(book_id)
                    );
                """,
            }

            for table_name, query in tables.items():
                cursor.execute(query)
                print(f"Table '{table_name}' created successfully.")
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
if __name__ == "__main__":
    create_tables()