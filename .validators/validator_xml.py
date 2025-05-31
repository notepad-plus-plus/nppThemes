#!/usr/local/bin/python3

import os
import io
import sys

import requests
from lxml import etree
import json

api_url = os.environ.get('APPVEYOR_API_URL')
has_error = False


def post_error(message):
    global has_error

    has_error = True

    message = {
        "message": message,
        "category": "error",
        "details": ""
    }

    if api_url:
        requests.post(api_url + "api/build/messages", json=message)
    else:
        from pprint import pprint
        pprint(message)


def parse_xml_file(filename_xml, filename_xsd = None):

    # parse xml
    try:
        doc = etree.parse(filename_xml)
        print(f'{filename_xml} vs parser: XML WELL-FORMED, SYNTAX OK')

    # check for file IO error
    except IOError:
        #print('Invalid File')
        post_error(f'{filename_xml}: IOError Invalid File')

    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
        #print('XML Syntax Error, see error_syntax.log')
        post_error(f'{filename_xml}: {str(err.error_log)}: XMLSyntaxError Invalid File')

    except:
        #print('Unknown error.')
        post_error(f'{filename_xml}: Unknown error. Maybe check that no xml version is in the first line.')


    ##### check XML using XSD
    if filename_xsd is not None:
        try:
            xmlschema_doc = etree.parse(filename_xsd)

        # error reading XSD
        except IOError:
            post_error(f'{filename_xml} | {filename_xsd}: IOError Invalid File')
            return

        # error parsing XSD
        except etree.XMLSyntaxError as err:
            post_error(f'{filename_xml} | {filename_xsd}: {str(err.error_log)}: XMLSyntaxError Invalid File')
            return

        # other error
        except Exception as err:
            post_error(f'{filename_xml} | {filename_xsd}: Unknown error {str(err.error_log)} reading Schema .xsd file.')
            return

        # Next, extract the schema object from the schema_doc
        try:
            xmlschema = etree.XMLSchema(xmlschema_doc)
            #print(f'{filename_xml} | {filename_xsd}: SCHEMA OBJECT OK')

        # error with Schema
        except etree.XMLSchemaError as err:
            post_error(f'{filename_xml} | {filename_xsd}: {str(err.error_log)}: XMLSchemaError')
            return

        # other error
        except Exception as err:
            post_error(f'{filename_xml} | {filename_xsd}: Unknown error {str(err.error_log)} obtaining schema object')
            return

        # finally, validate the XML against the schema
        if not xmlschema.validate(doc):
            post_error(f'{filename_xml} | {filename_xsd}: Validation error {str(xmlschema.error_log)}')
            return
        else:
            print(f'{filename_xml} vs schema: VALIDATION OK')

def parse_xml_files_from_themes_dir():
    xml_list = []
    for file in os.listdir("themes"):
        if file.endswith(".xml"):
            #print(os.path.join("themes", file))
            parse_xml_file(os.path.join("themes", file), os.path.join(".validators", "theme.xsd"))
            xml_list.append(file)
    return xml_list

def output_json_toc(tocname, xlst):
    #print(f'{tocname} =>\n' + json.dumps(sorted(xlst, key=str.casefold), indent=4))
    with open(tocname, "w", encoding="utf8") as toc_file:
        json.dump(sorted(xlst, key=str.casefold), toc_file, indent=4)

my_list = parse_xml_files_from_themes_dir()
output_json_toc('themes/.toc.json', my_list)

if has_error:
    sys.exit(-2)
else:
    sys.exit()
