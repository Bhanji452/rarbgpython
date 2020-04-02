import rarbgapi
import tmdbsimple as tmdb
import copy
import time
import os
from tabulate import tabulate
from flask import Flask, render_template,request,redirect, session
import random
import string
import uuid
import threading
tmdb.API_KEY = 'c4169d47ae1ad053b921a9df127f69bc'

app = Flask(__name__)
app.secret_key = os.urandom(20)
app.config["SESSION_TYPE"] = "filesystem"


chonk = ""

@app.route("/", methods=["GET","POST"])
def home():
    dokey = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    app.session_cookie_name = dokey
    #main()
    if request.method == "POST":
        print("SESSION: ")
        session.clear()
        print(dokey)
        print("CLEARED SESSION: ")
        #app.session_interface.make_null_session(app)
        SESSION = session._get_current_object()
        session.pop("Category",None)
        session.pop("TORRENTS",None)
        search = request.form["search"]
        category = request.form["category"]
        session["Category"] = ""
        session["Category"] = category
        chonk = copy.deepcopy(category)
        session["TORRENTS"] = []
        session["TORRENTS"].clear()
        session["TORRENTS"] = []
        tic = time.perf_counter()
        if category == "Movie":
            main(2,search)
            print("BEFORE REDIRECT: ",session["TORRENTS"])
            return redirect("/results")
        else:
            main(1,search)
            return redirect("/results")
        toc = time.perf_counter()
        print(toc - tic)
        return render_template("index.html")

    elif request.method == "GET":
        resp = app.make_response(render_template('index.html'))
        resp.set_cookie(dokey, "")
        return resp


@app.route("/results")
def results():
    if session["TORRENTS"] == []:
        return redirect("/")
    print(session["Category"])
    return render_template("results.html", content=session["TORRENTS"])


@app.route("/torrent0")
def detailed():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][0]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)


@app.route("/torrent1")
def detailed1():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][1]
    except:
        return redirect("/")

    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent2")
def detailed2():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][2]
    except:
        return redirect("/")

    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent3")
def detailed3():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][3]
    except:
        return redirect("/")

    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent4")
def detailed4():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][4]
    except:
        return redirect("/")

    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent5")
def detailed5():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][5]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent6")
def detailed6():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][6]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent7")
def detailed7():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][7]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent8")
def detailed8():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][8]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent9")
def detailed9():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][9]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent10")
def detailed10():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][10]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent11")
def detailed11():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][11]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent12")
def detailed12():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][12]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent13")
def detailed13():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][13]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent14")
def detailed14():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][14]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent15")
def detailed15():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][15]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent16")
def detailed16():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][16]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent17")
def detailed17():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][17]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent18")
def detailed18():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][18]
    except:
        return redirect("/")

    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent19")
def detailed19():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][19]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent20")
def detailed20():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][20]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent21")
def detailed21():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][21]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent22")
def detailed22():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][22]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent23")
def detailed23():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][23]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)

@app.route("/torrent24")
def detailed24():
    if session["TORRENTS"] ==  []:
        return redirect("/")
    try:
        data = session["TORRENTS"][24]
    except:
        return redirect("/")
    if session["Category"] == "TV":
        return render_template("detailedtv.html", content=data)
    else:
        return render_template("detailed.html", content=data)
TV_HD = 41
TV_UHD = 49
MOV_720 = 45
MOV_1080 = 44
MOV_4K = 51
LOGO_BASE = "https://image.tmdb.org/t/p/h60"
POSTER_BASE = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
BACKDROP_BASE = "https://image.tmdb.org/t/p/original"
MOV_DATA_TEMP = {"Title": "", "Overview": "", "Release": "", "Budget": "", "Runtime": "", "Poster": "", "Backdrop": ""}
MOV_TOR_TEMP = {"Filename": "", "Magnet": "", "Category": "", "Seeders": "", "Size": ""}
TV_DATA_TEMP = {"Title":"","Overview": "", "Poster": "", "Backdrop": "", "next_ep": "", "last_ep": "", "net_name": "",
                "net_logo": ""}
