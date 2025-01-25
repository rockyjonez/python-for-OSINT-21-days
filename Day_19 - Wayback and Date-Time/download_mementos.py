import wayback
from datetime import datetime

client = wayback.WaybackClient()

for record in client.search('https://nasa.gov', to_date=datetime(1999, 1, 1)):

    memento = client.get_memento(record)

    # Replace slashes and colons with underscores in the filename
    fileName = memento.memento_url.replace("/", "_").replace(":", "_") + ".html"

    memento_file = open(fileName, "a")

    memento_file.write(memento.text)

    memento_file.close()

    print (fileName)
