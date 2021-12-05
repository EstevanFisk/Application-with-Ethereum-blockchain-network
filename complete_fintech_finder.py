# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a Fintech Finder
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally sign a transaction that pays a Fintech Finder candidate, and send
# this transaction to the Ganache blockchain.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to the Transactions
# section of Ganache to review the blockchain transaction details. 

################################################################################
# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
################################################################################
# Import Ethereum Transaction Functions into the Fintech Finder Application

# In this section, you'll import several functions from the `crypto_wallet.py`
# script into the file `fintech_finder.py`, which contains code for Fintech
# Finder’s customer interface, in order to add wallet operations to the
# application. For this section, you will assume the perspective of a Fintech
# Finder customer (i.e., you’ll provide your Ethereum wallet and account
# information to the application).

# Complete the following steps:

# 1. Review the code contained in the `crypto_wallet.py` script file. Note that
# the Ethereum transaction functions that you have built throughout this
# module-including `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`,
# `estimateGas`, `sendRawTransaction`, and others&mdash;have now been
# incorporated into Python functions that allow you to automate the process of
# accessing them.

# 2. Add your mnemonic seed phrase (provided by Ganache) to the starter code’s `SAMPLE.env` file.
# When the information has been added, rename the file `.env`.

# 3. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the Fintech Finder customer’s (in this
# case, your) HD wallet and Ethereum account.

# 5. Within this same section of the `fintech_finder.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function
# and pass it your Ethereum `account.address`.


################################################################################

# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

from crypto_wallet import generate_account, get_balance, send_transaction

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane": ["Lane", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "Mod_2/Mod2_challenge/Starter_Code/Images/lane.jpeg"],
    "Ash": ["Ash", "0x33C3fA51E89C509d43A48B2D316044Fda1181465", "5.0", .33, "Mod_2/Mod2_challenge/Starter_Code/Images/ash.jpeg"],
    "Jo": ["Jo", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "Mod_2/Mod2_challenge/Starter_Code/Images/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "Mod_2/Mod2_challenge/Starter_Code/Images/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = ["Lane", "Ash", "Jo", "Kendall"]


# Function to describe each candidate on webpage
def get_people(w3):
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        st.image(db_list[number][4], width=200)
        st.write("Name: ", db_list[number][0])
        st.write("Ethereum Account Address: ", db_list[number][1])
        st.write("FinTech Finder Rating: ", db_list[number][2])
        st.write("Hourly Rate per Ether: ", db_list[number][3], "eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Fintech Finder!")
st.markdown("## Hire A Fintech Professional!")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################

# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
st.sidebar.write(get_balance(w3, account.address))

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select a Person', people)

# Create a input field to record the number of hours the candidate worked
hours = st.sidebar.number_input("Number of Hours")

st.sidebar.markdown("## Candidate Name, Hourly Rate, and Ethereum Address")

# Identify the FinTech Hire candidate
candidate = candidate_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write(candidate)

# Identify the FinTech Finder candidate's hourly rate
hourly_rate = candidate_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write(hourly_rate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = candidate_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write(candidate_address)

# Write the Fintech Finder candidate's name to the sidebar

st.sidebar.markdown("## Total Wage in Ether")


##########################################

# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = candidate_database[person][3] * hours

# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.write(wage)

##########################################


if st.sidebar.button("Send Transaction"):

    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    transaction_hash= send_transaction(w3, account, candidate_address, wage)
     

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_people(w3)

################################################################################
# Inspect the Transaction

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash in Ganache.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run fintech_finder.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to Ganache, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

