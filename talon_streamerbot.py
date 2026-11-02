
import json
import urllib.request
import urllib.error

from talon import Module

mod = Module()

STREAMERBOT_URL = "http://127.0.0.1:7474/DoAction"
ACTION_NAME = "Talon Speech Test"


@mod.action_class
class Actions:

    def streamerbot_send_transcript(transcript: list[str]):
        """Send recognized Talon speech to Streamer.bot."""

        # Convert Talon's word list into normal text
        text = " ".join(transcript).strip()

        if not text:
            return

        payload = {
            "action": {
                "name": ACTION_NAME
            },
            "args": {
                "transcript": text
            }
        }

        body = json.dumps(payload).encode("utf-8")

        request = urllib.request.Request(
            STREAMERBOT_URL,
            data=body,
            headers={
                "Content-Type": "application/json"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(request, timeout=5) as response:
                print("Streamer.bot:", response.status)

        except urllib.error.HTTPError as error:
            print("HTTP error:", error.code)
            print("Response:", error.read().decode("utf-8"))

        except Exception as error:
            print("Connection error:", repr(error))
