from pydantic import BaseModel

from models.booking_create_request_model import BookingCreateRequest


class BookingCreateResponse(BaseModel):
    bookingid: int
    booking: BookingCreateRequest
