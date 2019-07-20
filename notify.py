import notify

watcher = notify.Watcher()

watcher.add('/tmp/file', notify.IN_MODIFY)

watcher.read()