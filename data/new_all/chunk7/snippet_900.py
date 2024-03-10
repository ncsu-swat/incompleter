# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72526346/typeerror-must-be-real-number-not-nonetype-moviepy-write-videofile
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from moviepy.editor import *
    _l_(394512)

except ImportError:
    pass
try:
    from os import walk
    _l_(394514)

except ImportError:
    pass
try:
    from random import randint as rand
    _l_(394516)

except ImportError:
    pass

def makeVideo(videoCounter, picturePath, audioPath, stockPath, musicPath, outputPath, emptyPath):
    _l_(394707)


    #Get files
    myAudioFiles = _c_(394521, _n_(394517, "next", lambda: next), _c_(394520, _n_(394518, "walk", lambda: walk), _n_(394519, "audioPath", lambda: audioPath)), (None, None, []))[2]
    _l_(394522)
    myImageFiles = _c_(394527, _n_(394523, "next", lambda: next), _c_(394526, _n_(394524, "walk", lambda: walk), _n_(394525, "picturePath", lambda: picturePath)), (None, None, []))[2]
    _l_(394528)

    #Make audio file (without music)
    audio = []
    _l_(394529)
    emptyAudio = _c_(394532, _n_(394530, "AudioFileClip", lambda: AudioFileClip), _n_(394531, "emptyPath", lambda: emptyPath)+'\\'+'emptyAudio.mp3')
    _l_(394533)
    for counter1 in _c_(394538, _n_(394534, "range", lambda: range), _c_(394537, _n_(394535, "len", lambda: len), _n_(394536, "myAudioFiles", lambda: myAudioFiles))):
        _l_(394561)

        theAudio = _c_(394545, _n_(394539, "AudioFileClip", lambda: AudioFileClip), _n_(394540, "audioPath", lambda: audioPath)+'\\'+_c_(394544, _n_(394541, "str", lambda: str), _n_(394542, "myAudioFiles", lambda: myAudioFiles)[_n_(394543, "counter1", lambda: counter1)]))
        _l_(394546)
        theAudio = _c_(394549, _a_(394548, _n_(394547, "theAudio", lambda: theAudio), "subclip"), 0,-0.1)
        _l_(394550)
        _c_(394554, _a_(394552, _n_(394551, "audio", lambda: audio), "append"), _n_(394553, "theAudio", lambda: theAudio))
        _l_(394555)
        _c_(394559, _a_(394557, _n_(394556, "audio", lambda: audio), "append"), _n_(394558, "emptyAudio", lambda: emptyAudio))
        _l_(394560)
    audioFiles = _c_(394564, _n_(394562, "concatenate_audioclips", lambda: concatenate_audioclips), _n_(394563, "audio", lambda: audio))
    _l_(394565)
    audioFiles = _c_(394568, _a_(394567, _n_(394566, "audioFiles", lambda: audioFiles), "set_fps"), 44100)
    _l_(394569)
    audioFiles = _c_(394572, _a_(394571, _n_(394570, "audioFiles", lambda: audioFiles), "volumex"), 2)
    _l_(394573)

    #Make comment video
    images = []
    _l_(394574)
    emptyImage = _c_(394577, _n_(394575, "ImageClip", lambda: ImageClip), _n_(394576, "emptyPath", lambda: emptyPath)+'\\'+'emptyImage.png', duration=0.5)
    _l_(394578)
    emptyImage = _c_(394581, _a_(394580, _n_(394579, "emptyImage", lambda: emptyImage), "set_opacity"), 0)
    _l_(394582)
    for counter2 in _c_(394587, _n_(394583, "range", lambda: range), _c_(394586, _n_(394584, "len", lambda: len), _n_(394585, "myImageFiles", lambda: myImageFiles))):
        _l_(394615)

        theImage = _c_(394599, _a_(394595, _c_(394594, _n_(394588, "ImageClip", lambda: ImageClip), _n_(394589, "picturePath", lambda: picturePath)+'\\'+_c_(394593, _n_(394590, "str", lambda: str), _n_(394591, "myImageFiles", lambda: myImageFiles)[_n_(394592, "counter2", lambda: counter2)])), "set_duration"), _a_(394598, _n_(394596, "audio", lambda: audio)[_n_(394597, "counter2", lambda: counter2)*2], "duration"))
        _l_(394600)
        theImage = _c_(394603, _a_(394602, _n_(394601, "theImage", lambda: theImage), "resize"), 2)
        _l_(394604)
        _c_(394608, _a_(394606, _n_(394605, "images", lambda: images), "append"), _n_(394607, "theImage", lambda: theImage))
        _l_(394609)
        _c_(394613, _a_(394611, _n_(394610, "images", lambda: images), "append"), _n_(394612, "emptyImage", lambda: emptyImage))
        _l_(394614)
    theImages = _c_(394618, _n_(394616, "concatenate_videoclips", lambda: concatenate_videoclips), _n_(394617, "images", lambda: images), method='compose')
    _l_(394619)
    theImages = _c_(394622, _a_(394621, _n_(394620, "theImages", lambda: theImages), "set_position"), ("center"))
    _l_(394623)
    theImages = _c_(394626, _a_(394625, _n_(394624, "theImages", lambda: theImages), "set_fps"), 10)
    _l_(394627)

    #Get stock video
    myStock = _c_(394632, _n_(394628, "next", lambda: next), _c_(394631, _n_(394629, "walk", lambda: walk), _n_(394630, "stockPath", lambda: stockPath)), (None, None, []))[2]
    _l_(394633)
    stockFile = _c_(394639, _n_(394634, "VideoFileClip", lambda: VideoFileClip), _n_(394635, "stockPath", lambda: stockPath)+'\\'+_c_(394638, _n_(394636, "str", lambda: str), _n_(394637, "myStock", lambda: myStock)[0]), target_resolution=(1080, 1920), audio=False)
    _l_(394640)
    stockFile = _c_(394643, _a_(394642, _n_(394641, "stockFile", lambda: stockFile), "subclip"), 0.5,-0.5)
    _l_(394644)
    stockFile = _c_(394649, _a_(394646, _n_(394645, "stockFile", lambda: stockFile), "loop"), duration = _a_(394648, _n_(394647, "theImages", lambda: theImages), "duration"))
    _l_(394650)
    stockFile = _c_(394653, _a_(394652, _n_(394651, "stockFile", lambda: stockFile), "set_fps"), 30)
    _l_(394654)

    #Get background music
    myMusic = _c_(394659, _n_(394655, "next", lambda: next), _c_(394658, _n_(394656, "walk", lambda: walk), _n_(394657, "musicPath", lambda: musicPath)), (None, None, []))[2]
    _l_(394660)

    #Make final audio and final video
    with _c_(394671, _n_(394661, "AudioFileClip", lambda: AudioFileClip), _n_(394662, "musicPath", lambda: musicPath)+'\\'+_c_(394670, _n_(394663, "str", lambda: str), _n_(394664, "myMusic", lambda: myMusic)[_c_(394669, _n_(394665, "rand", lambda: rand), 0,_c_(394668, _n_(394666, "len", lambda: len), _n_(394667, "myMusic", lambda: myMusic))-1)]), fps=44100) as musicFile:
        _l_(394706)

        musicFile = _c_(394677, _a_(394673, _n_(394672, "afx", lambda: afx), "audio_loop"), _n_(394674, "musicFile", lambda: musicFile), duration=_a_(394676, _n_(394675, "theImages", lambda: theImages), "duration"))
        _l_(394678)
        finalAudio = _c_(394682, _n_(394679, "CompositeAudioClip", lambda: CompositeAudioClip), [_n_(394680, "musicFile", lambda: musicFile), _n_(394681, "audioFiles", lambda: audioFiles)])
        _l_(394683)
        finalAudio = _c_(394686, _a_(394685, _n_(394684, "finalAudio", lambda: finalAudio), "set_fps"), 44100)
        _l_(394687)
        finalVideo = _c_(394691, _n_(394688, "CompositeVideoClip", lambda: CompositeVideoClip), [_n_(394689, "stockFile", lambda: stockFile), _n_(394690, "theImages", lambda: theImages)])
        _l_(394692)
        finalVideo = _c_(394696, _a_(394694, _n_(394693, "finalVideo", lambda: finalVideo), "set_audio"), _n_(394695, "finalAudio", lambda: finalAudio))
        _l_(394697)
        #v v v this line has the error v v v
        _c_(394704, _a_(394699, _n_(394698, "finalVideo", lambda: finalVideo), "write_videofile"), _n_(394700, "outputPath", lambda: outputPath)+'\\'+'finalVideo #'+_c_(394703, _n_(394701, "str", lambda: str), _n_(394702, "videoCounter", lambda: videoCounter))+'.mp4')
        _l_(394705)

