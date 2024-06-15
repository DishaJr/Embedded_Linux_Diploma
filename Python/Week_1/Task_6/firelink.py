import webbrowser

websites = {"Facebook":"https://www.facebook.com/", "Youtube":"https://www.youtube.com/"}
urls = ["Facebook", "Youtube"]

def firefox(url):
    firefox_path="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open(websites[urls[int(url)-1]])
