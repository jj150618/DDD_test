from abc import ABCMeta, abstractmethod


class MakeInputExecutor(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def make_input_array(self, date: str, region: str):
        pass


class InferenceModelExecutor(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def inference(self, input_array, region:str):
        pass


class PredictDustService(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def return_predict_dust(self, date: str, region: str):
        pass


class PredictDustServiceImpl(PredictDustService):
    def __init__(
            self,
            make_input_executor: MakeInputExecutor,
            inference_model_executor: InferenceModelExecutor
    ) -> None:
        super().__init__()
        self.make_input_executor = make_input_executor
        self.inference_model_executor = inference_model_executor

    def return_predict_dust(self, date: str, region: str):
        return self.inference_model_executor.inference(
            input_array=self.make_input_executor.make_input_array(date=date, region=region),
            region=region
        )
