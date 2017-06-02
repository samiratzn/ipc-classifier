"""Provide data models"""
class PatentDocument(object):
    """A model for a IPC patent"""
    def __init__(self, number, ipcs, list_ipc, abstract):
        self.number = number
        self.ipcs = ipcs
        self.list_ipc = list_ipc
        self.abstract = abstract
