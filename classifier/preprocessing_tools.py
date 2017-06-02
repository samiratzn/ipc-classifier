"""Provide utility functions for text preprocessing"""
import classifier
from bs4 import BeautifulSoup

def _clean_ipc_list(list_ipc):
    list_ipc_clean = [element['ic'] for element in list_ipc if not isinstance(element, str)]
    return list_ipc_clean

def _extract_fields(text_patent):
    soup = BeautifulSoup(text_patent, "lxml")
    tag_record = soup.record
    number = tag_record['pn']
    tag_ipcs = soup.ipcs
    ipcs = tag_ipcs['mc']
    list_ipc = _clean_ipc_list(tag_ipcs.contents)
    tag_abstract = soup.ab
    abstract = tag_abstract.text
    return classifier.models.PatentDocument(number, ipcs, list_ipc, abstract)
