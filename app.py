from flask import Flask,render_template, request
from web3 import Web3


app = Flask(__name__)
Eth = "https://mainnet.infura.io/v3/3beb35814f274c01996224de0c825f95"
w3 = Web3(Web3.HTTPProvider(Eth))

def get_blockchain_info():
    latest_block_number = w3.eth.blockNumber
    connection_status = w3.isConnected()
    latest_block  = w3.eth.get_block('latest')
    return latest_block_number,connection_status,latest_block


def get_latest_transaction_info(input_text):
    transaction = w3.eth.getTransaction(input_text)
    return transaction

@app.route('/')
def index():
    latest_block_number,connection_status,latest_block = get_blockchain_info()
    return render_template('index.html',block=latest_block_number,connection=connection_status,latest_block=latest_block)


if __name__ == '__main__':
    app.run(debug=True)