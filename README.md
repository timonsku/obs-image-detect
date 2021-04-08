# obs-image-detect
A quick hack to do image classification on an OBS stream and do some audio/video actions based on that. Requires OBS Vitual Cam plugin or another way to pipe the video of the stream into python.

Train a model using https://lobe.ai/
Then export that to Tensorflow. In the `detector.py` adjust either the path of the `model_dir` or place the file into the exported model directory and execute it from there.
Instead of lobe you can use any other tensorflow model too of course. You might not be able to use the convinience wrapper from lobe for that, I have not tested it.

All the code here is doing is communicate from python to a MQTT broker which is picked up by a local web UI loaded into OBS, you can plug anything you want into the backend.

The code was made to detect a bird in a nest (https://twitter.com/timonsku/status/1379523345650233356)
So all names in the code will refer to that, you may want to change that.

Install Python dependencies:
```
pip3 install git+https://github.com/lobe/lobe-python --no-cache-dir
pip3 install paho-mqtt opencv-python
```

Adjust the `index.html` file to your liking. You want to replace the sound and webp animation with your own.
Then adjust the label to the ones used in your trained model.

Requires an MQTT broker to send and recieve the detections from python to the web UI. By default it assumes you have a local broker installed.
If you don't have a broker install https://mosquitto.org/download/

Lastly load the index.html into the Browser source of OBS. Tick local file and tick the control audio option if you want audio from the UI to play in the stream.
