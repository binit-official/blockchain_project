import hashlib
import json
import datetime

class Block:
    """
    A single block in the blockchain.
    Each block contains an index, timestamp, transactions, previous hash, and its own hash.
    """

    def __init__(self, block_id, transactions, prev_hash, nonce=0):
        self.block_id = block_id
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Computes the SHA-256 hash of the block's contents.
        Ensures data integrity and security.
        """
        block_data = json.dumps({
            "block_id": self.block_id,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "prev_hash": self.prev_hash,
            "nonce": self.nonce
        }, sort_keys=True)

        return hashlib.sha256(block_data.encode()).hexdigest()

    def __str__(self):
        """
        Returns a readable string representation of the block for easy debugging.
        """
        return f"Block {self.block_id} | Hash: {self.hash[:10]}... | Prev: {self.prev_hash[:10]}... | Tx: {self.transactions}"
