import spacy

def process_nlp(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    topics = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    sentiment = "Neutral"
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return topics, sentiment, entities