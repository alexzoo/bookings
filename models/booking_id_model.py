from pydantic import BaseModel


class BookingID(BaseModel):
    bookingid: int
