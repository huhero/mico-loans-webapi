import enum


class RoleType(enum.Enum):
    admin = "admin"
    approver = "approver"
    complainer = "complainer"


class State(enum.Enum):
    approved = "Approved"
    pending = "Pending"
    rejected = "Rejected"
