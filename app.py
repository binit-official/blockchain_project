from blockchain.blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    # Adding transactions to be included in the next block
    blockchain.add_transaction("Alice sends 2 BTC to Bob")
    blockchain.add_transaction("Charlie pays 5 BTC to Eve")

    # Mining a new block
    print("\nMining Block 1...")
    blockchain.mine_block()

    # Adding more transactions
    blockchain.add_transaction("Eve transfers 3 BTC to Dave")

    # Mining another block
    print("\nMining Block 2...")
    blockchain.mine_block()

    # Displaying the blockchain
    print("\nBlockchain Structure:")
    blockchain.display_chain()

    # Validating the blockchain
    print("\nBlockchain valid?", blockchain.validate_chain())

    # Simulating tampering with the blockchain
    print("\nAttempting to tamper with a block...")
    blockchain.chain[1].transactions = "Alice sends 1000 BTC to Malicious User"

    # Checking if the blockchain detects tampering
    print("\nBlockchain valid after tampering?", blockchain.validate_chain())
