#Source: https://stackoverflow.com/questions/69032946/python-process-typeerror-no-default-reduce-due-to-non-trivial-cinit
from aiohttp import web
from aiortc.mediastreams import MediaStreamTrack
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer
from pydub import AudioSegment
import av
from aiohttp import web
from aiortc.mediastreams import MediaStreamTrack
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer
from pydub import AudioSegment
import av
import pyaudio
import asyncio
import json
import os
from multiprocessing import Process, freeze_support, Queue
import sys
import threading
from time import sleep
import fractions
import time

class RadioServer(Process):
    def __init__(self,q):
        super().__init__()
        self.q = q
        self.ROOT = os.path.dirname(__file__)
        self.pcs = []
        self.channels = []
        self.stream_offers = []
    
    def run(self):
        self.app = web.Application()
        self.app.on_shutdown.append(self.on_shutdown)
        self.app.router.add_get("/", self.index)
        self.app.router.add_get("/telephone_calls.js", self.javascript)
        self.app.router.add_get("/jquery-3.5.1.min.js", self.jquery)
        self.app.router.add_post("/offer", self.offer)
        
        threading.Thread(target=self.fill_the_queues).start()
        web.run_app(self.app, access_log=None, host="192.168.1.20", port="8080", ssl_context=None)

    def fill_the_queues(self):
        while(True):
            frame = self.q.get()
            for stream_offer in self.stream_offers:
                stream_offer.q.put(frame)

    async def index(self,request):
        content = open(os.path.join(self.ROOT, "index.html"), encoding="utf8").read()
        return web.Response(content_type="text/html", text=content)


    async def javascript(self,request):
        content = open(os.path.join(self.ROOT, "telephone_calls.js"), encoding="utf8").read()
        return web.Response(content_type="application/javascript", text=content)

    async def jquery(self,request):
        content = open(os.path.join(self.ROOT, "jquery-3.5.1.min.js"), encoding="utf8").read()
        return web.Response(content_type="application/javascript", text=content)

    async def offer(self,request):  
        params = await request.json()
        offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

        pc = RTCPeerConnection()
        self.pcs.append(pc)

        # prepare epalxeis media
        self.stream_offers.append(CustomRadioStream())
        pc.addTrack(self.stream_offers[-1])

        #player = MediaPlayer(os.path.join(self.ROOT, "ΑΓΙΑ ΚΥΡΙΑΚΗ.mp3"))
        #pc.addTrack(player.audio)

        @pc.on("datachannel")
        def on_datachannel(channel):
            self.channels.append(channel)
            self.send_channel_message(str(len(self.pcs)))


        @pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            if pc.iceConnectionState == "failed":
                self.pcs.remove(pc)
                print("Current peer connections:"+str(len(self.pcs)))
            

        # handle offer
        await pc.setRemoteDescription(offer)

        # send answer
        answer = await pc.createAnswer()
        await pc.setLocalDescription(answer)
        
            

        return web.Response(content_type="application/json",text=json.dumps({"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}))

    async def on_shutdown(self,app):
        # close peer connections
        if self.pcs:
            coros = [pc.close() for pc in self.pcs]
            await asyncio.gather(*coros)
            self.pcs = []
            self.channels = []
            self.stream_offers = []
            
    def send_channel_message(self,message):
        for channel in self.channels:
            channel.send(message)
            

class CustomRadioStream(MediaStreamTrack):
    kind = "audio"
    
    def __init__(self):
        super().__init__()  # don't forget this!
        
        self.q = Queue()
        self._start = None
        
    async def recv(self):
        frame = self.q.get()
        frame_time = frame.time
        if self._start is None:
            self._start = time.time() - frame_time
        else:
            wait = self._start + frame_time - time.time()
            await asyncio.sleep(wait)
        return frame

class RadioOutputStream:
    def __init__(self,q):
        self.sample_rate = 44800
        self.AUDIO_PTIME = 0.744
        self.samples = int(self.AUDIO_PTIME * self.sample_rate)
        self.packet_time = 20

        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = self.sample_rate
        self.CHUNK = int(44100*0.744)

        
        self.files_directory = os.path.abspath(r"C:\Users\Χρήστος\Music\Αναστάσιμα τροπάρια ή άλλα τροπάρια Δεσποτικών, Θεομητορικών ή άλλων εορτών Αγίων")
        self.files_paths = os.listdir(self.files_directory)
        self.files_info = []
        for song_file in self.files_paths:
            if ".mp3" in song_file.lower():
                file_segment = AudioSegment.from_file(os.path.join(self.files_directory, song_file)).set_frame_rate(self.sample_rate)
                duration_milliseconds = len(file_segment)
                self.files_info.append({"file_segment":file_segment,"duration_milliseconds":duration_milliseconds})
        self.total_files = len(self.files_info)
        self.current_file = 0
        self.chunk_number = 0

        self.silence = AudioSegment.silent(duration=self.packet_time)

        self.q = q

        self.codec = av.CodecContext.create('pcm_s16le', 'r')
        self.codec.sample_rate = 44800
        self.codec.channels = 2

        self.audio_samples = 0
        
    def run_stream(self):
        while(True):
            if((self.chunk_number+1)*(self.packet_time)<=self.files_info[self.current_file]["duration_milliseconds"]):
                final_slice = self.files_info[self.current_file]["file_segment"][self.chunk_number*self.packet_time:(self.chunk_number+1)*self.packet_time]
                #final_slice = final_slice + 100
                self.chunk_number += 1

                packet = av.Packet(final_slice.raw_data)
                frame = self.codec.decode(packet)[0]
                frame.pts = self.audio_samples
                frame.time_base = fractions.Fraction(1, self.codec.sample_rate)
                self.audio_samples += frame.samples
                self.q.put(frame)
            else:
                if(self.chunk_number*self.packet_time<self.files_info[self.current_file]["duration_milliseconds"]):
                    final_slice = self.files_info[self.current_file]["file_segment"][self.chunk_number*self.packet_time:]
                    final_slice = final_slice + self.silence
                    #final_slice = final_slice + 100
                    self.chunk_number += 1


                    packet = av.Packet(final_slice.raw_data)
                    frame = self.codec.decode(packet)[0]
                    frame.pts = self.audio_samples
                    frame.time_base = fractions.Fraction(1, self.codec.sample_rate)
                    self.audio_samples += frame.samples
                    self.q.put(frame)
                else:
                    #start song from begin
                    self.chunk_number=0
                    if self.current_file==self.total_files-1:
                        self.current_file = 0
                    else:
                        self.current_file += 1
                    
            sleep(0.01)

if __name__ == "__main__":
    freeze_support()

    q = Queue()
    radio_stream = RadioOutputStream(q)
    threading.Thread(target=radio_stream.run_stream).start()

    custom_server_child_process = RadioServer(q)
    custom_server_child_process.start()
    print("Thread and process started sucessfully.")