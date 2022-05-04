# DB
from db import database

# Models
from models import loan, RoleType, State

# Services
from services.s3 import S3Service

# Constants
from constants import TEMP_FILE_FOLDER

# Utils
import uuid
import os
from utils.helpers import save_local_document

s3 = S3Service()


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
        # encoded_document = loan_data.pop("encoded_document")
        # extension = document.
        # name = f"{uuid.uuid4()}.{document.filename}"
        # path = os.path.join(TEMP_FILE_FOLDER, name)
        # save_local_document(path, document.file.read())
        # loan_data["contract_document_url"] = s3.upload(path, name)
        # os.remove(path)
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
