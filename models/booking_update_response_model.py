from pydantic import BaseModel

from models.booking_dates_model import BookingDates


class BookingUpdateResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str
