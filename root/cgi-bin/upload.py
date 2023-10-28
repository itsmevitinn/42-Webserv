#!/usr/bin/python3

import os, cgi, sys

form = cgi.FieldStorage()

form_data = form["filename"]

if form_data.filename:
    if not os.path.exists("uploads"):
        os.mkdir("uploads")

    open("uploads/" + form_data.filename, "wb").write(form_data.file.read())

    response = b"<html>"
    response += b"<p>Your file has been uploaded successfully!</p>"
    response += b"</html>"

    sys.stdout.buffer.write(b"HTTP/1.1 200 OK\r\n")
    sys.stdout.buffer.write(b"Content-Length: " + str(len(response)).encode("utf-8") + b"\r\n")
    sys.stdout.buffer.write(b"\r\n")
    sys.stdout.buffer.write(response)
else:
    response = b"<html>"
    response += b"<p>No file was uploaded</p>"
    response += b"</html>"

    sys.stdout.buffer.write(b"HTTP/1.1 400 Bad Request")
    sys.stdout.buffer.write(b"Content-Length: " + str(len(response)).encode("utf-8") + b"\r\n")
    sys.stdout.buffer.write(b"\r\n")
    sys.stdout.buffer.write(response)
