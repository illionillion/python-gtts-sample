from gtts import gTTS
import IPython.display
import os

def get_input(prompt, valid_inputs):
    """
    ユーザーに指定したプロンプトを表示し、有効な入力を待ちます。
    
    Parameters:
        prompt (str): ユーザーに表示するメッセージ。
        valid_inputs (list): 有効な入力のリスト。

    Returns:
        str: ユーザーが入力した有効な値。
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_inputs:
            return user_input
        print("無効な入力です。もう一度入力してください。")

def get_filename_without_extension(file_name):
    """
    ファイル名から拡張子を除いた部分を取得します。

    Parameters:
        file_name (str): ファイル名。

    Returns:
        str: 拡張子を除いたファイル名。
    """
    while True:
        base_name, extension = os.path.splitext(file_name)
        if extension:
            file_name = base_name
        else:
            return file_name

def main():
    # Get the input message
    message = input("変換したいテキストを入力してください：")

    # Get the language choice (either 'ja' or 'en')
    language = get_input("言語を選択してください（'ja' for 日本語, 'en' for English）：", ['ja', 'en'])

    # Get the file name
    file_name = input("ファイル名を入力してください：")

    # Get the file name without extension
    file_name_without_extension = get_filename_without_extension(file_name)

    # Convert text to speech
    tts = gTTS(message, lang=language)
    mp3_file_name = f"{file_name_without_extension}.mp3"
    tts.save(mp3_file_name)

    # Play the audio
    IPython.display.Audio(mp3_file_name)

if __name__ == "__main__":
    main()
