from ibm_watson import TextToSpeechV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('API key')
tts = TextToSpeechV1(
    authenticator=authenticator
)

tts.set_service_url('the service url provided from IBM to you')

with open('./testHello.mp3', 'wb') as audio_file:
    res = tts.synthesize('Testing Hello Smart Method from Py Charm', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

print("The process is don")
