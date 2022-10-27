from services.predict_dust.domain.predict_dust_service import PredictDustService


class PredictDustFacade():
    def __init__(self, predict_dust_service: PredictDustService) -> None:
        self.predict_dust_service = predict_dust_service

    def return_predict_dust_result(self, date: str, region: str):
        return self.predict_dust_service.return_predict_dust(date=date, region=region)
        
