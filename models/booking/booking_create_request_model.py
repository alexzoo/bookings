from pydantic import BaseModel

from models.booking.booking_dates_model import BookingDates


class BookingCreateRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str
