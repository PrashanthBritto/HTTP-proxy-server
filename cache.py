from collections import OrderedDict

QueueCache = OrderedDict()


# Cache Frame capacity

config = {
	
	'capacity': 10,
}

# Checking for the cache file

def isCached(file_name: str):
	if file_name in QueueCache:
		return True
	else:
		return False

# Returing the cache file name string

def getCachedFile(file_name: str) -> str:
	QueueCache.move_to_end(file_name)
	return QueueCache[file_name]

# Putting the cache file into QueueCache dict

def putCacheFile(file_name: str, cacheFile: str):
	QueueCache[file_name] = cacheFile
	QueueCache.move_to_end(file_name)
	if len(QueueCache) > config['capacity']:
		QueueCache.popitem(last = False)