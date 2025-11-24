"""
File: filemodel.py
Project 9.4

Data model for a file viewer.  Supports navigation
through the lines of a file.
"""

from linkedlist import LinkedList

class FileModel(object):

    def __init__(self, filename):
        self.backingStore = LinkedList()
        with open(filename, "r") as file:
            for line in file:
                self.backingStore.append(line)

        self.currentline = "\n"
        # self.cursor = filename.

    def first(self):
        self.cursor = self.backingStore.head.next
        self.index = 0
        return self.cursor.data

    def last(self):
        self.cursor = self.backingStore.head.previous
        self.index = len(self.backingStore) - 1
        return self.cursor.data

    def next(self):
        if self.index == len(self.backingStore):
            return None
        self.cursor = self.cursor.next
        self.index += 1
        return self.cursor.data

    def previous(self):
        if self.index == 0:
            return None
        self.cursor = self.cursor.previous
        self.index -= 1
        return self.cursor.data



