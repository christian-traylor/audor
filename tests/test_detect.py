def test_transcription_and_scan():
    from audor.detect import transcribe_audio, scan_for_swear_words
    transcription_result = transcribe_audio('tests/extracted_audio.wav')
    assert transcription_result is not None
    swear_word_timestamps = scan_for_swear_words(transcription_result)
    assert swear_word_timestamps is not None
    assert len(swear_word_timestamps) == 13
    
