import http.client
import json
import logging
import ssl
import sys

# ===============================================================================
#  GLOBAL DECLARATIONS
# ===============================================================================

server_url = "127.0.0.1:5000"


# ===============================================================================
#  PRIVATE FUNCTIONS
# ===============================================================================

def __get(url):
    """Reads data from url.

    Parameters:
    url (string): /computer/{serialnumber}

    Returns:
    json: Computer object. None if serialnumber not found or failed to contact Jamf API."""
    try:
        conn = http.client.HTTPSConnection(
            server_url, context=ssl._create_unverified_context())

        # Generate credentials with
        # printf "username:password" | iconv -p ISO-8859-1 | base64 -i -

        headers = {
            'Accept': 'application/json'
        }

        # conn.request("GET", "/JSSResource/computers/serialnumber/%s" % (serialnumber),
        #             headers=headers)

        conn.request("GET", url, headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        data = json.loads(data)
        return data
    except Exception as err:
        logging.error(
            "[GET] {0} - HTTP status: {1}. {2}".format(server_url + url, res.status, err))
        return None


def __put(url, payload):
    """PUT data to Jamf Pro.

    Parameters:
    url: /computer/{serialnumber}
    payload: json formatted data"""
    try:
        conn = http.client.HTTPSConnection(
            server_url, context=ssl._create_unverified_context())

        headers = {
            'Content-type': 'application/json'
        }

        conn.request("PUT", url, json.dumps(payload), headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data
    except Exception as err:
        if 'res' in locals():
            logging.error(
                "[PUT] {0} - HTTP status: {1}. {2}".format(server_url + url, res.status, err))
        else:
            logging.error(
                "[PUT] {0} - Error: {1}".format(server_url + url, err))
        return None


def __del(url):
    """DELETE inventory data from url.

    Parameters:
    url: /computer/{serialnumber}
    """
    try:
        conn = http.client.HTTPSConnection(
            server_url, context=ssl._create_unverified_context())

        # Generate credentials with
        # printf "username:password" | iconv -t ISO-8859-1 | base64 -i -
        headers = {
            'Accept': 'application/xml'
        }

        conn.request("DELETE", url, headers=headers)
        res = conn.getresponse()
        # Exit if error was found
        if res.status != 200:
            raise Exception("")
        data = res.read().decode("utf-8")
        return data
    except Exception as err:
        if 'res' in locals():
            logging.error(
                "[DELETE] {0} - HTTP status: {1}. {2}".format(server_url + url, res.status, err))
        else:
            logging.error(
                "[DELETE] {0} - Error: {1}".format(server_url + url, err))
        return None


# ===============================================================================
#  PUBLIC FUNCTIONS
# ===============================================================================


# DELETE METHODS
def delete_inventory(serialNuber):
    url = "computer/%ss" % serialNuber
    data = __del(url)
    data = ""
    return data


# PUT METHODS
def update_inventory(serialNumber, payload):
    url = "/computer/%s" % serialNumber
    data = __put(url, payload)
    return data


# GET METHODS
def get_computer_basic():
    url = "/foo/bar"
    data = __get(url)
    return data
