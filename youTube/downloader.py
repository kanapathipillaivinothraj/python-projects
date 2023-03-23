from pytube import YouTube


def py_download(youtube_link):
    # download  the youtube link
    YouTube_Download = YouTube(youtube_link).streams.get_lowest_resolution()
    # get_highest_resolution()
    try:
        print(f" {YouTube_Download} is downloading..... ")
        YouTube_Download.download("A_project/youtube/")
        print(f" {YouTube_Download} is downloaded ")
    except AttributeError:
        print(f" fail download {YouTube_Download} \n AttributeError sorry! ")


youtube_link = str(input("Enter your Youtube download link : "))
py_download(youtube_link)
