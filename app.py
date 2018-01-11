from flask import Flask, request, jsonify
import mpd

app = Flask(__name__)
mpd_client = mpd.MPDClient(use_unicode=True)

@app.route("/music", methods=["GET"])
def get_all_music():
  mpd_client.connect("localhost", 6600)
  list_info = mpd_client.lsinfo("/")
  mpd_client.disconnect()
  return jsonify(list_info)

# TODO: Need to figure out how to list by artist
#@app.route("/music/<artist>", methods=["GET"])
#def get_music_artist(artist):
#  return jsonify(mpd_client.lsinfo("/" + artist))

@app.route("/status", methods=["GET"])
def get_status():
  mpd_client.connect("localhost", 6600)
  status = mpd_client.status()
  mpd_client.disconnect()
  return jsonify(status)

@app.route("/status/<status_id>", methods=["GET"])
def status_with_id(status_id):
  mpd_client.connect("localhost", 6600)
  if status_id in mpd_client.status():
    status = mpd_client.status()[status_id]
  else:
    status = {"ERROR": "Status Key Not Found"}
  mpd_client.disconnect()
  return jsonify({status_id: status})

@app.route("/play", methods=["GET"])
def press_play():
  mpd_client.connect("localhost", 6600)
  mpd_client.play()
  state = mpd_client.status()['state']
  mpd_client.disconnect()
  return jsonify({"state": state})

@app.route("/pause", methods=["GET"])
def press_pause():
  mpd_client.connect("localhost", 6600)
  mpd_client.pause()
  state = mpd_client.status()['state']
  mpd_client.disconnect()
  return jsonify({"state": state})


if __name__ == '__main__':
    app.run(debug=True)
