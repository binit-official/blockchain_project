from .block import Block

class Blockchain:
    """
    The Blockchain class manages the chain of blocks, transactions, mining (Proof-of-Work), 
    and validation. It ensures data integrity by linking blocks through hashes.
    """

    def __init__(self):
        """
        Initializes the blockchain with the genesis block.
        """
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain, known as the 'Genesis Block'.
        This block has a fixed previous hash of '0' since it has no predecessor.
        """
        return Block(0, "Genesis Block", "0")

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the list of pending transactions.
        Transactions are stored temporarily before being added to a new block.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self, difficulty=4):
        """
        Mines a new block using Proof-of-Work.
        - The block's hash must start with a certain number of leading zeros (difficulty).
        - This makes block creation computationally intensive.
        """
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), self.pending_transactions, last_block.hash)

        print(f"Mining Block {new_block.block_id}...")

        # Proof-of-Work: Adjust nonce until a valid hash is found
        while not new_block.hash.startswith("0" * difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        print(f"Block {new_block.block_id} successfully mined: {new_block.hash}")

        self.chain.append(new_block)
        self.pending_transactions = []  # Clear transactions after mining

    def validate_chain(self):
        """
        Checks if the blockchain is valid by verifying:
        - The hash of each block matches its computed hash.
        - The previous hash in each block matches the hash of the previous block.
        If any inconsistency is found, the blockchain is considered tampered.
        """
        for i in range(1, len(self.chain)):
            current, previous = self.chain[i], self.chain[i - 1]

            # Check if current block's hash is still valid
            if current.hash != current.compute_hash():
                print(f"Warning: Data tampered in Block {current.block_id}.")
                return False

            # Check if the block correctly references the previous block
            if current.prev_hash != previous.hash:
                print(f"Warning: Block {current.block_id} has an incorrect previous hash.")
                return False

        return True

    def display_chain(self):
        """
        Prints all blocks in the blockchain in a structured format.
        """
        print("\nBlockchain Structure:")
        for block in self.chain:
            print(block)
