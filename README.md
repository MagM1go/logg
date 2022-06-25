```Python

from logg import Logger

log = Logger()

log.info("More info")
log.debug("Debug")
log.error("Some erorr")

```

# And you can customize colors by using config

## config.ini

```ini

[logger.log.colors] # Set your color
error = [1;31m
info = [1;32m
debug = [1;33m

```