from yt_concate.pipeline.steps.step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR


class Downloadvideos(Step):
    def process(self, data, inputs, utils):
        print(len(data))
        yt_set = set([found.yt for found in data])
        print('videos to download=', len(yt_set))


        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloding', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
            break

        return data