TV_TOR_TEMP = {"Title:": "", "Filename": "", "Magnet": "", "Category": "", "Size": "", "Episode": "", "Season": "",
               "Seeders": ""}


client = rarbgapi.RarbgAPI()
client.list(limit=100)


def humanbytes(B):
    'Return the given bytes as a human friendly KB, MB, GB, or TB string'
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2)  # 1,048,576
    GB = float(KB ** 3)  # 1,073,741,824
    TB = float(KB ** 4)  # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)


def movieDBm(identifier):
    data = copy.deepcopy(MOV_DATA_TEMP)
    try:
        movie = tmdb.Movies(identifier)
        response = movie.info()
        title = movie.title
        summary = response.get('overview')
        release = response.get('release_date')
        budget = movie.budget
        runtime = response.get('runtime')
        images = movie.images(include_image_language="en,null")
        poster = response.get('poster_path')
        backdrop = response.get('backdrop_path')
        try:
            posterLink = POSTER_BASE + poster
            backdropLink = BACKDROP_BASE + backdrop
        except:
            posterLink = "NONE"
            backdropLink = "NONE"
        data["Title"] = title
        data["Overview"] = summary
        data["Release"] = release
        data["Budget"] = budget
        data["Runtime"] = runtime
        data["Poster"] = posterLink
        data["Backdrop"] = backdropLink
    except:
        data["Title"] = "N/A"
        data["Overview"] = "N/A"
        data["Release"] = "N/A"
        data["Budget"] = "N/A"
        data["Runtime"] = "N/A"
        data["Poster"] = "/nofilm.png"
        data["Backdrop"] = "/nofilm.png"
    return data


def movieDBt(identifier):
    dataT = copy.deepcopy(TV_DATA_TEMP)
    try:
        tv = tmdb.TV(identifier)
        response = tv.info()
        summary = response.get('overview')
        poster = response.get('poster_path')
        backdrop = response.get('backdrop_path')
        lastepisode = response.get('last_episode_to_air')
        try:
            nextepisode = response.get('next_episode_to_air')
        except:
            nextepisode = "N/A"
        networks = response.get('networks')
        try:
            network = networks[0]
            networkName = network.get('name')
            networkLogo = network.get('logo_path')
        except:
            network = "Unknown"
            networkName = "Unavailable"
            networkLogo = "Unavailable"
        dataT["Overview"] = summary
        dataT["Poster"] = POSTER_BASE + poster
        dataT["Backdrop"] = BACKDROP_BASE + backdrop
        try:
            dataT["next_ep"] = nextepisode.get('name')
        except:
            dataT["next_ep"] = "N/A"
        dataT["last_ep"] = lastepisode.get('name')
        dataT["net_name"] = networkName
        dataT["net_logo"] = LOGO_BASE + networkLogo
    except:
        dataT["Overview"] = "Unavailable"
        dataT["Poster"] = "/nofilm.png"
        dataT["Backdrop"] = "Unavailable"
        dataT["next_ep"] = "Unavailable"
        dataT["last_ep"] = "Unavailable"
        dataT["net_name"] = "Unavailable"
        dataT["net_logo"] = "Unavailable"
    return dataT


