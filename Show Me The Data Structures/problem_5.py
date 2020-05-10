import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash() 
        self.next = None 

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_data = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        hash_str = hash_data.encode('utf-8')

        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self):
        return f'Block >> timestamp: {str(self.timestamp)}, data: {str(self.data)}, prev_hash: ...{str(self.previous_hash)[-10:]}, hash: ...{str(self.hash)[-10:]}'


class BlockChain:

    def __init__(self):
        self.head = None
        self.size = 0


    def append(self, data):

        if type(data) is not str:
            return

        if self.head is None:
            self.head = Block(datetime.datetime.now(datetime.timezone.utc), data, None)
            self.size += 1
            return 

        prev_block = self.head
        curr_block = self.head.next

        while curr_block is not None:
            prev_block = curr_block
            curr_block = prev_block.next

        new_block = Block(datetime.datetime.now(
            datetime.timezone.utc), data, prev_block.hash)
        prev_block.next = new_block
        
        self.size += 1

    def to_list(self):
        block_list = list()
        
        node = self.head
        while node is not None:
            block_list.append(node)
            node = node.next

        return block_list
    

########################################################
##                      TEST CASES                    ##
########################################################

print("\n\n___ TEST 1 ___")

chain = BlockChain()
chain.append("data 1")
chain.append("data 2")
chain.append("data 3")
for block in chain.to_list():
    print(block)
# Expected 3 blocks data 1, data 2, data 3 with correct hashes pairs (None, hash1), (hash1, hash2), (hash2, hash3) 

print("\n\n___ TEST 2 ___")

chain = BlockChain()
chain.append(None)
chain.append("")
chain.append(123)
for block in chain.to_list():
    print(block)
# Expected 1 block data: '' 

print("\n\n___ TEST 3 ___")

chain = BlockChain()
chain.append(Block(datetime.datetime.now, "Data 1", "123"))
for block in chain.to_list():
    print(block)
# Expected 0 blocks 
