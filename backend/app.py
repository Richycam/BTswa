# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import shutil
from models import SIEM, siem_instance, Map, map_instance, Banner, banner_instance

app = Flask(__name__)
CORS(app) 

NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"  

if not siem_instance.get_tool():
    siem_instance.set_tool("Elastic")
if not siem_instance.get_link():
    siem_instance.set_link("https://www.elastic.co/")

@app.route('/siem/link', methods=['GET'])
def get_siem_link():
    """Return the SIEM tool link."""
    return jsonify({'link': siem_instance.get_link()})

@app.route('/siem/docs', methods=['GET'])
def get_siem_docs():
    """Return the SIEM documentation link based on the tool."""
    tool = siem_instance.get_tool().lower()
    if tool in ["kibana", "elastic"]:
        doc_link = "https://www.elastic.co/guide/index.html"
    elif tool == "splunk":
        doc_link = "https://docs.splunk.com/Documentation"
    elif tool == "velociraptor":
        doc_link = "https://docs.velociraptor.app/docs/"
    else:
        doc_link = "Documentation not found for the SIEM tool."
    return jsonify({'docs': doc_link})

@app.route('/siem', methods=['POST'])
def set_siem():
    """
    Set the SIEM tool name and link.
    Expects JSON payload with 'tool' and 'link'.
    """
    data = request.get_json()
    tool = data.get('tool')
    link = data.get('link')
    
    if not tool or not link:
        return jsonify({'error': 'Both "tool" and "link" are required.'}), 400
    
    siem_instance.set_tool(tool)
    siem_instance.set_link(link)
    
    return jsonify({'message': f'SIEM tool set to {tool} with link {link}.'}), 200

@app.route('/nmap', methods=['POST'])
def run_nmap():
    data = request.get_json()
    ip = data.get('ip')
    scan_type = data.get('scan_type')
    
    if not ip or not scan_type:
        return jsonify({'error': 'IP address and scan type are required.'}), 400
    
    if scan_type == 'simple':
        command = ['nmap', ip]
    elif scan_type == 'version':
        command = ['nmap', '-A', ip]
    else:
        return jsonify({'error': 'Invalid scan type.'}), 400
    
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500
    
    return jsonify({'output': output})

@app.route('/tcpdump', methods=['GET'])
def run_tcpdump():
    """
    Run tcpdump command.
    Note: Requires appropriate system permissions.
    """
    command = ['tcpdump', '-c', '30', '-i', 'any']
    
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        output = result.stdout
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.stderr}), 500
    
    return jsonify({'output': output})

@app.route('/worldmap', methods=['GET'])
def get_worldmap():
    """
    Return the ASCII art world map.
    """
    ascii_map = map_instance.get_map()
    return jsonify({'map': ascii_map})

@app.route('/check_password', methods=['POST'])
def check_password():
    """
    Check if a password exists in the provided wordlist.
    Expects JSON payload with 'password' and 'wordlist'.
    """
    data = request.get_json()
    password = data.get('password')
    wordlist = data.get('wordlist')
    
    if not password or not wordlist:
        return jsonify({'error': 'Password and wordlist are required.'}), 400
    
    words = wordlist.splitlines()
    if password in words:
        message = "The password is in the wordlist!"
    else:
        message = "The password is not in the wordlist!"
    
    return jsonify({'message': message})

@app.route('/banner', methods=['GET'])
def get_banner():
    """
    Return the current banner and header.
    """
    banner1 = banner_instance.get_banner1()
    banner2 = banner_instance.get_banner2()
    header = banner_instance.get_header()
    
    return jsonify({
        'banner1': banner1,
        'banner2': banner2,
        'header': header
    })

@app.route('/banner', methods=['POST'])
def set_banner():
    """
    Update the banners and header.
    Expects JSON payload with 'banner1', 'banner2', and 'header'.
    """
    data = request.get_json()
    banner1 = data.get('banner1')
    banner2 = data.get('banner2')
    header = data.get('header')
    
    if not banner1 or not banner2 or not header:
        return jsonify({'error': 'All "banner1", "banner2", and "header" fields are required.'}), 400
    
    banner_instance.set_banner1(banner1)
    banner_instance.set_banner2(banner2)
    banner_instance.set_header(header)
    
    return jsonify({'message': 'Banners and header updated successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
