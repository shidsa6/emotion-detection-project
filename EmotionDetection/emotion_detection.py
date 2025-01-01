import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check for blank input
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:  # Check for server errors
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
        
        formatted_response = json.loads(response.text)
        emotions = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})
        if emotions:
            dominant_emotion = max(emotions, key=emotions.get)
            return {
                "anger": emotions.get("anger", 0),
                "disgust": emotions.get("disgust", 0),
                "fear": emotions.get("fear", 0),
                "joy": emotions.get("joy", 0),
                "sadness": emotions.get("sadness", 0),
                "dominant_emotion": dominant_emotion
            }
        else:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }
    except Exception as e:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }