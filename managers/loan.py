# DB
from db import database

# Models
from models import loan, RoleType, State


class LoanManager:
    @staticmethod
    async def get_loans(user):
        query = loan.select()
        if user["role"] == RoleType.complainer:
            query = query.where(loan.c.user_id == user["id"])
        elif user["role"] == RoleType.approver:
            query = query.where(loan.c.state == State.pending)
        return await database.fetch_all(query)

    @staticmethod
    async def create_loan(loan_data, user):
        loan_data["user_id"] = user["id"]
        id_ = await database.execute(loan.insert().values(**loan_data))
        return await database.fetch_one(loan.select().where(loan.c.id == id_))

    @staticmethod
    async def delete_loan(loan_id):
        await database.execute(loan.delete().where(loan.c.id == loan_id))

    @staticmethod
    async def approve(loan_id):
        await database.execute(
            loan.update().where(loan.c.id == loan_id).values(state=State.approved)
        )

    @staticmethod
    async def rejected(loan_id):
        await database.execute(
            loan.update().where(loan.c.id == loan_id).values(state=State.Rejected)
        )
