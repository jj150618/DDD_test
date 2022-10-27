from fastapi import APIRouter
from routers.info import *
from routers.di import get_predict_dust_DI



router = APIRouter(
    prefix="/assignment",
    tags=["assignment"],
    responses={404: {"description": "Not found !"}}
)


@router.post("/predict_dust")
async def predict_dust(item: DateRegionInfo):
    predict_dust_facade = get_predict_dust_DI()
    return ResponseDustInfo(
        pm10=predict_dust_facade.return_predict_dust_result(date=item.date, region=item.region)
    )

