from ai.nlp.text_classifier import classify_text

def test_classify_text():
    result = classify_text("Urgent issue")
    assert result in ['urgent', 'normal']
