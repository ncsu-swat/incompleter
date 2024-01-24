# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75781036/can-anyone-help-me-with-speech-emotion-classifier-i-dont-know-what-to-do-about
#Extract features (mfcc, chroma, mel) from a sound file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_feature(file_name, **kwargs):
    _l_(609989)

    mfcc = _c_(609894, _a_(609893, _n_(609892, "kwargs", lambda: kwargs), "get"), "mfcc")
    _l_(609895)
    chroma = _c_(609898, _a_(609897, _n_(609896, "kwargs", lambda: kwargs), "get"), "chroma")
    _l_(609899)
    mel = _c_(609902, _a_(609901, _n_(609900, "kwargs", lambda: kwargs), "get"), "mel")
    _l_(609903)
    with _c_(609907, _a_(609905, _n_(609904, "soundfile", lambda: soundfile), "SoundFile"), _n_(609906, "file_name", lambda: file_name)) as sound_file:
        _l_(609986)

        X = _c_(609910, _a_(609909, _n_(609908, "sound_file", lambda: sound_file), "read"), dtype="float32")
        _l_(609911)
        sample_rate=_a_(609913, _n_(609912, "sound_file", lambda: sound_file), "samplerate")
        _l_(609914)
        if _n_(609915, "chroma", lambda: chroma):
            _l_(609928)

            stft=_c_(609922, _a_(609917, _n_(609916, "np", lambda: np), "abs"), _c_(609921, _a_(609919, _n_(609918, "librosa", lambda: librosa), "stft"), _n_(609920, "X", lambda: X)))
            _l_(609923)
            result=_c_(609926, _a_(609925, _n_(609924, "np", lambda: np), "array"), [])
            _l_(609927)
        if _n_(609929, "mfcc", lambda: mfcc):
            _l_(609947)

            mfccs=_c_(609939, _a_(609931, _n_(609930, "np", lambda: np), "mean"), _a_(609938, _c_(609937, _a_(609934, _a_(609933, _n_(609932, "librosa", lambda: librosa), "feature"), "mfcc"), y=_n_(609935, "X", lambda: X), sr=_n_(609936, "sample_rate", lambda: sample_rate), n_mfcc=40), "T"), axis=0)
            _l_(609940)
            result=_c_(609945, _a_(609942, _n_(609941, "np", lambda: np), "hstack"), (_n_(609943, "result", lambda: result), _n_(609944, "mfccs", lambda: mfccs)))
            _l_(609946)
        if _n_(609948, "chroma", lambda: chroma):
            _l_(609966)

            chroma=_c_(609958, _a_(609950, _n_(609949, "np", lambda: np), "mean"), _a_(609957, _c_(609956, _a_(609953, _a_(609952, _n_(609951, "librosa", lambda: librosa), "feature"), "chroma_stft"), S=_n_(609954, "stft", lambda: stft), sr=_n_(609955, "sample_rate", lambda: sample_rate)), "T"),axis=0)
            _l_(609959)
            result=_c_(609964, _a_(609961, _n_(609960, "np", lambda: np), "hstack"), (_n_(609962, "result", lambda: result), _n_(609963, "chroma", lambda: chroma)))
            _l_(609965)
        if _n_(609967, "mel", lambda: mel):
            _l_(609985)

            mel=_c_(609977, _a_(609969, _n_(609968, "np", lambda: np), "mean"), _a_(609976, _c_(609975, _a_(609972, _a_(609971, _n_(609970, "librosa", lambda: librosa), "feature"), "melspectrogram"), _n_(609973, "X", lambda: X), sr=_n_(609974, "sample_rate", lambda: sample_rate)), "T"),axis=0)
            _l_(609978)
            result=_c_(609983, _a_(609980, _n_(609979, "np", lambda: np), "hstack"), (_n_(609981, "result", lambda: result), _n_(609982, "mel", lambda: mel)))
            _l_(609984)
    aux = _n_(609987, "result", lambda: result)
    _l_(609988)
    return aux
# Emotions in the RAVDESS dataset
emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happiness',
  '04':'sadness',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}
_l_(609990)

#Emotions to observe
observed_emotions=['happiness', 'neutral', 'sadness']
_l_(609991)

#Load the data and extract features for each sound file
def load_data(test_size=0.2):
    _l_(610035)

    a,b=[],[]
    _l_(609992)
    for file in _c_(609995, _a_(609994, _n_(609993, "glob", lambda: glob), "glob"), "/content/drive/MyDrive/Depression detection/speech-emotion-recognition-ravdess-data/Actor_*/*.wav"):
        _l_(610025)

        file_name=_c_(610000, _a_(609998, _a_(609997, _n_(609996, "os", lambda: os), "path"), "basename"), _n_(609999, "file", lambda: file))
        _l_(610001)
        emotion=_n_(610002, "emotions", lambda: emotions)[_c_(610005, _a_(610004, _n_(610003, "file_name", lambda: file_name), "split"), "-")[2]]
        _l_(610006)
        if _n_(610007, "emotion", lambda: emotion) not in _n_(610008, "observed_emotions", lambda: observed_emotions):
            _l_(610010)

            continue
            _l_(610009)
        feature=_c_(610013, _n_(610011, "extract_feature", lambda: extract_feature), _n_(610012, "file", lambda: file), mfcc=True, chroma=True, mel=True)
        _l_(610014)
        _c_(610018, _a_(610016, _n_(610015, "a", lambda: a), "append"), _n_(610017, "feature", lambda: feature))
        _l_(610019)
        _c_(610023, _a_(610021, _n_(610020, "b", lambda: b), "append"), _n_(610022, "emotion", lambda: emotion))
        _l_(610024)
    aux = _c_(610033, _n_(610026, "train_test_split", lambda: train_test_split), _c_(610030, _a_(610028, _n_(610027, "np", lambda: np), "array"), _n_(610029, "a", lambda: a)), _n_(610031, "b", lambda: b), test_size=_n_(610032, "test_size", lambda: test_size), random_state=9)
    _l_(610034)
    return aux
#Split the dataset
atrain, atest, btrain, btest = _c_(610037, _n_(610036, "load_data", lambda: load_data), test_size=0.25)
_l_(610038)