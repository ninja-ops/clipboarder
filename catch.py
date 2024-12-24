import sys
import time
import os
import pyperclip
import validators
import base64, binascii
import requests
import hashlib
import subprocess

recent_value = ""

DOMAIN_SCRIPT = ""
if os.environ.get("DOMAIN_SCRIPT") is not None:
  DOMAIN_SCRIPT = os.environ.get("DOMAIN_SCRIPT")

IPV4_SCRIPT = ""
if os.environ.get("IPV4_SCRIPT") is not None:
  IPV4_SCRIPT = os.environ.get("IPV4_SCRIPT")

URL_SCRIPT = ""
if os.environ.get("URL_SCRIPT") is not None:
  URL_SCRIPT = os.environ.get("URL_SCRIPT")

EMAIL_SCRIPT = ""
if os.environ.get("EMAIL_SCRIPT") is not None:
  EMAIL_SCRIPT = os.environ.get("EMAIL_SCRIPT")

BASE64_SCRIPT = ""
if os.environ.get("BASE64_SCRIPT") is not None:
  BASE64_SCRIPT = os.environ.get("BASE64_SCRIPT")

CATCH_ALL_PIPE = ""
if os.environ.get("CATCH_ALL_PIPE") is not None:
  CATCH_ALL_PIPE = os.environ.get("CATCH_ALL_PIPE")

while True:
  tmp_value = pyperclip.paste()
  if tmp_value != recent_value:
    recent_value = tmp_value
    str_value = str(recent_value)
    md5 = hashlib.md5(str_value.encode()).hexdigest()
    print(md5)
    print("? '%s'" % str(recent_value).encode())

    if validators.domain(str_value):
      if DOMAIN_SCRIPT != "":
        print("EXECUTE DOMAIN_SCRIPT")
        p = subprocess.call([DOMAIN_SCRIPT, str_value])
        print()

    if validators.ipv4(str_value):
      if IPV4_SCRIPT != "":
        print("EXECUTE IPV4_SCRIPT")
        p = subprocess.call([IPV4_SCRIPT, str_value])
        print()

    if validators.url(str_value):
      if URL_SCRIPT != "":
        print("EXECUTE URL_SCRIPT")
        p = subprocess.call([URL_SCRIPT, str_value])
        print()

    if validators.email(str_value):
      if EMAIL_SCRIPT != "":
        print("EXECUTE EMAIL_SCRIPT")
        p = subprocess.call([EMAIL_SCRIPT, str_value])
        print()

    try:
      data = base64.b64decode(str_value, validate=True)
      if BASE64_SCRIPT != "":
        print("EXECUTE BASE64_SCRIPT")
        os.system(BASE64_SCRIPT + " {}" . format(str_value))
    except:
      time.sleep(0.1)

    if CATCH_ALL_PIPE != "":
      print("EXECUTE CATCH_ALL_PIPE")
      catch_all = subprocess.Popen([CATCH_ALL_PIPE], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      catch_all.stdin.write(bytes(str_value + "\n", 'utf-8'))
      out, err = catch_all.communicate()
      catch_all.stdin.close()
      print(out.decode())

    print()

  time.sleep(0.1)
