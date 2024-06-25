#!/usr/bin/env python
# coding: utf-8

import argparse
from lxml import etree
import json
import os
import sys

def xsd_to_json_schema(element):
    schema = {}
    
    if element.tag.endswith('schema'):
        schema['$schema'] = 'http://json-schema.org/draft-07/schema#'
        schema['type'] = 'object'
        schema['properties'] = {}
        schema['required'] = []

        for child in element:
            if child.tag.endswith('element'):
                child_name = child.get('name')
                if child_name:
                    schema['properties'][child_name] = xsd_element_to_json_schema(child)
                    if child.get('minOccurs') != '0':
                        schema['required'].append(child_name)
    
    return schema

def xsd_element_to_json_schema(element):
    element_schema = {}
    element_type = element.get('type')

    if element_type:
        element_schema['type'] = xsd_type_to_json_type(element_type)
    else:
        for child in element:
            if child.tag.endswith('complexType'):
                element_schema.update(xsd_complex_type_to_json_schema(child))
            elif child.tag.endswith('simpleType'):
                element_schema['type'] = 'string'
    
    return element_schema

def xsd_complex_type_to_json_schema(element):
    complex_schema = {'type': 'object', 'properties': {}, 'required': []}

    for child in element:
        if child.tag.endswith('sequence'):
            for seq_child in child:
                child_name = seq_child.get('name')
                if child_name:
                    complex_schema['properties'][child_name] = xsd_element_to_json_schema(seq_child)
                    if seq_child.get('minOccurs') != '0':
                        complex_schema['required'].append(child_name)
    
    return complex_schema

def xsd_type_to_json_type(xsd_type):
    mapping = {
        'xs:string': 'string',
        'xs:integer': 'integer',
        'xs:decimal': 'number',
        'xs:boolean': 'boolean',
        'xs:date': 'string',
        'xs:dateTime': 'string',
        'xs:time': 'string'
    }
    return mapping.get(xsd_type, 'string')

def xsd_to_json_schema_file(xsd_file_path):
    with open(xsd_file_path, 'rb') as file:
        xml_content = file.read()
    
    root = etree.XML(xml_content)
    schema_dict = xsd_to_json_schema(root)
    
    # Determine the JSON Schema file path
    base_name = os.path.splitext(xsd_file_path)[0]
    json_schema_file_path = base_name + '.json'
    
    with open(json_schema_file_path, 'w') as json_file:
        json.dump(schema_dict, json_file, indent=4)
    
    print(f"Converted {xsd_file_path} to {json_schema_file_path} successfully.")
    return json_schema_file_path

def is_jupyter_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config: 
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True

if __name__ == "__main__":
    if is_jupyter_notebook():
        # If in a Jupyter Notebook, skip argument parsing
        xsd_file_path = 'path/to/your/xsdfile.xsd'  # Update this path as needed
        xsd_to_json_schema_file(xsd_file_path)
    else: #for cli
        parser = argparse.ArgumentParser(description='Convert XSD to JSON Schema')
        parser.add_argument('xsd_file_path', type=str, help='The path to the XSD file')
        args = parser.parse_args()
        
        xsd_to_json_schema_file(args.xsd_file_path)
