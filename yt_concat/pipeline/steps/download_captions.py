from pytube import YouTube

from .step import Step, StepException


class DownloadCaptions(Step):

    def process(self, data, inputs, utils):
        
        for url in data:
            if utils.caption_file_exists:
                print('found existing caption file')
                continue

            source = YouTube(url)
            en_caption = source.captions.get_by_language_code('a.en')
            en_caption_convert_to_srt =(en_caption.generate_srt_captions())
            print(en_caption_convert_to_srt)

            text_file = open(utils.get_caption_path(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            break
        
        