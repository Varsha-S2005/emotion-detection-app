from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Watson NLP Authentication
authenticator = IAMAuthenticator("YOUR_IBM_API_KEY")
nlp = NaturalLanguageUnderstandingV1(
    version="2021-08-01",
    authenticator=authenticator
)
nlp.set_service_url("YOUR_IBM_SERVICE_URL")

def emotion_predictor(text):
    response = nlp.analyze(
        text=text,
        features=Features(emotion=EmotionOptions()),
        language="en"
    ).get_result()
    return response["emotion"]["document"]["emotion"]


