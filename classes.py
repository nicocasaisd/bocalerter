from datetime_controller import parse_datetime

class Match:
    def __init__(self, date, local, _ ,visitor, hour, tournament):
        self.date_str = date
        self.date_obj = parse_datetime(date)
        self.local = local
        self.visitor = visitor
        self.hour = hour
        self.tournament = tournament
