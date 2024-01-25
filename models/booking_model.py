from pydantic import BaseModel
from datetime import date


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingCreateRequest(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingCreateResponse(BaseModel):
    bookingid: int
    booking: BookingCreateRequest


class BookingGetByIdResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str