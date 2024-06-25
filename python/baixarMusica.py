from pytube import YouTube
link = input('Digite o link da musica: ')
yt = YouTube(link)
print('Baixando...', yt.title)
resolucao = yt.streams.filter(only_audio=True, file_extension='mp4').first()
resolucao.download(output_path='.', filename='audio.mp3')
resolucao.download()
print('Download Concluido')