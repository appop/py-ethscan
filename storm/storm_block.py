
import storm.locals


class block:
    __storm_table__ = "blocks"
    hash = storm.locals.Int(Primary = True)

