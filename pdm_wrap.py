import numpy as np
import pandas as pd
from PdmModule.PdMApi import PdmModule


class PdM_wrap:

    def __init__(self):
        self.streamModule = PdmModule()

    def collect_data(self, temp_data):
        timestamp = pd.to_datetime(temp_data["timestamp"])
        id = str(temp_data["source"])
        data = np.array(temp_data["features"])

        prediction = self.streamModule.collect_data(timestamp=timestamp, data=data, id=id)

        notes = prediction.notes.split(",")[1:]
        dictionary_to_return = {
            "source": id,
            "timestamp": temp_data["timestamp"],
            "alarm": prediction.alarm,
            "scores": [float(sc) for sc in notes[:len(data)]],
            "thresholds": [th for th in notes[len(data):]],
            "description": prediction.ensemble_details
        }
        return dictionary_to_return

    def collect_event(self, temp_data):
        timestamp = pd.to_datetime(temp_data["timestamp"])
        id = temp_data["source"]
        self.streamModule.collect_event(timestamp=timestamp, desc="reset", id=id)
