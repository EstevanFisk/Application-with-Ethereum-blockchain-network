# Application-with-Ethereum-blockchain-network

## Overview
In this Streamlit application, you will assume the perspective of a "Fintech Finder" customer in order to do the following:  
- Generate a new Ethereum account instance by using the mnemonic seed phrase provided by Ganache.  
- Fetch and display the account balance associated with your Ethereum account address.  
- Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a Fintech Finder candidate for their work.  
- Digitally sign a transaction that pays a Fintech Finder candidate, and send this transaction to the Ganache blockchain.  
- Review the transaction hash code associated with the validated blockchain transaction.

![used_screen_interface](https://user-images.githubusercontent.com/46635638/144731055-e7c5873f-8c67-4f1f-8de6-27942c3217cd.PNG)



## Usage
To run the file application complete the following steps:

1. From your terminal, navigate to the project folder that contains your `.env` with your Ganach mnemonic seed phrase, `complete_fintech_finder.py`, and `crypto_wallet.py` files. Be sure to activate your Conda `dev` environment if it is not already active.

2. To launch the Streamlit application, type `streamlit run fintech_finder.py`.

### Libraries

````
# Imports
import os
import requests
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
from crypto_wallet import generate_account, get_balance, send_transaction
````

### Wallet Functionality

Below function creates a digital wallet and Ethereum account from a mnemonic seed phrase:
````
def generate_account():
    # Fetch mnemonic from environment variable.
    mnemonic = os.getenv("MNEMONIC")

    # Create Wallet Object
    wallet = Wallet(mnemonic)

    # Derive Ethereum Private Key
    private, public = wallet.derive_account("eth")

    # Convert private key into an Ethereum account
    account = Account.privateKeyToAccount(private)

    return account
````

Uses an Ethereum account address to access the balance of Ether:
````
def get_balance(w3, address):
    
    # Get balance of address in Wei
    wei_balance = w3.eth.get_balance(address)

    # Convert Wei value to ether
    ether = w3.fromWei(wei_balance, "ether")

    # Return the value in ether
    return ether
````


Sends an authorized transaction to the Ganache blockchain:
````
def send_transaction(w3, account, to, wage):
    
    # Set gas price strategy
    w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

    # Convert eth amount to Wei
    value = w3.toWei(wage, "ether")

    # Calculate gas estimate
    gasEstimate = w3.eth.estimateGas({"to": to, "from": account.address, "value": value})

    # Construct a raw transaction
    raw_tx = {
        "to": to,
        "from": account.address,
        "value": value,
        "gas": gasEstimate,
        "gasPrice": 0,
        "nonce": w3.eth.getTransactionCount(account.address)
    }

    # Sign the raw transaction with ethereum account
    signed_tx = account.signTransaction(raw_tx)

    # Send the signed transactions
    return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
````

## Example Transaction

Selecting options as shown on image one. We select Ash for 0.5 hours, which provides a wage of 0.165 in Ether. We see this transaction has decreased customer balance from 100 to 99.83 Eth (0.17 ether rounded to nearest hundredths):

![From_balance_hist](https://user-images.githubusercontent.com/46635638/144731168-73b854c7-40be-4965-b96f-9887d8ffdc87.PNG)



We also see the associated increase in balance for Ash's account as follows:

![To_balance_hist](https://user-images.githubusercontent.com/46635638/144731215-cc05c523-14bf-4eec-b75b-369f550c87bb.PNG)




Finally we inspect the transaction details as follows:


![transaction_details_1](https://user-images.githubusercontent.com/46635638/144731237-e85a1c09-0593-4e1c-90e6-bf6a60214bbd.PNG)

![transaction_details_2](https://user-images.githubusercontent.com/46635638/144731241-085210e1-061d-46f9-9ac2-576e71d269cc.PNG)


Thank you, and enjoy coding!
