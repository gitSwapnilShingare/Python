import logging

logging.basicConfig(
    level=logging.INFO,  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Pipeline started 🚀")
logging.warning("Missing values found in 'sales'")
logging.error("DB connection failed! 💥")
