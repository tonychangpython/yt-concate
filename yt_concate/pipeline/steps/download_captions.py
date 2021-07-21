import os
import time


from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from .step import StepException



class DownloadCaptions(Step):
    def process(self, data, inputs, utils):

        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except (AttributeError, KeyError):
                print('Error when downloading caption for', yt.url)
                continue


            # save the caption to a file named Output.txt
            text_file = open(yt.get_caption_filepath(), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
        end = time.time()
        print('took ', end - start, 'seconds')

        return data
