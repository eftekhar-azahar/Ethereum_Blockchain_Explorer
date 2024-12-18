Ethereum Blockchain Explorer

Overview

The Ethereum Blockchain Explorer is a Flask-based web application that interacts with the Ethereum blockchain. It enables users to:

View the latest block details.

Check the connection status to the Ethereum network.

Retrieve transaction details by entering a transaction hash.

The project leverages the Web3.py library to connect to the Ethereum network and Infura as an HTTP provider.

Features

1. Blockchain Information

Fetches and displays the latest block number.

Shows the connection status to the Ethereum network.

Provides detailed information about the latest block.

2. Transaction Lookup

Allows users to input a transaction hash.

Retrieves and displays transaction details, such as:

From and To addresses

Gas used

Value transferred

Project Structure

Key Files

app.py

Core logic for interacting with the Ethereum blockchain.

Routes:

/: Displays the latest block details and connection status.

Templates Folder

Contains HTML files for rendering the user interface.

Code Highlights

Connection to the Ethereum network using Infura:

Eth = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(Eth))

Fetching blockchain information:

def get_blockchain_info():
    latest_block_number = w3.eth.blockNumber
    connection_status = w3.isConnected()
    latest_block = w3.eth.get_block('latest')
    return latest_block_number, connection_status, latest_block

Transaction lookup:

def get_latest_transaction_info(input_text):
    transaction = w3.eth.getTransaction(input_text)
    return transaction

Prerequisites

1. Software Requirements

Python 3.7+

Flask

Web3.py

2. Setup Infura

Create an account on Infura.

Create a new project and get your Infura Project ID.

Replace YOUR_INFURA_PROJECT_ID in app.py with your actual project ID.

Installation and Setup

Clone the repository:

git clone https://github.com/your-username/Ethereum_Blockchain_Explorer.git

Navigate to the project directory:

cd Ethereum_Blockchain_Explorer

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open your browser and go to:

http://127.0.0.1:5000/

Usage

Home Page

Displays the latest block number and connection status.

Shows details of the latest block.

Transaction Lookup

Enter a transaction hash to retrieve its details.

Future Enhancements

Search by Address: Allow users to fetch transactions and balance for an Ethereum address.

Block Explorer: Add functionality to browse blocks and transactions.

Front-End Framework: Use React or Angular for an enhanced user interface.

License

This project is licensed under the MIT License.

