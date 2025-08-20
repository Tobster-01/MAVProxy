import subprocess
subprocess.run([
    "gst-launch-1.0",
    "rtspsrc", f"location=rtsp://127.0.0.1:8554/camera", "protocols=tcp", "latency=0", "drop-on-latency=true",
    "!", "rtph264depay", "!", "avdec_h264", "!", "videoconvert", "!", "fakesink"
])
