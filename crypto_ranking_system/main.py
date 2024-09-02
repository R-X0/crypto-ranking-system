import time
from config.settings import UPDATE_INTERVAL
from services.data_fetcher import DataFetcher
from services.data_processor import DataProcessor
from services.chart_generator import ChartGenerator
from utils.logger import logger



def main():
    data_processor = DataProcessor()
    
    try:
        while True:
            logger.info("Fetching latest cryptocurrency data...")
            coin_data = DataFetcher.fetch_latest_coin_data()
            
            logger.info("Processing and storing data...")
            data_processor.process_and_store_data(coin_data)
            
            logger.info("Generating sample chart for BTC...")
            btc_data = data_processor.get_coin_ranking_trends('BTC')
            chart_html = ChartGenerator.generate_ranking_chart('BTC', btc_data)
            
            # Here you would typically save or display the chart
            logger.info("Chart generated successfully.")
            
            logger.info(f"Waiting for {UPDATE_INTERVAL} seconds before next update...")
            time.sleep(UPDATE_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Shutting down...")
    finally:
        data_processor.close()

if __name__ == "__main__":
    main()