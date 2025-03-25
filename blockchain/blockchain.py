from .block import Block

class Blockchain:
    """
    The Blockchain class manages a list of blocks, transaction handling, mining, and validation.
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
        """
        return Block(0, "Genesis Block", "0")

    def add_transaction(self, transaction):
        """
        Adds a new transaction to the list of pending transactions.
        Transactions are stored temporarily before being added to a new block.
        """
        self.pending_transactions.append(transaction)

    def mine_block(self, difficulty=3):
        """
        Mines a new block by solving a Proof-of-Work problem.
        The difficulty defines how many leading zeros the block hash must have.
        """
        last_block = self.chain[-1]
        new_block = Block(len(self.chain), self.pending_transactions, last_block.hash)

        while not new_block.hash.startswith("0" * difficulty):
            new_block.nonce += 1
            new_block.hash = new_block.compute_hash()

        self.chain.append(new_block)
        self.pending_transactions = []  # Clear transactions after mining

    def validate_chain(self):
        """
        Checks if the blockchain is valid by verifying the hashes of all blocks.
        Detects any tampering in the chain.
        """
        for i in range(1, len(self.chain)):
            current, previous = self.chain[i], self.chain[i - 1]

            if current.hash != current.compute_hash():
                print(f"Warning: Data tampered in Block {current.block_id}.")
                return False

            if current.prev_hash != previous.hash:
                print(f"Warning: Block {current.block_id} has an incorrect previous hash.")
                return False

        return True

    def display_chain(self):
        """
        Prints all blocks in the blockchain in a structured format.
        """
        for block in self.chain:
            print(block)
