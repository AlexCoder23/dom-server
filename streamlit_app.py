# import os, datetime, time, sys, json, traceback, html, importlib, requests
from quart import (Quart, redirect, url_for, session, request, jsonify, render_template, Blueprint)
# from quart_compress import Compress
# import socketio
# import blueprints, api, sockets

HOST = 'real-dog-together.ngrok-free.app'
  
app = Quart(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET']
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MAX_CONTENT_LENGTH'] = 4*1024*1024*1024
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.jinja_env.auto_reload = True
# compress = Compress(app)
app.permanent_session_lifetime = datetime.timedelta(days=7)
# sio = socketio.AsyncServer(
#   async_mode='asgi',
# )

# blueprints.load(app)
# sockets.load(sio)

@app.errorhandler(404)
async def page_404(e):
  return await render_template('404Page.html')

# asgi = socketio.ASGIApp(sio, app)
