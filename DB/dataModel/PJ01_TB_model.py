from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base


class BASE(DeclarativeBase):
    pass

class CORP_RCH_ECONOMIC(BASE):
    __tablename__ = "CORP_RCH_ECONOMIC"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    Num_Lab_Corp: Mapped[int] = mapped_column()
    Num_Rchr_Corp: Mapped[int] = mapped_column()
    Percent_DrMSc_Corp: Mapped[float] = mapped_column()
    Num_Lab_Dept: Mapped[int] = mapped_column()
    Num_Rchr_Dept: Mapped[int] = mapped_column()
    Percent_DrMSc_Dept: Mapped[float] = mapped_column()
    Num_Working_People: Mapped[int] = mapped_column()
    Num_Employment: Mapped[int] = mapped_column()
    Num_Non_Wage_Work: Mapped[int] = mapped_column()
    Num_Self_With_Employee: Mapped[int] = mapped_column()
    Num_Self_No_Employee: Mapped[int] = mapped_column()
    Num_Unpaid_FamSerive: Mapped[int] = mapped_column()
    Num_Wage_Work: Mapped[int] = mapped_column()
    Num_Commercial_Work: Mapped[int] = mapped_column()
    Num_Wage_Work: Mapped[int] = mapped_column()
    Num_Temp_Work: Mapped[int] = mapped_column()
    Num_Day_Work: Mapped[int] = mapped_column()
    Num_Work_Male: Mapped[int] = mapped_column()
    Num_Work_Female: Mapped[int] = mapped_column()
    Num_Unemployed: Mapped[int] = mapped_column()
    Percent_Unemployed: Mapped[float] = mapped_column()
    Num_15Up_employed: Mapped[int] = mapped_column()
    Num_Unemployed: Mapped[int] = mapped_column()
    Num_Unworking_People: Mapped[int] = mapped_column()
    Rate_Employment: Mapped[float] = mapped_column()
    Indx_Product_Leading_Economic: Mapped[float] = mapped_column()
    Indx_Product_Accomp_Economic: Mapped[float] = mapped_column()
    Indx_Product_All_Industries: Mapped[float] = mapped_column()
    Indx_Product_Mining: Mapped[float] = mapped_column()
    Indx_Product_Construction: Mapped[float] = mapped_column()
    Indx_Product_Services: Mapped[float] = mapped_column()
    Indx_Product_Public_Affairs: Mapped[float] = mapped_column()
    Machine_Orders_Total: Mapped[int] = mapped_column()
    Machine_Orders_Domestic: Mapped[int] = mapped_column()
    Machine_Orders_Distributors: Mapped[int] = mapped_column()
    Machine_Orders_International: Mapped[int] = mapped_column()
    Indx_Producer_Price: Mapped[float] = mapped_column()
    Indx_Capex: Mapped[float] = mapped_column()
    ReadyMix_Construction: Mapped[int] = mapped_column()
    BSI_OutLook: Mapped[float] = mapped_column()
    BSI_OutLook_Business: Mapped[float] = mapped_column()
    BSI_OutLook_Sales: Mapped[float] = mapped_column()
    BSI_OutLook_Fertility: Mapped[float] = mapped_column()
    BSI_OutLook_Financial: Mapped[float] = mapped_column()
    BSI_OutLook_Labor: Mapped[float] = mapped_column()
    BSI_Performance: Mapped[float] = mapped_column()
    BSI_Performance_Business: Mapped[float] = mapped_column()
    BSI_Performance_Sales: Mapped[float] = mapped_column()
    BSI_Performance_Fertility: Mapped[float] = mapped_column()
    BSI_Performance_Financial: Mapped[float] = mapped_column()
    BSI_Performance_Labor: Mapped[float] = mapped_column()



    








    # def __repr__(self)->str:
    #     return f"CORP_RCH_ECO(id={self.id!r})"