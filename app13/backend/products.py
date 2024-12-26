import reflex as rx
from sqlmodel import Field, select, Relationship, update
from typing import Optional
import sqlalchemy as sql
import sqlalchemy.orm as sqlorm
from .base import


class StockMaster(rx.Model, table=True):
    stockid: str = Field(default=None, primary_key=True)
    categoryid: str
    description: str
    minimo: int
    stock_image: Optional["Stock_Image"] = Relationship(
        back_populates="stock_master")
    loc_stocks: list["Locstock"] = Relationship(back_populates="stock_master")


class Stock_Image(rx.Model, table=True):
    id_image: int = Field(default=None, primary_key=True)
    id_product: str = Field(default=None, foreign_key="stockmaster.stockid")
    position: int
    cover: int
    imagen_principal: int
    stock_master: Optional[StockMaster] = Relationship(
        back_populates="stock_image")


class Locstock(rx.Model, table=True):
    loccode: str
    stockid: str = Field(default=None, primary_key=True,
                         foreign_key="stockmaster.stockid")
    quantity: int
    reorderlevel: int
    location: str
    lowstockfee: int
    stock_master: Optional["StockMaster"] = Relationship(
        back_populates="loc_stocks")


class Locations(rx.Model, table=True):
    loccode: str = Field(default=None, primary_key=True)
    locationname: str


class StockDisplayProducts(rx.Base):
    """Modelo para mostrar en la tabla."""
    loccode: str
    stockid: str
    description: str
    quantity: int
    location: str
    id_image: Optional[int]


class ProductsStates(rx.States):
    categoryid: str = ""

    @rx.event(background=True)
    async def get_all_products(self):
        async with self:
            with rx.session() as session:
                query = select(
                    StockMaster.stockid,
                    StockMaster.description,
                    Locstock.quantity,
                    Locstock.location,
                    Stock_Image.id_image,
                    Locations.locationname
                ).join(Locstock, StockMaster.stockid == Locstock.stockid).outerjoin(Stock_Image, StockMaster.stockid == Stock_Image.id_product
                                                                                    ).join(Locations, Locations.loccode == Locstock.loccode).where(Locstock.lowstockfee == 1)
                if self.selected_location != "ALL":
                    query = query.where(Locstock.loccode == self.selected_location,
                                        Locstock.lowstockfee == 1)

            results = session.exec(query).all()

            self.stocklowfee = [
                StockDisplayProducts(
                    stockid=row[0],
                    description=row[1],
                    quantity=row[2],
                    location=row[3],
                    id_image=row[4],
                    locationname=row[5],
                    # Add image_url and call get_image_path
                    image_url=self.get_image_path(row[4])
                ) for row in results
            ]
