from gtts import gTTS
import pdfplumber
from pathlib import Path
import playsound


def convertPdfIntoMp3(filepath: str, language: str = 'en'):
    if Path(filepath).is_file() and Path(filepath).suffix == '.pdf':
        with pdfplumber.PDF(open(file=filepath, mode='rb')) as pdf:

            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(filepath).stem
        audio.save(f'{file_name}.mp3')
        return 1
    else:
        return -1


def main():
    result = convertPdfIntoMp3(filepath='C:\\Users\\gomoz\\PycharmProjects\\PDFintoMP3\\Вместо тепла зелень стекла.pdf',
                               language='ru')
    if result == 1:
        print('File converted successfully!!')
    else:
        print('Something went wrong. Check if there is such a file')


if __name__ == '__main__':
    main()
