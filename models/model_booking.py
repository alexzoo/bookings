from pydantic import BaseModel
from datetime import date


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingResponse(BaseModel):
    bookingid: int
    booking: BookingRequest