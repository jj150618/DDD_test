from services.predict_dust.application.predict_dust_facade import PredictDustFacade
from services.predict_dust.domain.predict_dust_service import PredictDustServiceImpl
from services.predict_dust.infrastructure.make_input_executor import MakeInputExecutorImpl
from services.predict_dust.infrastructure.inference_model_executor import InferenceModelExecutorImpl

import sys
from os import path
sys.path.append(path.dirname(path.abspath(__file__)))

def get_predict_dust_DI():
    predict_dust_service = PredictDustServiceImpl(
        make_input_executor=MakeInputExecutorImpl(),
        inference_model_executor=InferenceModelExecutorImpl(),
    )

    return PredictDustFacade(predict_dust_service)
