'''
Enter your Binance API keys here.
'''

from dotenv import load_dotenv

load_dotenv()

API_KEY_BINANCE = os.getenv('BINANCE_KEY')
API_SECRET_BINANCE = os.getenv('BINANCE_SECRET')
