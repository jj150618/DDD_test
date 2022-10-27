from services.predict_dust.domain.predict_dust_service import InferenceModelExecutor
from services.predict_dust.domain.entity import region_dict
import tensorflow as tf
import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class InferenceModelExecutorImpl(InferenceModelExecutor):
    def __init__(self,) -> None:
        super().__init__()

    def inference(self, input_array, region:str):
        model = tf.keras.models.load_model(
            path.dirname(path.dirname(path.abspath(__file__))) + f'/infrastructure/model/2019_'+region_dict[region]+'.h5'
        )
        dust_result = model.predict(input_array)

        return float(dust_result)
