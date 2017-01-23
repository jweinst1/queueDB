#file that implements the stack data source object

import struct

class DataQueue:

    #Indicates number of bytes to read for each data type
    LENGTH_KEYS = {
        b'c':1,
        b'i':4,
        b'?':1,
        b'l':8
    }

    def __init__(self, file_name):
        self.name = ".{f}.oqueue".format(f=file_name)
        try:
            self.queue = open(self.name, 'rb+')
        except FileNotFoundError:
            self.queue = open(self.name, 'wb+')

    def __del__(self):
        self.queue.close()

    def __len__(self):
        self.queue.seek(0)
        length = 0
        cur_byte = self.queue.read(1)
        while cur_byte != '':
            try:
                unp = struct.unpack('c', cur_byte)[0]
                if unp in DataQueue.LENGTH_KEYS:
                    self.queue.read(DataQueue.LENGTH_KEYS[unp])
                    length += 1
                    cur_byte = self.queue.read(1)
                else:
                    raise KeyError("Unknown Data Type {0}".format(unp))
            except struct.error:
                return length
        return length


    # = specifies no padding
    def push_int(self, elem):
        #Pushes an integer onto the data queue
        self.queue.write(struct.pack('=ci', b'i', elem))

    def push_long(self, elem):
        #Pushes a long onto the data queue
        self.queue.write(struct.pack('=cl', b'l', elem))

    def push_bool(self, elem):
        #Pushes a boolean onto the data queue
        self.queue.write(struct.pack('=c?', b'?', elem))

    def push_char(self, elem):
        #Pushes a char onto the data queue
        self.queue.write(struct.pack('=cc', b'c', elem))

    def pop(self):
        #returns the first item in the queue and deletes it
        self.queue.seek(0)
        data_key = self.queue.read(1)
        byte_key = struct.unpack('c', data_key)[0]
        if byte_key in DataQueue.LENGTH_KEYS:
            data = struct.unpack(str(data_key, 'utf-8'), self.queue.read(DataQueue.LENGTH_KEYS[byte_key]))
            tail = self.queue.read()
            self.queue.seek(0)
            self.queue.truncate()
            self.queue.seek(0)
            self.queue.write(tail)
            return data
        else:
            raise KeyError("Unknown Data Type {0}".format(byte_key))