PICTURE_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\topicAndCommentsPictures'       
_l_(394708)       
AUDIO_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\topicAndCommentsAudio'            
_l_(394709)            
STOCK_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\redditVideo\stockFootage'         
_l_(394710)         
MUSIC_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\permanentClips\Atmosphere'        
_l_(394711)        
OUTPUT_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\redditVideo\finalVideos'         
_l_(394712)         
THUMBNAIL_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\redditVideo\thumbnails'       
_l_(394713)       
PERMANENT_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\permanentClips\deadTopics'    
_l_(394714)    
EMPTY_FILES_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\permanentClips\emptyFiles'  
_l_(394715)  
UPLOAD_TO_YOUTUBE_PATH = r'C:\Users\jack_l\Documents\REDDIT_TO_YOUTUBE_PYTHON_SELENIUM\uploadToYoutube'      
_l_(394716)      

_c_(394724, _n_(394717, "makeVideo", lambda: makeVideo), 1, _n_(394718, "PICTURE_PATH", lambda: PICTURE_PATH), _n_(394719, "AUDIO_PATH", lambda: AUDIO_PATH), _n_(394720, "STOCK_PATH", lambda: STOCK_PATH), _n_(394721, "MUSIC_PATH", lambda: MUSIC_PATH), _n_(394722, "OUTPUT_PATH", lambda: OUTPUT_PATH), _n_(394723, "EMPTY_FILES_PATH", lambda: EMPTY_FILES_PATH))
_l_(394725)