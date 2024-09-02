import psycopg2
from psycopg2.extras import execute_values
from config.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

class Database:
    def __init__(self):
        self.conn = self.get_connection()

    def get_connection(self):
        return psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

    def create_tables(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS coin_rankings (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() AT TIME ZONE 'UTC'),
                    coin_id INTEGER NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    symbol VARCHAR(20) NOT NULL,
                    rank INTEGER NOT NULL,
                    price NUMERIC(18, 8) NOT NULL,
                    market_cap NUMERIC(18, 2) NOT NULL,
                    volume_24h NUMERIC(18, 2) NOT NULL
                );
                
                CREATE INDEX IF NOT EXISTS idx_coin_rankings_timestamp ON coin_rankings (timestamp);
                CREATE INDEX IF NOT EXISTS idx_coin_rankings_coin_id ON coin_rankings (coin_id);
            """)
        self.conn.commit()

    def insert_coin_data(self, coin_data):
        with self.conn.cursor() as cur:
            values = [
                (
                    coin.coin_id,
                    coin.name,
                    coin.symbol,
                    coin.rank,
                    coin.price,
                    coin.market_cap,
                    coin.volume_24h
                )
                for coin in coin_data
            ]
            execute_values(cur, """
                INSERT INTO coin_rankings (coin_id, name, symbol, rank, price, market_cap, volume_24h)
                VALUES %s
            """, values)
        self.conn.commit()

    def get_ranking_trends(self, coin_symbol, days=7):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT timestamp, rank
                FROM coin_rankings
                WHERE symbol = %s
                AND timestamp >= NOW() - INTERVAL %s DAY
                ORDER BY timestamp
            """, (coin_symbol, days))
            return cur.fetchall()

    def close(self):
        self.conn.close()