# -*- coding: utf-8 -*-

import os, sys
import timeside

audio_file = sys.argv[-1]
audio_filename = audio_file.split(os.sep)[-1]
result_dir = '../results/'

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

decoder  = timeside.decoder.FileDecoder(audio_file)
graphers = timeside.core.processors(timeside.api.IGrapher)
encoders = timeside.core.processors(timeside.api.IEncoder)
analyzers = timeside.core.processors(timeside.api.IAnalyzer)

grapher_list = []
analyzer_list = []
encoder_list = []

pipe = decoder

for grapher in graphers:
    proc = grapher()
    grapher_list.append(proc)
    print proc.id()
    pipe = pipe | proc

for analyzer in analyzers:
    proc = analyzer()
    analyzer_list.append(proc)
    print proc.id()
    pipe = pipe | proc

for encoder in encoders:
    path = result_dir + os.sep + audio_filename + '.' + encoder.file_extension()
    proc = encoder(path, overwrite=True)
    encoder_list.append(proc)
    pipe = pipe | proc

print pipe
pipe.run()

for grapher in grapher_list:
    image = result_dir + os.sep + audio_filename + '-' + grapher.id() + '.png'
    grapher.render(image)

