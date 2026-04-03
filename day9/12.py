class WiFiDevice:
    def connect_wifi(self):
        print("Connecting to WiFi...")

class VoiceAssistant:
    def voice_control(self):
        print("Voice control activated")

class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def play_music(self):
        print("Playing music...")

speaker = SmartSpeaker()

speaker.connect_wifi()
speaker.voice_control()
speaker.play_music()
