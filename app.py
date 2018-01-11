from flask import Flask, request, jsonify
import mpd

app = Flask(__name__)
mpd_client = mpd.MPDClient(use_unicode=True)
mpd_client.connect("localhost", 6600)

@app.route("/music", methods=["GET"])
def get_all_music():
  return jsonify(mpd_client.lsinfo("/"))

# TODO: Need to figure out how to list by artist
#@app.route("/music/<artist>", methods=["GET"])
#def get_music_artist(artist):
#  return jsonify(mpd_client.lsinfo("/" + artist))

@app.route("/status", methods=["GET"])
def get_status():
  return jsonify(mpd_client.status())

@app.route("/status/<status_id>", methods=["GET"])
def status_with_id(status_id):
  if status_id in mpd_client.status():
    return jsonify(mpd_client.status()[status_id])
  else:
    return jsonify({"ERROR": "Status Key Not Found"})

@app.route("/play", methods=["GET"])
def press_play():
  return jsonify(mpd_client.play())

@app.route("/pause", methods=["GET"])
def press_pause():
  return jsonify(mpd_client.pause())

@app.route("/state", methods=["PUT"])
def toggle_state():
  if mpd_client.status()['state'] == 'play':
    mpd_client.pause()
  else:
    mpd_client.play()


if __name__ == '__main__':
    app.run(debug=True)
