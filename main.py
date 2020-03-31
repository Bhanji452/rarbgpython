import rarbgapi

TV_HD = 41
TV_UHD = 49
MOV_720 = 45
MOV_1080 = 44
MOV_4K = 51

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

def searchRAR(contentType,contentName):
	client = rarbgapi.RarbgAPI()
	client.list(limit=100)
	print(contentType)
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
		for torrent in client.search(search_string=contentName, category=contentCategory, format_="json_extended", sort="seeders"):
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
			print("======================================================================")
			print(torrentName+"\n\n")
			print(torrentTitle+"\n\n")
			print(torrentLink+"\n\n")
			print(torrentCategory+"\n\n")
			print(torrentSeeders+"\n\n")
			print(torrentSize+"\n\n")
			#print(str(torrentInfo)+"\n\n")
			print(torrentAirDate+"\n\n")
			print(torrentIMDb+"\n\n")
			print(torrentEpisodeNo+"\n\n")
			print(torrentSeasonNo+"\n\n")
			print("======================================================================")
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
			torrentName = torrent.filename
			torrentLink = torrent.download
			torrentCategory = torrent._raw['category']
			torrentSeeders = str(torrent._raw['seeders'])
			torrentSize = humanbytes(int(torrent._raw['size']))
			torrentInfo = torrent._raw['episode_info']
			#print(torrentInfo)
			torrentIMDb = torrentInfo.get('imdb')
			print("======================================================================")
			print(torrentName+"\n\n")
			print(torrentLink+"\n\n")
			print(torrentCategory+"\n\n")
			print(torrentSeeders+"\n\n")
			print(torrentSize+"\n\n")
			#print(str(torrentInfo)+"\n\n")
			print(torrentIMDb+"\n\n")
			print("======================================================================")
	else:
		print("The Content type you have selected is unavailable!")

######
#Main#
######

tOf = int(input("TV (1) or Film (2) ? : "))
search = raw_input("Please enter the name of the Content : ")
searchRAR(tOf,search)


