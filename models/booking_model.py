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


class BookingUpdateResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingGetByIdResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: str


class BookingID(BaseModel):
    bookingid: int


