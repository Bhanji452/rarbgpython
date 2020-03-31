import rarbgapi
import tmdbsimple as tmdb
import copy
from tabulate import tabulate

tmdb.API_KEY = 'c4169d47ae1ad053b921a9df127f69bc'

TV_HD = 41
TV_UHD = 49
MOV_720 = 45
MOV_1080 = 44
MOV_4K = 51
LOGO_BASE = "https://image.tmdb.org/t/p/h60"
POSTER_BASE = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"
BACKDROP_BASE = "https://image.tmdb.org/t/p/w1066_and_h600_bestv2"
MOV_DATA_TEMP = {"Title":"","Overview":"","Release":"","Budget":"","Runtime":"","Poster":"","Backdrop":""}
MOV_TOR_TEMP = {"Filename":"","Magnet":"","Category":"","Seeders":"","Size":""}
TV_DATA_TEMP = {"Overview":"","Poster":"","Backdrop":"","next_ep":"","last_ep":"","net_name":"","net_logo":""}
TV_TOR_TEMP = {"Title:":"","Filename":"","Magnet":"","Category":"","Size":"","Episode":"","Season":"","Seeders":""}
TORRENTS = []


def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)

def movieDBm(identifier):
	data = copy.deepcopy(MOV_DATA_TEMP)
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
		backdropLink= "NONE"
	data["Title"] = title
	data["Overview"] = summary
	data["Release"] = release
	data["Budget"] = budget
	data["Runtime"] = runtime
	data["Poster"] = posterLink
	data["Backdrop"] = backdropLink
	return data

def movieDBt(identifier):
	dataT = copy.deepcopy(TV_DATA_TEMP)
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
	network = networks[0]
	networkName = network.get('name')
	networkLogo = network.get('logo_path')
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
	return dataT
	

	
	
	

	

def searchRAR(contentType,contentName):
	client = rarbgapi.RarbgAPI()
	client.list(limit=50)
	if contentType == 1:
		categoryType = raw_input("Select a Category (0) - All, (1) - HD , (2) - UHD : ")
		if categoryType == "0":
			contentCategory = 0
		elif categoryType == "1":
			contentCategory = TV_HD
		elif categoryType == "2":
			contentCategory = TV_UHD
		else:
			contentType = 0 
		print("\n\n")
		for torrent in client.search(search_string=contentName, category=contentCategory, format_="json_extended", sort="seeders"):
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
			dataObject = [dataTV,tvTorData]
			TORRENTS.append(dataObject)
			
	elif contentType == 2:
		categoryType = raw_input("Select a Category (0) - All, (1) - 720p , (2) - 1080p, (3) - 4K : ")
		if categoryType == "0":
			contentCategory = 0
		elif categoryType == "1":
			contentCategory = MOV_720
		elif categoryType == "2":
			contentCategory = MOV_1080
		elif categoryType == "3":
			contentCategory = MOV_4K
		else:
			contentType = 0 
		for torrent in client.search(search_string=contentName, category=contentCategory, format_="json_extended", sort="seeders"):
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
			dataObject = [dataP1,torData]
			TORRENTS.append(dataObject)
	else:
		print("The Content type you have selected is unavailable!")

######
#Main#
######

def main():
	torrentNum = 0
	tOf = int(input("TV (1) or Film (2) ? : "))
	search = raw_input("Please enter the name of the Content : ")
	searchRAR(tOf,search)
	table = []
	if tOf == 2:
		for each in TORRENTS:
			tor = TORRENTS[torrentNum]
			movieData = tor[0]
			torrentData = tor[1]
			title = str(movieData.get("Title"))
			filename = str(torrentData.get("Filename"))
			size = str(torrentData.get("Size"))
			seeders = str(torrentData.get("Seeders"))
			torrentNumStr = str(torrentNum + 1)
			tableObject = [title,filename,size,seeders]
			table.append(tableObject)
			torrentNum = torrentNum + 1
		print(tabulate(table, headers=["Title","Filename","Filesize","Seeders"]))
	elif tOf == 1:
		for each in TORRENTS:
			tor = TORRENTS[torrentNum]
			tvData = tor[0]
			torrentData = tor[1]
			title = str(torrentData.get("Title"))
			filename = str(torrentData.get("Filename"))
			size = str(torrentData.get("Size"))
			seeders = str(torrentData.get("Seeders"))
			tableObject = [title,filename,size,seeders]
			table.append(tableObject)
			torrentNum = torrentNum + 1
		print(tabulate(table, headers=["Title","Filename","Filesize","Seeders"]))
if __name__ == "__main__":
	main()


