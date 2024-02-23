# FastAPI Backend Boilerplate Codebase

Author: Anh T. Tra  
Email: anh.tra@c0x12c.com

> This codebase is the boilerplate for FastAPI backend application. It is organized based on Domain Driven Development approach. We separate the API logic (FastAPI) and the business logics, so that we can change any web framework/library very conveniently. Moreover, we apply Repository Pattern and Unit-of-Work pattern for dealing with database logics. Main processing logics are kept in service layer.

## Installation

```bash
pip install -r requirements.txt
```

## Initialize DB (sqlite)

```bash
alembic upgrade head
```

## Start API Server

```bash
make fastapi
```