def searchRAR(contentType, contentName):
    if contentType == 1:
        categoryType = "0"
        print("\n")
        if categoryType == "0":
            contentCategory = 0
        elif categoryType == "1":
            contentCategory = TV_HD
        elif categoryType == "2":
            contentCategory = TV_UHD
        else:
            contentType = 0
        print("\n")
        for torrent in client.search(search_string=contentName, category="18;41;49", format_="json_extended",
                                     sort="seeders"):
            tvTorData = copy.deepcopy(TV_TOR_TEMP)
            torrentName = torrent.filename
            torrentLink = torrent.download
            torrentCategory = torrent._raw['category']
            torrentSeeders = str(torrent._raw['seeders'])
            torrentSize = humanbytes(int(torrent._raw['size']))
            torrentInfo = torrent._raw['episode_info']
            torrentAirDate = torrentInfo.get('airdate')
            torrentIMDb = torrentInfo.get('imdb')
            torrentEpisodeNo = torrentInfo.get('epnum')
            torrentSeasonNo = torrentInfo.get('seasonnum')
            torrentTitle = torrentInfo.get('title')
            torrentTVdb = torrentInfo.get('themoviedb')
            dataTV = movieDBt(torrentTVdb)
            tvTorData["Title"] = torrentTitle
            tvTorData["Filename"] = torrentName
            tvTorData["Magnet"] = torrentLink
            tvTorData["Category"] = torrentCategory
            tvTorData["Size"] = torrentSize
            tvTorData["Episode"] = torrentEpisodeNo
            tvTorData["Season"] = torrentSeasonNo
            tvTorData["Seeders"] = torrentSeeders
            dataTV["Title"] = torrentTitle
            dataObject = [dataTV, tvTorData]
            session["TORRENTS"].append(dataObject)
            print(session["TORRENTS"])

    elif contentType == 2:
        categoryType = "0"
        print("\n")
        if categoryType == "0":
            contentCategory = 0
        elif categoryType == "1":
            contentCategory = MOV_720
        elif categoryType == "2":
            contentCategory = MOV_1080
        elif categoryType == "3":
            contentCategory = MOV_4K
        #print(contentCategory)
        for torrent in client.search(search_string=contentName, category="movies", format_="json_extended",
                                     sort="seeders"):
            torData = copy.deepcopy(MOV_TOR_TEMP)
            torrentName = torrent.filename
            torrentLink = torrent.download
            torrentCategory = torrent._raw['category']
            torrentSeeders = str(torrent._raw['seeders'])
            torrentSize = humanbytes(int(torrent._raw['size']))
            torrentInfo = torrent._raw['episode_info']
            try:
                torrentIMDb = torrentInfo.get('imdb')
                torrentMVdb = torrentInfo.get('themoviedb')
            except:
                pass
            dataP1 = movieDBm(torrentMVdb)
            torData["Filename"] = torrentName
            torData["Magnet"] = torrentLink
            torData["Category"] = torrentCategory
            torData["Seeders"] = torrentSeeders
            torData["Size"] = torrentSize
            dataObject = [dataP1, torData]
            session["TORRENTS"].append(dataObject)
            print(session["TORRENTS"])
    else:
        print("The Content type you have selected is unavailable!")


######
# Main#
######

def main(tOf,search):
    torrentNum = 0
    #tOf = int(input("TV (1) or Film (2) ? : "))
    #search = input("Please enter the name of the Content : ")
    tic = time.perf_counter()
    searchRAR(tOf, search)
    print("AFTER SEARCH",session["TORRENTS"])
    toc = time.perf_counter()
    print("SEARCH TIME", toc-tic)
    table = []
    if tOf == 2:
        for each in session["TORRENTS"]:
            tor = session["TORRENTS"][torrentNum]
            movieData = tor[0]
            torrentData = tor[1]
            title = str(movieData.get("Title"))
            filename = str(torrentData.get("Filename"))
            size = str(torrentData.get("Size"))
            seeders = str(torrentData.get("Seeders"))
            torrentNumStr = str(torrentNum + 1)
            tableObject = [title, filename, size, seeders]
            table.append(tableObject)
            torrentNum = torrentNum + 1
        print(tabulate(table, headers=["Title", "Filename", "Filesize", "Seeders"]))
    elif tOf == 1:
        for each in session["TORRENTS"]:
            tor = session["TORRENTS"][torrentNum]
            tvData = tor[0]
            torrentData = tor[1]
            title = str(torrentData.get("Title"))
            filename = str(torrentData.get("Filename"))
            size = str(torrentData.get("Size"))
            seeders = str(torrentData.get("Seeders"))
            tableObject = [title, filename, size, seeders]
            table.append(tableObject)
            torrentNum = torrentNum + 1
        print(tabulate(table, headers=["Title", "Filename", "Filesize", "Seeders"]))


if __name__ == "__main__":
    #main()
    app.run(host="0.0.0.0",port="80")
